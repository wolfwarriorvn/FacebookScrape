# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Pages(object):
    def setupUi(self, Pages):
        if not Pages.objectName():
            Pages.setObjectName(u"Pages")
        Pages.resize(352, 284)
        Pages.setStyleSheet(u"font-family: Noto Sans SC;\n"
"font-size: 11pt;")
        self.verticalLayout = QVBoxLayout(Pages)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Pages)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_page_name = QLineEdit(self.frame)
        self.le_page_name.setObjectName(u"le_page_name")
        self.le_page_name.setEnabled(True)

        self.horizontalLayout.addWidget(self.le_page_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_page_uid = QLineEdit(self.frame)
        self.le_page_uid.setObjectName(u"le_page_uid")
        self.le_page_uid.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_page_uid)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.cb_list_accounts = QComboBox(self.frame)
        self.cb_list_accounts.setObjectName(u"cb_list_accounts")
        self.cb_list_accounts.setEditable(True)
        self.cb_list_accounts.setMaxVisibleItems(30)

        self.horizontalLayout_4.addWidget(self.cb_list_accounts)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_note = QLineEdit(self.frame)
        self.le_note.setObjectName(u"le_note")
        self.le_note.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.le_note)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Pages)

        self.cb_list_accounts.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Pages)
    # setupUi

    def retranslateUi(self, Pages):
        Pages.setWindowTitle(QCoreApplication.translate("Pages", u"Form", None))
        self.label.setText(QCoreApplication.translate("Pages", u"T\u00ean Page", None))
        self.le_page_name.setText("")
        self.label_2.setText(QCoreApplication.translate("Pages", u"Page ID", None))
        self.label_4.setText(QCoreApplication.translate("Pages", u"Ch\u1ecdn Nick", None))
        self.cb_list_accounts.setCurrentText("")
        self.label_3.setText(QCoreApplication.translate("Pages", u"Ghi ch\u00fa", None))
        self.btn_save.setText(QCoreApplication.translate("Pages", u"L\u01b0u", None))
    # retranslateUi

