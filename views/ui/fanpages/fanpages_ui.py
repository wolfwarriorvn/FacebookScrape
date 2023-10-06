# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanpages.ui'
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

class Ui_FanPages(object):
    def setupUi(self, FanPages):
        if not FanPages.objectName():
            FanPages.setObjectName(u"FanPages")
        FanPages.resize(638, 421)
        self.verticalLayout = QVBoxLayout(FanPages)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(FanPages)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_addpages = QPushButton(self.frame)
        self.btn_addpages.setObjectName(u"btn_addpages")

        self.horizontalLayout.addWidget(self.btn_addpages)


        self.verticalLayout.addWidget(self.frame)

        self.tbl_pages = QFrame(FanPages)
        self.tbl_pages.setObjectName(u"tbl_pages")
        self.tbl_pages.setFrameShape(QFrame.StyledPanel)
        self.tbl_pages.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.tbl_pages)


        self.retranslateUi(FanPages)

        QMetaObject.connectSlotsByName(FanPages)
    # setupUi

    def retranslateUi(self, FanPages):
        FanPages.setWindowTitle(QCoreApplication.translate("FanPages", u"Form", None))
        self.btn_addpages.setText(QCoreApplication.translate("FanPages", u"Add Fanpages", None))
    # retranslateUi

