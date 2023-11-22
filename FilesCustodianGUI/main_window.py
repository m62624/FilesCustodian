import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QAction,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
    QSplitter,
    QFileDialog,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir, QSize
from settings_window import SettingsWindow, CopyPanel
from custom_file_manager import CustomFileManager
from keys import (
    language_mapping,
    theme_mapping,
    get_index_from_text,
    reverse_language_mapping,
    reverse_theme_mapping,
)
from file_json import SettingsManager


class MyMainWindow(QMainWindow):
    def save_settings(self):
        selected_theme = get_index_from_text(
            self.settings_window.theme_combo.currentText(), reverse_theme_mapping
        )
        selected_language = get_index_from_text(
            self.settings_window.language_combo.currentText(), reverse_language_mapping
        )

        theme_index = list(theme_mapping.keys())[
            list(theme_mapping.values()).index(selected_theme)
        ]
        language_index = list(language_mapping.keys())[
            list(language_mapping.values()).index(selected_language)
        ]
        settings_file_manager = SettingsManager()
        settings_file_manager.save_settings("theme", theme_index)
        settings_file_manager.save_settings("language", language_index)

    def update_existing_backups(self):
        settings_file_manager = SettingsManager()
        settings_file_manager.load_settings()
        existing_backups_path = settings_file_manager.get_setting("backup_folder")
        self.existing_backups_path = existing_backups_path

    def __init__(self):
        super().__init__()
        settings_file_manager = SettingsManager()
        self.settings_window = SettingsWindow()
        settings_file_manager.load_settings()
        self.settings_window.theme_combo.setCurrentIndex(
            settings_file_manager.get_setting("theme")
        )
        self.settings_window.language_combo.setCurrentIndex(
            settings_file_manager.get_setting("language")
        )
        self.setWindowTitle(self.tr("FilesCustodian v0.0.2"))
        self.setGeometry(100, 100, 700, 700)

        menubar = self.menuBar()

        exit_action = QAction(self.tr("Выход"), self)
        exit_action.triggered.connect(self.close)

        settings_menu = menubar.addMenu(self.tr("Настройки"))

        open_settings_action = QAction(self.tr("Язык и тема"), self)
        open_settings_action.triggered.connect(self.open_settings)

        open_copy_panel_action = QAction(self.tr("Копирование файлов"), self)
        open_copy_panel_action.triggered.connect(self.open_copy_panel)

        open_existing_backups_action = QAction(self.tr("Выбор существующих бэкапов"), self)
        open_existing_backups_action.triggered.connect(self.open_existing_backups)

        settings_menu.addAction(open_settings_action)
        settings_menu.addAction(open_copy_panel_action)
        settings_menu.addAction(open_existing_backups_action)

        # Создаем виджет для отображения выбранных файлов
        self.selected_files_widget = QListWidget()

        # Создаем виджет для отображения файлового менеджера
        self.file_manager_widget = CustomFileManager()

        # Создаем виджет для отображения существующих бэкапов
        self.list_widget = QListWidget()
        self.large_icon_size = QSize(128, 128)
        self.small_icon_size = QSize(32, 32)

        # Устанавливаем размеры иконок
        self.list_widget.setIconSize(self.small_icon_size)

        # Устанавливаем корневой путь для списка существующих бэкапов
        self.update_existing_backups()

        # Создаем разделитель для размещения виджетов
        splitter = QSplitter()
        splitter.addWidget(self.file_manager_widget)
        splitter.addWidget(self.list_widget)

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

    def open_existing_backups(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Выбрать папку с существующими бэкапами", options=options)

        if folder_path:
            settings_file_manager = SettingsManager()
            settings_file_manager.load_settings()
            settings_file_manager.save_settings("backup_folder", folder_path)
            self.update_existing_backups()
            self.list_widget.clear()

            # Заполняем список существующих бэкапов
            for entry in QDir(self.existing_backups_path).entryInfoList(QDir.NoDotAndDotDot | QDir.AllDirs):
                item = QListWidgetItem(entry.fileName(), self.list_widget)
                icon = QIcon(entry.filePath())
                item.setIcon(icon)

            self.list_widget.show()


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
