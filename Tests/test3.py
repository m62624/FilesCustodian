import sys
sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
import unittest
from PyQt5.QtWidgets import QApplication
from settings_window import SettingsWindow

class TestSettingsWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = SettingsWindow()

    def test_window_title(self):
        self.assertEqual(self.window.windowTitle(), "Настройки")

    def test_theme_combo_items(self):
        expected_items = ["Светлая", "Темная"]
        combo_items = [self.window.theme_combo.itemText(i) for i in range(self.window.theme_combo.count())]
        self.assertEqual(combo_items, expected_items)

    def test_language_combo_items(self):
        expected_items = ["Русский", "Английский"]
        combo_items = [self.window.language_combo.itemText(i) for i in range(self.window.language_combo.count())]
        self.assertEqual(combo_items, expected_items)

    def tearDown(self):
        self.window.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
