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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_DashBoard(object):
    def setupUi(self, DashBoard):
        if not DashBoard.objectName():
            DashBoard.setObjectName(u"DashBoard")
        DashBoard.resize(562, 399)
        self.verticalLayout = QVBoxLayout(DashBoard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(DashBoard)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(436, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

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
        icon = QIcon()
        icon.addFile(u":/icon/views/icon/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon)
        self.btn_refresh.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_refresh, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

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
        self.btn_refresh.setText("")
    # retranslateUi

