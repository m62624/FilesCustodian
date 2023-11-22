from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)
from file_json import SettingsManager
from keys import (
    get_index_from_text,
    reverse_theme_mapping,
    reverse_language_mapping,
    language_mapping,
    theme_mapping,
)


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        settings_manager = SettingsManager()
        settings_manager.load_settings()

        self.setWindowTitle(self.tr("Настройки"))
        self.setGeometry(200, 200, 300, 200)

        theme_label = QLabel(self.tr("Тема:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItem(self.tr("Светлая"))
        self.theme_combo.addItem(self.tr("Темная"))

        language_label = QLabel(self.tr("Язык:"))
        self.language_combo = QComboBox()
        self.language_combo.addItem(self.tr("Русский"))
        self.language_combo.addItem(self.tr("Английский"))

        self.path_backups_combo = QComboBox()
        self.path_backups_combo.addItem(self.tr("По умолчанию"))

        save_button = QPushButton(self.tr("Сохранить"))
        save_button.clicked.connect(self.save_settings)

        layout = QVBoxLayout()
        layout.addWidget(theme_label)
        layout.addWidget(self.theme_combo)
        layout.addWidget(language_label)
        layout.addWidget(self.language_combo)
        layout.addWidget(save_button)
        self.setLayout(layout)
        self.theme_combo.setCurrentText(
            theme_mapping[settings_manager.get_setting("theme")]
        )
        self.language_combo.setCurrentText(
            language_mapping[settings_manager.get_setting("language")]
        )

        # Создаем экземпляр SettingsManager

    def save_settings(self):
        selected_theme = get_index_from_text(
            self.theme_combo.currentText(), reverse_theme_mapping
        )
        selected_language = get_index_from_text(
            self.language_combo.currentText(), reverse_language_mapping
        )
        print(selected_language, selected_theme)
        settings_manager = SettingsManager()
        settings_manager.load_settings()
        settings_manager.save_settings("theme", selected_theme)
        settings_manager.save_settings("language", selected_language)


class CopyPanel(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.tr("Настройки копирования"))
        self.setGeometry(200, 200, 400, 200)

        backup_folder_label = QLabel(self.tr("Папка для бэкапов:"))
        self.backup_folder_button = QPushButton(self.tr("Выбрать папку"))
        self.backup_folder_button.clicked.connect(self.select_backup_folder)

        save_button = QPushButton(self.tr("Сохранить"))
        save_button.clicked.connect(self.save_settings)

        cancel_button = QPushButton(self.tr("Отмена"))
        cancel_button.clicked.connect(self.close_window)

        error_label = QLabel()
        error_label.setStyleSheet("color: red;")

        layout = QVBoxLayout()
        layout.addWidget(backup_folder_label)
        layout.addWidget(self.backup_folder_button)
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)
        layout.addWidget(error_label)
        self.setLayout(layout)

    def select_backup_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(
            self, self.tr("Выбрать папку для бэкапов"), options=options
        )

        if folder_path:
            self.backup_folder_button.setText(folder_path)

    def save_settings(self):
        settings_manager = SettingsManager()
        settings_manager.load_settings()
        settings_manager.save_settings(
            "backup_folder", self.backup_folder_button.text()
        )
        # Добавьте код для сохранения пути бэкапа ваших файлов
        # settings_manager.save_settings("backup_folder", backup_folder)

        # После сохранения настроек закройте окно:
        self.close()

    def close_window(self):
        self.close()
