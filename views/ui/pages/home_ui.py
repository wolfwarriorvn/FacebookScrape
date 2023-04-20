# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(973, 545)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

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

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.widget_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: transparent;\n"
"border: 1px solid rgba(255,1,1,40);\n"
"border-radius: 7px;\n"
"color: black;\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"}\n"
"QHeaderView{\n"
"background-color: transparent;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid rgba(255,1,1,40);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: transparent;\n"
"height: 50px;\n"
"}\n"
"QTableView::item {\n"
"	font-size: 11pt;\n"
"    border-bottom: 1px solid rgba(255,1,1,40);\n"
"}\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"    background-color: rgba(255, 1, 1, 50);\n"
"}\n"
"\n"
"\n"
"")
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.btn_add_accounts.setText(QCoreApplication.translate("Form", u"Add account", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

