import sys

from PyQt5.QtWidgets import QApplication

from photo_editor import EasyPzUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = EasyPzUI()
    sys.exit(app.exec_())
