import sys
sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRect
from main_window import MyMainWindow, SettingsWindow

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_window_creation(self):
        window = MyMainWindow()
        self.assertIsNotNone(window)
        self.assertEqual(window.windowTitle(), "Мое главное окно")
        self.assertEqual(window.geometry(), QRect(100, 100, 700, 700))

    def test_file_manager_widget(self):
        window = MyMainWindow()
        self.assertIsNotNone(window.selected_files_widget)
        self.assertIsNotNone(window.selected_files_model)
        self.assertIsNotNone(window.file_manager_widget)
        
    def test_is_success(self):
    # Ваш тестовый код здесь
        self.assertTrue(True)  # Пример утверждения, чтобы тест всегда проходил успешно

if __name__ == "__main__":
    unittest.main(verbosity=2)
