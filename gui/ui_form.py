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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFormLayout,
    QGridLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 642)
        self.actionOpen_image = QAction(MainWindow)
        self.actionOpen_image.setObjectName(u"actionOpen_image")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.comboColor = QComboBox(self.centralwidget)
        self.comboColor.addItem("")
        self.comboColor.addItem("")
        self.comboColor.setObjectName(u"comboColor")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboColor)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboPad = QComboBox(self.centralwidget)
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.addItem("")
        self.comboPad.setObjectName(u"comboPad")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboPad)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.comboDither = QComboBox(self.centralwidget)
        self.comboDither.addItem("")
        self.comboDither.addItem("")
        self.comboDither.addItem("")
        self.comboDither.setObjectName(u"comboDither")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboDither)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.pushStart = QPushButton(self.centralwidget)
        self.pushStart.setObjectName(u"pushStart")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pushStart)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.spinGenCurrent = QSpinBox(self.centralwidget)
        self.spinGenCurrent.setObjectName(u"spinGenCurrent")
        self.spinGenCurrent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinGenCurrent.setReadOnly(True)
        self.spinGenCurrent.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinGenCurrent)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.formLayout_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.spinGenSelect = QSpinBox(self.centralwidget)
        self.spinGenSelect.setObjectName(u"spinGenSelect")
        self.spinGenSelect.setValue(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinGenSelect)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setScaledContents(False)
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.image, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_image)

        self.retranslateUi(MainWindow)
        self.spinGenSelect.valueChanged.connect(MainWindow.setGenCount)
        self.comboColor.currentTextChanged.connect(MainWindow.setColorMode)
        self.comboPad.currentTextChanged.connect(MainWindow.setPadMode)
        self.comboDither.currentTextChanged.connect(MainWindow.setDitherMode)
        self.pushStart.clicked.connect(MainWindow.startGame)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_image.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.comboColor.setItemText(0, QCoreApplication.translate("MainWindow", u"RGB", None))
        self.comboColor.setItemText(1, QCoreApplication.translate("MainWindow", u"Grayscale", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pad mode:", None))
        self.comboPad.setItemText(0, QCoreApplication.translate("MainWindow", u"Dead", None))
        self.comboPad.setItemText(1, QCoreApplication.translate("MainWindow", u"Live", None))
        self.comboPad.setItemText(2, QCoreApplication.translate("MainWindow", u"Wrap", None))
        self.comboPad.setItemText(3, QCoreApplication.translate("MainWindow", u"Symmetric", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dither", None))
        self.comboDither.setItemText(0, QCoreApplication.translate("MainWindow", u"2x2", None))
        self.comboDither.setItemText(1, QCoreApplication.translate("MainWindow", u"4x4", None))
        self.comboDither.setItemText(2, QCoreApplication.translate("MainWindow", u"8x8", None))

        self.pushStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current generation:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Color mode:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Generations:", None))
        self.image.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

