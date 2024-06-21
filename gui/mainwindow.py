# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.default_file = "../images/default.png"
        self.current_file = "../images/utahteapot.jpg"
        pixmap = QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio)
        self.ui.image.setPixmap(pixmap)
#maybe overload QLabel's resizeEvent instead?



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
