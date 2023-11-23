from PyQt5.QtWidgets import (
    QMainWindow,
    QFileSystemModel,
    QTreeView,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QDialog,
    QLabel,
    QProgressBar,
)
from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import shutil
import os
from settings_window import SettingsManager
from datetime import datetime


class CopyThread(QThread):
    progress_changed = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, sources, destination):
        super().__init__()
        self.sources = sources
        self.destination = destination

    def run(self):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            destination_path = os.path.join(self.destination, current_datetime)
            os.makedirs(destination_path)

            total_files = len(self.sources)
            log_file_path = os.path.join(destination_path, "restore.log")
            with open(log_file_path, "w") as log_file:
                for i, source in enumerate(self.sources):
                    # Используйте os.path.basename для получения имени файла или директории
                    relative_name = os.path.basename(source)
                    shutil.copy2(source, destination_path)
                    log_file.write(f"{relative_name}\t{source}\n")
                    progress = int((i + 1) / total_files * 100)
                    self.progress_changed.emit(progress)

        except Exception as e:
            print(f"Error copying files: {e}")
        finally:
            self.finished.emit()

        # Завершаем цикл событий в потоке
        self.quit()
        # Дожидаемся завершения потока
        self.wait()

    def restore_from_log(self, log_file_path):
        try:
            total_files = sum(1 for line in open(log_file_path))
            with open(log_file_path, "r") as log_file:
                for i, line in enumerate(log_file):
                    print("вот полученый путь из файла {}".format(line))
                    # Разбиваем строку на относительный путь и оригинальный путь
                    relative_path, original_path = line.strip().split("\t")
                    # Полный путь к файлу в папке восстановления
                    restored_file_path = os.path.join(
                        os.path.dirname(log_file_path), relative_path
                    )
                    print("откуда {}".format(restored_file_path))
                    print("куда {}".format(original_path))
                    # Восстанавливаем файл на оригинальное место
                    shutil.copy2(restored_file_path, original_path)
                    progress = int((i + 1) / total_files * 100)
                    self.progress_changed.emit(progress)
        except Exception as e:
            print(f"Error restoring files: {e}")
        finally:
            self.finished.emit()


class CopyProgressDialog(QDialog):
    def __init__(self, sources, destination):
        super().__init__()

        self.setWindowTitle("Сохранение файлов")

        layout = QVBoxLayout()

        self.progress_label = QLabel("Прогресс:")
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)

        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(cancel_button)

        self.setLayout(layout)

        self.copy_thread = CopyThread(sources, destination)
        self.copy_thread.progress_changed.connect(self.update_progress)
        self.copy_thread.finished.connect(self.accept)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def restore(self, log_file_path):
        self.copy_thread.restore_from_log(log_file_path)

    def start_copy(self):
        self.copy_thread.start()
        result = self.exec_()
        if result == QDialog.Accepted:
            # Закрываем диалог только если он был закрыт пользователем, а не автоматически после завершения
            self.copy_thread.wait()


class CustomFileManager(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Custom File Manager")
        self.setGeometry(100, 100, 700, 700)

        layout = QVBoxLayout()

        self.dir_model = QFileSystemModel()
        home_dir = QDir.homePath()
        self.dir_model.setRootPath(home_dir)

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.dir_model)
        self.tree_view.setRootIndex(self.dir_model.index(home_dir))
        self.tree_view.setSelectionMode(QTreeView.MultiSelection)

        layout.addWidget(self.tree_view)

        select_button = QPushButton(self.tr("Сделать бэкап"))
        cancel_button = QPushButton(self.tr("Отмена"))
        button_layout = QVBoxLayout()
        button_layout.addWidget(select_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        select_button.clicked.connect(self.select_items)
        cancel_button.clicked.connect(self.cancel_selection)

        self.selected_items = []

    def select_items(self):
        selected_indexes = self.tree_view.selectionModel().selectedIndexes()

        unique_items = set()

        for index in selected_indexes:
            file_path = self.dir_model.filePath(index)
            unique_items.add(file_path)

        self.selected_items.clear()
        self.selected_items.extend(unique_items)

        settings_manager = SettingsManager()
        settings_manager.load_settings()

        copy_dialog = CopyProgressDialog(
            self.selected_items, settings_manager.get_setting("backup_folder")
        )
        copy_dialog.start_copy()
        self.main_window.update_backup_list()
        # update_backup_list()
        # print("Выбранные элементы:")
        # for item in self.selected_items:
        #     print

    def cancel_selection(self):
        # Сбрасываем выделение в QTreeView
        self.tree_view.selectionModel().clearSelection()
        print(self.tr("Сброс выбора"))
