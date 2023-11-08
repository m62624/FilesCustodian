from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QVBoxLayout

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

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

    def save_settings(self):
        selected_theme = self.theme_combo.currentText()
        selected_language = self.language_combo.currentText()
        # Добавьте код для сохранения выбранного языка

if __name__ == "__main__":
    settings_window = SettingsWindow()
    settings_window.exec_()


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

    # Добавьте методы для выбора папки-источника и папки-приемника
