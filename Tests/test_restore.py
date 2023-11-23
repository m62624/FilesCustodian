import sys
import unittest
sys.path.append('c:/Users/Дайте пожрать/Desktop/Fc/FilesCustodian/FilesCustodianGUI')
from PyQt5.QtWidgets import QApplication
from main_window import MyMainWindow

class TestRestoreBackup(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MyMainWindow()

    def test_restore_backup_after_settings_window_open(self):

        # Assuming the specified backup folder exists in the path
        backup_folder_path = r'C:/Users/Дайте пожрать/Downloads/TestBackup'

        # Set the backup folder in the settings
        self.window.settings_window.path_backups_combo.setCurrentText(backup_folder_path)

        # Trigger the restore backup process
        self.window.restore_backup()

        # Add assertions here to check if the restore backup process was initiated successfully
        # You may need to add signals or other mechanisms to determine when the restore backup is complete

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

#r'C:/Users/Дайте пожрать/Downloads/TestBackup'