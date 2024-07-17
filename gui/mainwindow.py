# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QSpinBox

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

def spinChanged(spin: QSpinBox, count: int):
    count = spin.value()
    print(count)

def comboChanged(combo: QComboBox, mode: str):
    mode = combo.currentText()
    print(mode)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    #set default values
    spin_gens = widget.ui.spinGenSelect
    num_gens = spin_gens.value()

    combo_color = widget.ui.comboColor
    color_mode = combo_color.currentText()

    combo_pad = widget.ui.comboPad
    pad_mode = combo_pad.currentText()

    combo_dither = widget.ui.comboDither
    dither_mode = combo_dither.currentText()

    #connect signals with functions that update the variables above
    #this doesn't work. check if it works when moved to mainwindow.py. can;t move to ui_form.py due to it resetting on rebuild
    widget.ui.spinGenSelect.valueChanged.connect(spinChanged(widget.ui.spinGenSelect, num_gens))
    combo_color.currentTextChanged.connect(comboChanged(combo_color, color_mode))
    combo_pad.currentTextChanged.connect(comboChanged(combo_pad, pad_mode))
    combo_dither.currentTextChanged.connect(comboChanged(combo_dither, dither_mode))

    widget.show()
    sys.exit(app.exec())
