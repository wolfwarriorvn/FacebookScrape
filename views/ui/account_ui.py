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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(973, 545)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_refresh = QPushButton(self.widget)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.btn_add_accounts = QPushButton(self.widget)
        self.btn_add_accounts.setObjectName(u"btn_add_accounts")

        self.horizontalLayout.addWidget(self.btn_add_accounts)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.widget)

        self.f_account = QFrame(Form)
        self.f_account.setObjectName(u"f_account")

        self.verticalLayout_3.addWidget(self.f_account)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_refresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.btn_add_accounts.setText(QCoreApplication.translate("Form", u"Add account", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

