# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_edit_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(352, 284)
        Form.setStyleSheet(u"font-family: Noto Sans SC;\n"
"font-size: 11pt;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
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

        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setEnabled(True)

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_uid = QLineEdit(self.frame)
        self.le_uid.setObjectName(u"le_uid")
        self.le_uid.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_uid)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_pass = QLineEdit(self.frame)
        self.le_pass.setObjectName(u"le_pass")

        self.horizontalLayout_3.addWidget(self.le_pass)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.le_proxy = QLineEdit(self.frame)
        self.le_proxy.setObjectName(u"le_proxy")

        self.horizontalLayout_5.addWidget(self.le_proxy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setEditable(True)
        self.cb_category.setMaxVisibleItems(30)

        self.horizontalLayout_4.addWidget(self.cb_category)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

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


        self.retranslateUi(Form)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"T\u00ean t\u00e0i kho\u1ea3n", None))
        self.le_name.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"M\u1eadt kh\u1ea9u", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Proxy", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Th\u1ec3 lo\u1ea1i", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Form", u"DEP", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Form", u"MAY", None))

        self.cb_category.setCurrentText("")
        self.btn_save.setText(QCoreApplication.translate("Form", u"L\u01b0u", None))
    # retranslateUi

