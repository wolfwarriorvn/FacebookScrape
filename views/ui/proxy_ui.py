# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proxy.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QTableView,
    QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(614, 520)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.le_proxy = QLineEdit(self.splitter)
        self.le_proxy.setObjectName(u"le_proxy")
        self.splitter.addWidget(self.le_proxy)
        self.btn_add = QPushButton(self.splitter)
        self.btn_add.setObjectName(u"btn_add")
        self.splitter.addWidget(self.btn_add)

        self.verticalLayout.addWidget(self.splitter)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

