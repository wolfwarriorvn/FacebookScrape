# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'approve.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)
import icon_rc

class Ui_Approve(object):
    def setupUi(self, Approve):
        if not Approve.objectName():
            Approve.setObjectName(u"Approve")
        Approve.resize(728, 422)
        Approve.setStyleSheet(u"* {\n"
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
"QPushButton#btn_start{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1, y2:3, stop:0 #0081A7, stop:1 #00AFB9);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 150;\n"
"height: 35;\n"
"}\n"
"QPushButton#btn_start:hover{\n"
"background-color: #0081A7\n"
"}\n"
"QPushButton#btn_start:pressed{\n"
"background-color: #00AFB9\n"
"}\n"
"QPushButton#btn_cancel{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: qlineargradient(spr"
                        "ead:pad, x1:0 y1:0, x2:1, y2:3, stop:0 #0011A7, stop:1 #00AFB9);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 150;\n"
"height: 35;\n"
"}\n"
"QPushButton#btn_schedule{\n"
"	 color: rgb(255, 255, 255);\n"
"     background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1, y2:3, stop:0 #FFA500, stop:1 #00AFB9);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 150;\n"
"height: 35;\n"
"}")
        self.verticalLayout = QVBoxLayout(Approve)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Approve)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.num_posts = QSpinBox(Approve)
        self.num_posts.setObjectName(u"num_posts")

        self.horizontalLayout.addWidget(self.num_posts)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Approve)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.groups_settings = QTextEdit(Approve)
        self.groups_settings.setObjectName(u"groups_settings")

        self.verticalLayout.addWidget(self.groups_settings)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_schedule = QPushButton(Approve)
        self.btn_schedule.setObjectName(u"btn_schedule")

        self.horizontalLayout_2.addWidget(self.btn_schedule)

        self.btn_start = QPushButton(Approve)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_2.addWidget(self.btn_start)

        self.btn_cancel = QPushButton(Approve)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Approve)

        QMetaObject.connectSlotsByName(Approve)
    # setupUi

    def retranslateUi(self, Approve):
        Approve.setWindowTitle(QCoreApplication.translate("Approve", u"Duy\u1ec7t b\u00e0i", None))
        self.label.setText(QCoreApplication.translate("Approve", u"S\u1ed1 b\u00e0i:", None))
        self.label_2.setText(QCoreApplication.translate("Approve", u"Danh s\u00e1ch nh\u00f3m: UID | approve | decline", None))
        self.btn_schedule.setText(QCoreApplication.translate("Approve", u"L\u00ean l\u1ecbch", None))
        self.btn_start.setText(QCoreApplication.translate("Approve", u"Ch\u1ea1y ngay", None))
        self.btn_cancel.setText(QCoreApplication.translate("Approve", u"Hu\u1ef7", None))
    # retranslateUi

