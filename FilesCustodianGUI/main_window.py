import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QPushButton, QVBoxLayout, QWidget
from settings_window import SettingsWindow, CopyPanel
from file_explorer import FileExplorerPanel

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

        # Создаем кнопку для открытия FileExplorerPanel
        open_file_explorer_button = QPushButton(self.tr("Открыть файловый менеджер"), self)
        open_file_explorer_button.clicked.connect(self.open_file_explorer)
        open_file_explorer_button.setGeometry(200, 300, 300, 50)  # Устанавливаем позицию и размер кнопки

    def open_settings(self):
        settings_window = SettingsWindow()
        settings_window.exec_()

    def open_copy_panel(self):
        copy_panel = CopyPanel()
        copy_panel.exec_()

    def open_file_explorer(self):
        #    app = QApplication(sys.argv)
        ex = FileExplorerPanel()
        ex.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
