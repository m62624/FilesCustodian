from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QVBoxLayout
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
        self.setGeometry(200, 200, 300, 200)

        # Добавьте код для создания виджетов:
        # - поле для выбора папки-источника
        # - поле для выбора папки-приемника
        # - кнопка "Сохранить"
        # - кнопка "Отмена"
        # - метка для отображения ошибок

        layout = QVBoxLayout()
        # Добавьте виджеты на layout
        self.setLayout(layout)

    def save_settings(self):
        # Добавьте код для сохранения настроек:
        # - папка-источник
        # - папка-приемник
        # - маска для фильтрации файлов
        # - маска для фильтрации папок

        # После сохранения настроек закройте окно:
        self.close()

    def close_window(self):
        self.close()
