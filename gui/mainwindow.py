# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    gen_ct = 10
    color_mode = "rgb"
    pad_mode = "dead"
    dither_mode = "2x2"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.default_file = "../images/default.png"
        self.current_file = "../images/utahteapot.jpg"
        pixmap = QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio)
        self.ui.image.setPixmap(pixmap)

    @Slot(int)
    def setGenCount(self, ct):
        self.gen_ct = ct
        print(self.gen_ct)

    @Slot(str)
    def setColorMode(self, mode):
        self.color_mode = mode.lower()
        print(self.color_mode)

    @Slot(str)
    def setPadMode(self, mode):
        self.pad_mode = mode.lower()
        print(self.pad_mode)

    @Slot(str)
    def setDitherMode(self, mode):
        self.dither_mode = mode
        print(self.dither_mode)

    @Slot()
    def startGame(self):
        pass


#maybe overload QLabel's resizeEvent instead?


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
