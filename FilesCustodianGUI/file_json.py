import json
import os

settings_file = os.path.join(
    os.path.expanduser("~/.config/FilesCustodian"), "settings.json"
)


class SettingsManager:
    default_settings = {
        "theme": 0,  # 0 - Тема по умолчанию
        "language": 0,  # 0 - Английский
        "backup_path": os.path.join(os.path.expanduser("~"), "BackupsOfFilesCustodian"),
    }

    def __init__(self):
        self.settings_file = settings_file
        self.settings = {}

    def load_settings(self):
        if not os.path.exists(self.settings_file):
            os.makedirs(
                os.path.dirname(self.settings_file), exist_ok=True
            )  # Создаем директорию, если её нет

            # Создаем файл настроек с значениями по умолчанию
            with open(self.settings_file, "w") as file:
                json.dump(self.default_settings, file)

        with open(self.settings_file, "r") as file:
            self.settings = json.load(file)

    def save_settings(self, key, value):
        # Загружаем текущие настройки (если файл существует)
        if os.path.exists(settings_file):
            with open(settings_file, "r") as file:
                settings = json.load(file)
        else:
            settings = {}  # Если файла нет, создаем пустой словарь

            # Устанавливаем новое значение
        settings[key] = value
        # Записываем настройки в файл JSON
        with open(settings_file, "w") as file:
            json.dump(settings, file)

        return settings  # Возвращаем обновленные настройки

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)
