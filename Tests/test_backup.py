import unittest
import sys
sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import QItemSelectionModel
from main_window import MyMainWindow

class TestMyMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MyMainWindow()

    def test_window_creation(self):
        self.assertIsNotNone(self.window)

    def test_existing_backups_open(self):
        # Check if the existing backups window opens without any exceptions
        self.window.open_existing_backups()

    def test_backup_process(self):
        file1_path = r'C:/Users/Дайте пожрать/Downloads/Lab7/Laboratory work 7.pdf'
        file2_path = r'C:/Users/Дайте пожрать/Downloads/Lab7/Lab7.zcos'
        file3_path = r'C:/Users/Дайте пожрать/Downloads/Testfolder2/collinear.zip'
        file4_path = r'C:/Users/Дайте пожрать/Downloads/Testfolder2/deuce.png'
        file5_path = r'C:/Users/Дайте пожрать/Downloads/Testfolder2/putty.log'

        # Select the files in the CustomFileManager
        self.window.file_manager_widget.tree_view.setRootIndex(
            self.window.file_manager_widget.dir_model.index(file1_path)
        )
        self.window.file_manager_widget.tree_view.selectionModel().select(
            self.window.file_manager_widget.dir_model.index(file1_path),
            QItemSelectionModel.Select
        )
        
        self.window.file_manager_widget.tree_view.setRootIndex(
            self.window.file_manager_widget.dir_model.index(file2_path)
        )
        self.window.file_manager_widget.tree_view.selectionModel().select(
            self.window.file_manager_widget.dir_model.index(file2_path),
            QItemSelectionModel.Select
        )

        self.window.file_manager_widget.tree_view.setRootIndex(
            self.window.file_manager_widget.dir_model.index(file3_path)
        )
        self.window.file_manager_widget.tree_view.selectionModel().select(
            self.window.file_manager_widget.dir_model.index(file3_path),
            QItemSelectionModel.Select
        )

        self.window.file_manager_widget.tree_view.setRootIndex(
            self.window.file_manager_widget.dir_model.index(file4_path)
        )
        self.window.file_manager_widget.tree_view.selectionModel().select(
            self.window.file_manager_widget.dir_model.index(file4_path),
            QItemSelectionModel.Select
        )

        self.window.file_manager_widget.tree_view.setRootIndex(
            self.window.file_manager_widget.dir_model.index(file5_path)
        )
        self.window.file_manager_widget.tree_view.selectionModel().select(
            self.window.file_manager_widget.dir_model.index(file5_path),
            QItemSelectionModel.Select
        )

        # Trigger the backup process (assuming it's in CustomFileManager)
        self.window.file_manager_widget.select_items()


    def tearDown(self):
        del self.window
        del self.app

if __name__ == '__main__':
    unittest.main()
    # Start the main window after the tests
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())



#C:/Users/Дайте пожрать/Downloads/Lab7
#Laboratory work 7.pdf
#Lab7.zcos
#sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
#C:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/Backups