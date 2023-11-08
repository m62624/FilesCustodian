import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTreeView, QVBoxLayout, QWidget, QSplitter, QFileSystemModel
from settings_window import SettingsWindow, CopyPanel
from custom_file_manager import CustomFileManager
from PyQt5.QtCore import QDir

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("Мое главное окно"))
        self.setGeometry(100, 100, 700, 700)

        menubar = self.menuBar()

        exit_action = QAction(self.tr("Выход"), self)
        exit_action.triggered.connect(self.close)

        settings_menu = menubar.addMenu(self.tr("Настройки"))

        open_settings_action = QAction(self.tr("Язык и тема"), self)
        open_settings_action.triggered.connect(self.open_settings)

        open_copy_panel_action = QAction(self.tr("Копирование файлов"), self)
        open_copy_panel_action.triggered.connect(self.open_copy_panel)



        settings_menu.addAction(open_settings_action)
        settings_menu.addAction(open_copy_panel_action)


        # Создаем виджет для отображения выбранных файлов
        self.selected_files_widget = QTreeView()
        self.selected_files_model = QFileSystemModel()
        self.selected_files_model.setFilter(QDir.Files | QDir.AllDirs)
        self.selected_files_widget.setModel(self.selected_files_model)
        self.selected_files_widget.setHeaderHidden(True)

        # Создаем виджет для отображения файлового менеджера
        self.file_manager_widget = CustomFileManager()

        # Создаем разделитель для размещения виджетов
        splitter = QSplitter()
        splitter.addWidget(self.selected_files_widget)
        splitter.addWidget(self.file_manager_widget)

        layout = QVBoxLayout()
        layout.addWidget(splitter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_settings(self):
        settings_window = SettingsWindow()
        settings_window.exec_()

    def open_copy_panel(self):
        copy_panel = CopyPanel()
        copy_panel.exec_()


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()