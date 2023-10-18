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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_Addaccount(object):
    def setupUi(self, Addaccount):
        if not Addaccount.objectName():
            Addaccount.setObjectName(u"Addaccount")
        Addaccount.resize(744, 482)
        Addaccount.setStyleSheet(u"* {\n"
"	font: 11pt \"Segoe UI\";\n"
"}\n"
"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(192, 209, 231, 1);\n"
"	border-radius: 7px;\n"
"	color: black;\n"
"	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"}\n"
"QComboBox {\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(192, 209, 231, 1);\n"
"	border-radius: 7px;\n"
"	color: black;\n"
"	border-bottom-right-radius: 7px; \n"
"	border-bottom-left-radius: 7px; \n"
"}\n"
"QPushButton{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: rgba(74, 38, 171, 1);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(74, 38, 171, 1);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(227, 80, 168, 1)\n"
"}")
        self.verticalLayout = QVBoxLayout(Addaccount)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_accounts = QTextEdit(Addaccount)
        self.txt_accounts.setObjectName(u"txt_accounts")
        self.txt_accounts.setMinimumSize(QSize(0, 300))
        self.txt_accounts.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.txt_accounts)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, -1)
        self.label = QLabel(Addaccount)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.cb_category = QComboBox(Addaccount)
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setEditable(True)

        self.horizontalLayout.addWidget(self.cb_category)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.label_2 = QLabel(Addaccount)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cb_acc_format = QComboBox(Addaccount)
        self.cb_acc_format.setObjectName(u"cb_acc_format")
        self.cb_acc_format.setEditable(False)
        self.cb_acc_format.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.cb_acc_format)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(17, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lb_show_msg = QLabel(Addaccount)
        self.lb_show_msg.setObjectName(u"lb_show_msg")

        self.verticalLayout.addWidget(self.lb_show_msg)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(Addaccount)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 0))
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_save.setFont(font)
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setAutoFillBackground(False)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1, y2:3, stop:0 #0081A7, stop:1 #00AFB9);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 150;\n"
"height: 35;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0081A7\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #00AFB9\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/views/icon/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Addaccount)

        QMetaObject.connectSlotsByName(Addaccount)
    # setupUi

    def retranslateUi(self, Addaccount):
        Addaccount.setWindowTitle(QCoreApplication.translate("Addaccount", u"TH\u00caM T\u00c0I KHO\u1ea2N", None))
        self.txt_accounts.setHtml(QCoreApplication.translate("Addaccount", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100091593173069|ChiLinhen4|2IIJUI3GEJUJA24ZULR3NVOIRMSAMQKT|astoncilekt@outlook.com.br|qKk7dK14|c_user=100091593173069;xs=7:_a4pyg6FCRHu0Q:2:1695027669:-1:7761;fr=0wW7OWdM16BKq7vJu.AWVBY_ZdOvDkWcXj9YYomHk93mM.BlCBHU.ps.AAA.0.0.BlCBHU.AWW818G8MRc;datr=yBEIZYG5WYRdT2I-yvHiXEH0;|EAAAAUaZA8jlABOZCZBjKUVEvG4Wm4SBok1OJUlalnSp2hcUORtFW4ZBj8szzCWBy5jyK9fPwtltMEoaEWiStUFNQTCGG9FHdUemtlFNHcSr4Jv62ml5B0pZCPZBK6"
                        "iWRhpHxwhe9Bu8pFQ6cgMV9MZCzr4F3irgQ6Y0M4EAZAbXwBZA3KGtuDkVZCknmwH4PeZAuSuz|08/13/1979|</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Addaccount", u"Ph\u00e2n lo\u1ea1i t\u00e0i kho\u1ea3n:", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Addaccount", u"New", None))

        self.label_2.setText(QCoreApplication.translate("Addaccount", u"\u0110\u1ecbnh d\u1ea1ng:", None))
        self.lb_show_msg.setText("")
        self.btn_save.setText(QCoreApplication.translate("Addaccount", u"Th\u00eam", None))
    # retranslateUi

