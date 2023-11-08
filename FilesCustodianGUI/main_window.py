import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from settings_window import SettingsWindow,CopyPanel

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

    def open_settings(self):
        settings_window = SettingsWindow()
        settings_window.exec_()

    def open_copy_panel(self):
        copy_panel = CopyPanel()
        copy_panel.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
