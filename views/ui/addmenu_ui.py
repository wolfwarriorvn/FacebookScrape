# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addmenu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_Addaccount(object):
    def setupUi(self, Addaccount):
        if not Addaccount.objectName():
            Addaccount.setObjectName(u"Addaccount")
        Addaccount.resize(544, 364)
        self.verticalLayout = QVBoxLayout(Addaccount)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Addaccount)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.txt_accounts = QTextEdit(Addaccount)
        self.txt_accounts.setObjectName(u"txt_accounts")

        self.verticalLayout.addWidget(self.txt_accounts)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lb_show_msg = QLabel(Addaccount)
        self.lb_show_msg.setObjectName(u"lb_show_msg")

        self.verticalLayout.addWidget(self.lb_show_msg)

        self.btn_save = QPushButton(Addaccount)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(50, 0))
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setAutoFillBackground(False)
        self.btn_save.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/views/icon/arrow-31-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(Addaccount)

        QMetaObject.connectSlotsByName(Addaccount)
    # setupUi

    def retranslateUi(self, Addaccount):
        Addaccount.setWindowTitle(QCoreApplication.translate("Addaccount", u"Form", None))
        self.label.setText(QCoreApplication.translate("Addaccount", u"\u0110\u1ecbnh d\u1ea1ng: user|pass|2fa|email|pass", None))
        self.lb_show_msg.setText("")
        self.btn_save.setText(QCoreApplication.translate("Addaccount", u"Save", None))
    # retranslateUi

