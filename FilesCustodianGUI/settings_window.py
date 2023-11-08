from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QVBoxLayout

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Настройки")
        self.setGeometry(200, 200, 300, 200)

        theme_label = QLabel("Тема:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Светлая")
        self.theme_combo.addItem("Темная")

        language_label = QLabel("Язык:")
        self.language_combo = QComboBox()
        self.language_combo.addItem("Русский")
        self.language_combo.addItem("Английский")

        save_button = QPushButton("Сохранить")
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
