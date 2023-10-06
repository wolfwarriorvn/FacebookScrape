# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_scan_posted_history.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
import icon_rc

class Ui_DialogScanPost(object):
    def setupUi(self, DialogScanPost):
        if not DialogScanPost.objectName():
            DialogScanPost.setObjectName(u"DialogScanPost")
        DialogScanPost.resize(338, 209)
        icon = QIcon()
        icon.addFile(u":/icon/views/icon/search-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        DialogScanPost.setWindowIcon(icon)
        DialogScanPost.setStyleSheet(u"border: 1px solid rgba(255,1,1,40);\n"
"border-radius: 7px;\n"
"font: 14px;\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; ")
        self.verticalLayout = QVBoxLayout(DialogScanPost)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(DialogScanPost)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.scrolls = QSpinBox(DialogScanPost)
        self.scrolls.setObjectName(u"scrolls")
        self.scrolls.setMinimum(1)
        self.scrolls.setMaximum(999)
        self.scrolls.setValue(1)

        self.horizontalLayout_2.addWidget(self.scrolls)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sync_nicks = QLabel(DialogScanPost)
        self.sync_nicks.setObjectName(u"sync_nicks")

        self.horizontalLayout_3.addWidget(self.sync_nicks)

        self.syncs = QSpinBox(DialogScanPost)
        self.syncs.setObjectName(u"syncs")
        self.syncs.setMinimum(1)
        self.syncs.setValue(1)

        self.horizontalLayout_3.addWidget(self.syncs)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_schedule = QPushButton(DialogScanPost)
        self.btn_schedule.setObjectName(u"btn_schedule")
        self.btn_schedule.setStyleSheet(u"    background-color: purple;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout.addWidget(self.btn_schedule)

        self.btn_runnow = QPushButton(DialogScanPost)
        self.btn_runnow.setObjectName(u"btn_runnow")
        self.btn_runnow.setStyleSheet(u"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout.addWidget(self.btn_runnow)

        self.btn_cancel = QPushButton(DialogScanPost)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogScanPost)

        QMetaObject.connectSlotsByName(DialogScanPost)
    # setupUi

    def retranslateUi(self, DialogScanPost):
        DialogScanPost.setWindowTitle(QCoreApplication.translate("DialogScanPost", u"Scan Posted History", None))
        self.label.setText(QCoreApplication.translate("DialogScanPost", u"S\u1ed1 l\u1ea7n cu\u1ed9n trang", None))
        self.sync_nicks.setText(QCoreApplication.translate("DialogScanPost", u"S\u1ed1 nick ch\u1ea1y \u0111\u1ed3ng th\u1eddi", None))
        self.btn_schedule.setText(QCoreApplication.translate("DialogScanPost", u"L\u1eadp l\u1ecbch", None))
        self.btn_runnow.setText(QCoreApplication.translate("DialogScanPost", u"Ch\u1ea1y ngay", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogScanPost", u"Hu\u1ef7", None))
    # retranslateUi

