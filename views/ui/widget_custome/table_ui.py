# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_widget_table(object):
    def setupUi(self, widget_table):
        if not widget_table.objectName():
            widget_table.setObjectName(u"widget_table")
        widget_table.resize(690, 475)
        self.verticalLayout = QVBoxLayout(widget_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(widget_table)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"font: 10pt \"Segoe UI\";\n"
"background-color: white;\n"
"border: 1px solid rgba(192, 209, 231, 1);\n"
"border-radius: 15px;\n"
"color: black;\n"
"}\n"
"QHeaderView{\n"
"background-color: transparent;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid rgba(192, 209, 231, 1);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: transparent;\n"
"height: 50px;\n"
"}\n"
"QTableView::item {\n"
"	font-size: 11pt;\n"
"    border-bottom: 1px solid rgba(192, 209, 231, 1);\n"
"}\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"    background-color:  #0081A7;\n"
"}\n"
"\n"
"\n"
"")
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(100)
        self.tableView.horizontalHeader().setDefaultSectionSize(100)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(widget_table)

        QMetaObject.connectSlotsByName(widget_table)
    # setupUi

    def retranslateUi(self, widget_table):
        widget_table.setWindowTitle(QCoreApplication.translate("widget_table", u"Form", None))
    # retranslateUi

