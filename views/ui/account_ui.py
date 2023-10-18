# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(679, 478)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.btn_add_accounts = QPushButton(self.widget)
        self.btn_add_accounts.setObjectName(u"btn_add_accounts")
        self.btn_add_accounts.setMaximumSize(QSize(150, 16777215))
        self.btn_add_accounts.setStyleSheet(u"QPushButton{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1, y2:3, stop:0 #0081A7, stop:1 #00AFB9);;\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	width: 150;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0081A7\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #00AFB9\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/views/icon/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_accounts.setIcon(icon)

        self.gridLayout.addWidget(self.btn_add_accounts, 0, 2, 1, 1)

        self.btn_refresh = QPushButton(self.widget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMaximumSize(QSize(16777215, 16777215))
        self.btn_refresh.setStyleSheet(u"	* {background-color: rgba(192, 209, 231, 1);\n"
"	border: 1px solid rgba(192, 209, 231, 1);\n"
"	border-radius: 7px;\n"
"	color: black;\n"
"	width: 40;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #b8e7ea;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(227, 80, 168, 1)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/views/icon/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon1)
        self.btn_refresh.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_refresh, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(436, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.f_account = QFrame(Form)
        self.f_account.setObjectName(u"f_account")
        self.f_account.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.f_account)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_add_accounts.setText(QCoreApplication.translate("Form", u"Th\u00eam T\u00e0i Kho\u1ea3n ", None))
        self.btn_refresh.setText("")
    # retranslateUi

