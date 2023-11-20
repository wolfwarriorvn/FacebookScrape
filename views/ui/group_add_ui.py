# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_add.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_GroupAdd(object):
    def setupUi(self, GroupAdd):
        if not GroupAdd.objectName():
            GroupAdd.setObjectName(u"GroupAdd")
        GroupAdd.resize(659, 457)
        GroupAdd.setStyleSheet(u"* {\n"
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
"QLineEdit {\n"
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
"QPushButton:pres"
                        "sed{\n"
"background-color:rgba(227, 80, 168, 1)\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(GroupAdd)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GroupAdd)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))
        self.label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.uid = QLineEdit(GroupAdd)
        self.uid.setObjectName(u"uid")

        self.horizontalLayout.addWidget(self.uid)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(GroupAdd)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.group_name = QLineEdit(GroupAdd)
        self.group_name.setObjectName(u"group_name")

        self.horizontalLayout_2.addWidget(self.group_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(GroupAdd)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.label_3)

        self.approve = QTextEdit(GroupAdd)
        self.approve.setObjectName(u"approve")

        self.verticalLayout.addWidget(self.approve)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(GroupAdd)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_2.addWidget(self.label_4)

        self.decline = QTextEdit(GroupAdd)
        self.decline.setObjectName(u"decline")

        self.verticalLayout_2.addWidget(self.decline)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(14, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lb_show_msg = QLabel(GroupAdd)
        self.lb_show_msg.setObjectName(u"lb_show_msg")

        self.verticalLayout_3.addWidget(self.lb_show_msg)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(GroupAdd)
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
        icon.addFile(u":/new/views/icon/new/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(GroupAdd)

        QMetaObject.connectSlotsByName(GroupAdd)
    # setupUi

    def retranslateUi(self, GroupAdd):
        GroupAdd.setWindowTitle(QCoreApplication.translate("GroupAdd", u"TH\u00caM T\u00c0I KHO\u1ea2N", None))
        self.label.setText(QCoreApplication.translate("GroupAdd", u"UID:", None))
        self.label_2.setText(QCoreApplication.translate("GroupAdd", u"T\u00ean Nh\u00f3m", None))
        self.label_3.setText(QCoreApplication.translate("GroupAdd", u"Approve Keywork:", None))
        self.label_4.setText(QCoreApplication.translate("GroupAdd", u"Decline Keyword:", None))
        self.lb_show_msg.setText("")
        self.btn_save.setText(QCoreApplication.translate("GroupAdd", u"Th\u00eam", None))
    # retranslateUi

