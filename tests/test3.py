import unittest
import os
import tempfile


class TestAnotherFileOperations(unittest.TestCase):
    def setUp(self):
        # Создаем временную директорию для тестов
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Удаляем временную директорию после завершения тестов
        os.rmdir(self.test_dir)

    def create_temp_file(self, filename, content):
        # Создаем временный файл с заданным содержимым
        file_path = os.path.join(self.test_dir, filename)
        with open(file_path, "w") as file:
            file.write(content)
        return file_path

    def test_file_reading(self):
        # Создаем временный файл с содержимым
        source_content = "This is a test content."
        source_file = self.create_temp_file("source.txt", source_content)

        # Читаем содержимое файла
        with open(source_file, "r") as file:
            content = file.read()

        # Проверяем, что прочитанное содержимое совпадает с ожидаемым
        self.assertEqual(content, source_content)

    def test_file_writing(self):
        # Создаем временный файл
        destination_file = os.path.join(self.test_dir, "destination.txt")

        # Записываем в файл
        content_to_write = "This is content to write."
        with open(destination_file, "w") as file:
            file.write(content_to_write)

        # Читаем содержимое файла
        with open(destination_file, "r") as file:
            content = file.read()

        # Проверяем, что записанное содержимое совпадает с ожидаемым
        self.assertEqual(content, content_to_write)

    def test_file_appending(self):
        # Создаем временный файл
        destination_file = os.path.join(self.test_dir, "destination.txt")

        # Записываем в файл начальное содержимое
        initial_content = "This is initial content."
        with open(destination_file, "w") as file:
            file.write(initial_content)

        # Дописываем в файл
        content_to_append = " This is additional content."
        with open(destination_file, "a") as file:
            file.write(content_to_append)

        # Читаем содержимое файла
        with open(destination_file, "r") as file:
            content = file.read()

        # Проверяем, что записанное содержимое совпадает с ожидаемым
        self.assertEqual(content, initial_content + content_to_append)


if __name__ == "__main__":
    unittest.main()
