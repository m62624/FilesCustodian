import sys
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel, QTreeView, QVBoxLayout, QApplication, QWidget, QPushButton
from PyQt5.QtCore import QDir

class CustomFileManager(QMainWindow):
    def __init__(self):
        super().__init__()

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
        select_button = QPushButton(self.tr("Выбрать"))
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

        # Выводим выбранные элементы в консоль (вы можете использовать их как угодно)
        print("Выбранные элементы:")
        for item in self.selected_items:
            print(item)

    def cancel_selection(self):
        # Сбрасываем выделение в QTreeView
        self.tree_view.selectionModel().clearSelection()
        print(self.tr("Сброс выбора"))


