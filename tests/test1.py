import unittest
import os
import shutil
import tempfile

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Создаем временную директорию для тестов
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Удаляем временную директорию после завершения тестов
        shutil.rmtree(self.test_dir)

    def create_temp_file(self, filename, content):
        # Создаем временный файл с заданным содержимым
        file_path = os.path.join(self.test_dir, filename)
        with open(file_path, "w") as file:
            file.write(content)
        return file_path

    def test_file_copy(self):
        # Создаем временный файл с содержимым
        source_file = self.create_temp_file("source.txt", "Hello, World!")

        # Копируем файл в другое место
        destination_file = os.path.join(self.test_dir, "destination.txt")
        shutil.copy(source_file, destination_file)

        # Проверяем, что файл был скопирован успешно
        self.assertTrue(os.path.exists(destination_file))
        with open(destination_file, "r") as file:
            content = file.read()
        self.assertEqual(content, "Hello, World!")

    def test_file_deletion(self):
        # Создаем временный файл
        file_to_delete = self.create_temp_file("file_to_delete.txt", "To be deleted!")

        # Удаляем файл
        os.remove(file_to_delete)

        # Проверяем, что файл был удален успешно
        self.assertFalse(os.path.exists(file_to_delete))

    def test_file_rename(self):
        # Создаем временный файл
        original_file = self.create_temp_file("original.txt", "Content to be renamed!")

        # Переименовываем файл
        new_file_name = os.path.join(self.test_dir, "renamed.txt")
        os.rename(original_file, new_file_name)

        # Проверяем, что файл был переименован успешно
        self.assertFalse(os.path.exists(original_file))
        self.assertTrue(os.path.exists(new_file_name))

    def test_directory_creation(self):
        # Создаем новую временную директорию
        new_directory = os.path.join(self.test_dir, "new_directory")
        os.makedirs(new_directory)

        # Проверяем, что директория была создана успешно
        self.assertTrue(os.path.exists(new_directory))
        self.assertTrue(os.path.isdir(new_directory))

    def test_directory_deletion(self):
        # Создаем временную директорию
        directory_to_delete = os.path.join(self.test_dir, "directory_to_delete")
        os.makedirs(directory_to_delete)

        # Удаляем директорию
        shutil.rmtree(directory_to_delete)

        # Проверяем, что директория была удалена успешно
        self.assertFalse(os.path.exists(directory_to_delete))

if __name__ == "__main__":
    unittest.main()
