# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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

class Ui_DashBoard(object):
    def setupUi(self, DashBoard):
        if not DashBoard.objectName():
            DashBoard.setObjectName(u"DashBoard")
        DashBoard.resize(586, 398)
        self.verticalLayout = QVBoxLayout(DashBoard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DashBoard)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_reload = QPushButton(self.frame)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.btn_reload)


        self.verticalLayout.addWidget(self.frame)

        self.tb_dashboard = QFrame(DashBoard)
        self.tb_dashboard.setObjectName(u"tb_dashboard")
        self.tb_dashboard.setFrameShape(QFrame.StyledPanel)
        self.tb_dashboard.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.tb_dashboard)


        self.retranslateUi(DashBoard)

        QMetaObject.connectSlotsByName(DashBoard)
    # setupUi

    def retranslateUi(self, DashBoard):
        DashBoard.setWindowTitle(QCoreApplication.translate("DashBoard", u"Form", None))
        self.btn_reload.setText(QCoreApplication.translate("DashBoard", u"Reload", None))
    # retranslateUi

