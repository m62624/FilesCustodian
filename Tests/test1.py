import sys
sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
import custom_file_manager
import pytest
from PyQt5.QtWidgets import QApplication
from pytestqt import qtbot

@pytest.fixture
def app(qtbot):
    # Создаем экземпляр QApplication перед запуском приложения
    app = QApplication([])
    yield app
    app.quit()

@pytest.mark.incremental
class TestCustomFileManager:

    @pytest.fixture(autouse=True)
    def setup(self, app, qtbot):
        self.qtbot = qtbot
        self.file_manager = custom_file_manager.CustomFileManager()

    def test_file_manager_window_displayed(self):
        # Проверяем, что окно CustomFileManager отображается
        self.qtbot.addWidget(self.file_manager)
        self.qtbot.waitExposed(self.file_manager)
        assert self.file_manager.isVisible()

    def test_select_items(self):
        # Выбираем элементы в файловом менеджере (здесь можно использовать qtbot.mouseClick или другие методы qtbot)
        # Здесь мы просто симулируем выбор элементов
        self.file_manager.tree_view.selectionModel().select(
            self.file_manager.dir_model.index(0, 0),  # Замените на индекс(ы) вашего выбора
            self.file_manager.tree_view.selectionModel().Select
        )

        # Запускаем метод для выбора элементов
        self.file_manager.select_items()

        # Проверяем, что список выбранных элементов не пустой
        assert len(self.file_manager.selected_items) > 0

    @pytest.mark.xfail(reason="Custom File Manager cannot be tested from the command line")
    def test_main(self):
        # Проверяем, что приложение CustomFileManager может быть открыто без ошибок
        custom_file_manager.main()
