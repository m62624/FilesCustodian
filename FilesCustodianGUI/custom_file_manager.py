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

    def __init__(self, sources, destination):
        super().__init__()
        self.sources = sources
        self.destination = destination
        

    def run(self):
        try:
            # Создаем путь с текущей датой и временем
            current_datetime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            destination_path = os.path.join(self.destination, current_datetime)

            # Создаем папку назначения
            os.makedirs(destination_path)

            # Копируем файлы в новую папку
            for source in self.sources:
                shutil.copy2(source, destination_path)

        except Exception as e:
            print(f"Error copying files: {e}")

    def emit_progress(self, progress):
        self.progress_changed.emit(progress)


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

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def start_copy(self):
        self.copy_thread.start()
        self.exec_()


class CustomFileManager(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Custom File Manager")
        self.setGeometry(100, 100, 700, 700)

        layout = QVBoxLayout()

        self.dir_model = QFileSystemModel()
        home_dir = QDir.homePath()  # Получаем домашнюю директорию пользователя
        self.dir_model.setRootPath(home_dir)  # Устанавливаем домашнюю директорию

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.dir_model)
        self.tree_view.setRootIndex(self.dir_model.index(home_dir))

        # Включаем поддержку выбора нескольких элементов
        self.tree_view.setSelectionMode(QTreeView.MultiSelection)

        layout.addWidget(self.tree_view)

        # Создаем кнопки "Выбрать" и "Отмена"
        select_button = QPushButton(self.tr("Сделать бэкап"))
        cancel_button = QPushButton(self.tr("Отмена"))
        button_layout = QVBoxLayout()
        button_layout.addWidget(select_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Привязываем действие к кнопке "Выбрать"
        select_button.clicked.connect(self.select_items)

        # Привязываем действие к кнопке "Отмена"
        cancel_button.clicked.connect(self.cancel_selection)

        # Список для хранения выбранных файлов и папок
        self.selected_items = []

    def select_items(self):
        selected_indexes = self.tree_view.selectionModel().selectedIndexes()

        # Создаем множество для уникальных элементов
        unique_items = set()

        # Получаем пути к выбранным файлам и папкам
        for index in selected_indexes:
            file_path = self.dir_model.filePath(index)
            unique_items.add(file_path)

        # Очищаем список выбранных элементов и добавляем уникальные элементы
        self.selected_items.clear()
        self.selected_items.extend(unique_items)

        settings_manager = SettingsManager()
        settings_manager.load_settings()
        # Выводим выбранные элементы в консоль (вы можете использовать их как угодно)
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
