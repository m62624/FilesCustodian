import os
import sys

sys.path.append("../FilesCustodian/FilesCustodianGUI")
import json
import unittest
from unittest.mock import mock_open, patch
from FilesCustodianGUI.file_json import SettingsManager


class TestSettingsManager(unittest.TestCase):
    def setUp(self):
        # Имя временного файла для теста
        self.test_settings_file = "test_settings.json"

    def tearDown(self):
        # Удаляем временный файл после завершения тестов
        if os.path.exists(self.test_settings_file):
            os.remove(self.test_settings_file)

    def test_load_settings(self):
        # Создаем временный файл настроек с определенными значениями
        with open(self.test_settings_file, "w") as file:
            json.dump({"theme": 1, "language": 2, "backup_path": "/tmp"}, file)

        # Используем patch для замены реального пути к файлу на временный файл
        with patch(
            "FilesCustodianGUI.file_json.settings_file", self.test_settings_file
        ):
            settings_manager = SettingsManager()
            settings_manager.load_settings()

            # Проверяем, что загруженные настройки соответствуют ожидаемым значениям
            self.assertEqual(
                settings_manager.settings,
                {"theme": 1, "language": 2, "backup_path": "/tmp"},
            )

    def test_get_setting(self):
        # Используем patch для замены реального пути к файлу на временный файл
        with patch(
            "FilesCustodianGUI.file_json.settings_file", self.test_settings_file
        ):
            settings_manager = SettingsManager()

            # Проверяем, что получаем значение по умолчанию, если ключ отсутствует
            result = settings_manager.get_setting(
                "nonexistent_key", default="default_value"
            )
            self.assertEqual(result, "default_value")

            # Устанавливаем внутренние настройки и проверяем, что get_setting возвращает правильное значение
            settings_manager.settings = {
                "theme": 1,
                "language": 2,
                "backup_path": "/tmp",
            }
            result = settings_manager.get_setting("theme")
            self.assertEqual(result, 1)

# Запуск тестов
if __name__ == "__main__":
    unittest.main()