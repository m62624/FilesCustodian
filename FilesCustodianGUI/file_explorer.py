import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

class FileExplorerPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.btn = QPushButton("Открыть файл")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.le = QLabel("Выбранный файл будет здесь.")
        layout.addWidget(self.le)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle("Панель файлового менеджера")

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'All Files (*)')
        if fname:
            self.le.setPixmap(QPixmap(fname))
            with open(fname, 'r') as file:
                data = file.read()
                self.contents.setText(data)
