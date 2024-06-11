# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFormLayout,
    QGraphicsView, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_Gui(object):
    def setupUi(self, Gui):
        if not Gui.objectName():
            Gui.setObjectName(u"Gui")
        Gui.resize(1012, 713)
        self.label_6 = QLabel(Gui)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 420, 58, 15))
        self.gridLayout = QGridLayout(Gui)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Gui)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.spinGenSelect = QSpinBox(Gui)
        self.spinGenSelect.setObjectName(u"spinGenSelect")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinGenSelect)

        self.label_3 = QLabel(Gui)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.comboDither = QComboBox(Gui)
        self.comboDither.addItem("")
        self.comboDither.addItem("")
        self.comboDither.addItem("")
        self.comboDither.setObjectName(u"comboDither")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboDither)

        self.label_4 = QLabel(Gui)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboColor = QComboBox(Gui)
        self.comboColor.addItem("")
        self.comboColor.addItem("")
        self.comboColor.setObjectName(u"comboColor")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboColor)

        self.label_5 = QLabel(Gui)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.comboPad = QComboBox(Gui)
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.setObjectName(u"comboPad")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboPad)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(Gui)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.spinGenCurrent = QSpinBox(Gui)
        self.spinGenCurrent.setObjectName(u"spinGenCurrent")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinGenCurrent.sizePolicy().hasHeightForWidth())
        self.spinGenCurrent.setSizePolicy(sizePolicy)
        self.spinGenCurrent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinGenCurrent.setReadOnly(True)
        self.spinGenCurrent.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinGenCurrent)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.formLayout_2)

        self.startButton = QPushButton(Gui)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setCheckable(False)
        self.startButton.setFlat(False)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.startButton)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.graphicsView = QGraphicsView(Gui)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)


        self.retranslateUi(Gui)

        QMetaObject.connectSlotsByName(Gui)
    # setupUi

    def retranslateUi(self, Gui):
        Gui.setWindowTitle(QCoreApplication.translate("Gui", u"Gui", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate("Gui", u"Generations:", None))
        self.label_3.setText(QCoreApplication.translate("Gui", u"Dither:", None))
        self.comboDither.setItemText(0, QCoreApplication.translate("Gui", u"2x2", None))
        self.comboDither.setItemText(1, QCoreApplication.translate("Gui", u"4x4", None))
        self.comboDither.setItemText(2, QCoreApplication.translate("Gui", u"8x8", None))

        self.label_4.setText(QCoreApplication.translate("Gui", u"Color space:", None))
        self.comboColor.setItemText(0, QCoreApplication.translate("Gui", u"RGB", None))
        self.comboColor.setItemText(1, QCoreApplication.translate("Gui", u"Grayscale", None))

        self.label_5.setText(QCoreApplication.translate("Gui", u"Pad mode:", None))
        self.comboPad.setItemText(0, QCoreApplication.translate("Gui", u"dead", None))
        self.comboPad.setItemText(1, QCoreApplication.translate("Gui", u"live", None))
        self.comboPad.setItemText(2, QCoreApplication.translate("Gui", u"wrap", None))
        self.comboPad.setItemText(3, QCoreApplication.translate("Gui", u"symmetric", None))

        self.label_7.setText(QCoreApplication.translate("Gui", u"Current generation:", None))
        self.startButton.setText(QCoreApplication.translate("Gui", u"Start", None))
    # retranslateUi

