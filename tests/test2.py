import os
import sys
sys.path.append("../FilesCustodian/FilesCustodianGUI")
import unittest
from FilesCustodianGUI.keys import (
    theme_mapping,
    language_mapping,
    reverse_theme_mapping,
    reverse_language_mapping,
    get_index_from_text,
)


class TestKeys(unittest.TestCase):
    def test_theme_mapping(self):
        # Проверяем, что theme_mapping корректно отображает индексы в текстовые значения
        self.assertEqual(theme_mapping[0], "Светлая")
        self.assertEqual(theme_mapping[1], "Темная")

    def test_language_mapping(self):
        # Проверяем, что language_mapping корректно отображает индексы в текстовые значения
        self.assertEqual(language_mapping[0], "Русский")
        self.assertEqual(language_mapping[1], "Английский")

    def test_reverse_theme_mapping(self):
        # Проверяем, что reverse_theme_mapping корректно отображает текстовые значения в индексы
        self.assertEqual(reverse_theme_mapping["Светлая"], 0)
        self.assertEqual(reverse_theme_mapping["Темная"], 1)

    def test_reverse_language_mapping(self):
        # Проверяем, что reverse_language_mapping корректно отображает текстовые значения в индексы
        self.assertEqual(reverse_language_mapping["Русский"], 0)
        self.assertEqual(reverse_language_mapping["Английский"], 1)

    def test_get_index_from_text(self):
        # Проверяем, что get_index_from_text возвращает правильные индексы для текстовых значений
        self.assertEqual(get_index_from_text("Светлая", theme_mapping), 0)
        self.assertEqual(get_index_from_text("Темная", theme_mapping), 1)
        self.assertEqual(get_index_from_text("Русский", language_mapping), 0)
        self.assertEqual(get_index_from_text("Английский", language_mapping), 1)

        # Проверяем, что get_index_from_text возвращает None для неправильных текстовых значений
        self.assertIsNone(get_index_from_text("Неизвестное значение", theme_mapping))
        self.assertIsNone(get_index_from_text("Неизвестное значение", language_mapping))


if __name__ == "__main__":
    unittest.main()
