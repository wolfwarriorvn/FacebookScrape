# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_scan.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(641, 444)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_account = QWidget(Form)
        self.table_account.setObjectName(u"table_account")

        self.horizontalLayout.addWidget(self.table_account)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 140, 75, 24))
        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(80, 190, 89, 20))

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi

