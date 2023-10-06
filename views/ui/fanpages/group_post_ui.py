# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_post.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_GroupPost(object):
    def setupUi(self, GroupPost):
        if not GroupPost.objectName():
            GroupPost.setObjectName(u"GroupPost")
        GroupPost.resize(883, 614)
        self.horizontalLayout = QHBoxLayout(GroupPost)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbl_acc = QFrame(GroupPost)
        self.tbl_acc.setObjectName(u"tbl_acc")
        self.tbl_acc.setMaximumSize(QSize(400, 16777215))
        self.tbl_acc.setFrameShape(QFrame.StyledPanel)
        self.tbl_acc.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.tbl_acc)

        self.function = QFrame(GroupPost)
        self.function.setObjectName(u"function")
        self.function.setStyleSheet(u"QFrame {\n"
"border: 1px solid rgba(255,1,1,40);\n"
"border-radius: 7px;\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"}")
        self.function.setFrameShape(QFrame.StyledPanel)
        self.function.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.function)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.function)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.num_posts = QSpinBox(self.function)
        self.num_posts.setObjectName(u"num_posts")

        self.horizontalLayout_3.addWidget(self.num_posts)

        self.label_4 = QLabel(self.function)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cb_group_type = QComboBox(self.function)
        self.cb_group_type.addItem("")
        self.cb_group_type.addItem("")
        self.cb_group_type.addItem("")
        self.cb_group_type.setObjectName(u"cb_group_type")
        self.cb_group_type.setEditable(True)

        self.horizontalLayout_3.addWidget(self.cb_group_type)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.txt_contents = QTextEdit(self.function)
        self.txt_contents.setObjectName(u"txt_contents")
        self.txt_contents.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout.addWidget(self.txt_contents)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ck_image = QCheckBox(self.function)
        self.ck_image.setObjectName(u"ck_image")

        self.horizontalLayout_2.addWidget(self.ck_image)

        self.le_image_path = QLineEdit(self.function)
        self.le_image_path.setObjectName(u"le_image_path")

        self.horizontalLayout_2.addWidget(self.le_image_path)

        self.btn_select_image = QPushButton(self.function)
        self.btn_select_image.setObjectName(u"btn_select_image")

        self.horizontalLayout_2.addWidget(self.btn_select_image)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.ck_status = QCheckBox(self.function)
        self.ck_status.setObjectName(u"ck_status")

        self.verticalLayout.addWidget(self.ck_status)

        self.groupBox = QGroupBox(self.function)
        self.groupBox.setObjectName(u"groupBox")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 220, 49))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.post_start_ms = QSpinBox(self.layoutWidget)
        self.post_start_ms.setObjectName(u"post_start_ms")
        self.post_start_ms.setMinimum(100)
        self.post_start_ms.setMaximum(1000)

        self.gridLayout.addWidget(self.post_start_ms, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.post_stop_ms = QSpinBox(self.layoutWidget)
        self.post_stop_ms.setObjectName(u"post_stop_ms")
        self.post_stop_ms.setMinimum(200)
        self.post_stop_ms.setMaximum(1000)
        self.post_stop_ms.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.post_stop_ms, 0, 3, 1, 1)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(18, 80, 271, 26))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_run = QPushButton(self.layoutWidget1)
        self.btn_run.setObjectName(u"btn_run")

        self.gridLayout_2.addWidget(self.btn_run, 0, 0, 1, 1)

        self.btn_stop = QPushButton(self.layoutWidget1)
        self.btn_stop.setObjectName(u"btn_stop")

        self.gridLayout_2.addWidget(self.btn_stop, 0, 1, 1, 1)

        self.btn_schedule = QPushButton(self.layoutWidget1)
        self.btn_schedule.setObjectName(u"btn_schedule")

        self.gridLayout_2.addWidget(self.btn_schedule, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addWidget(self.function)


        self.retranslateUi(GroupPost)

        QMetaObject.connectSlotsByName(GroupPost)
    # setupUi

    def retranslateUi(self, GroupPost):
        GroupPost.setWindowTitle(QCoreApplication.translate("GroupPost", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("GroupPost", u"S\u1ed1 nh\u00f3m mu\u1ed1n \u0111\u0103ng:", None))
        self.label_4.setText(QCoreApplication.translate("GroupPost", u"Th\u1ec3 lo\u1ea1i", None))
        self.cb_group_type.setItemText(0, QCoreApplication.translate("GroupPost", u"Dep", None))
        self.cb_group_type.setItemText(1, QCoreApplication.translate("GroupPost", u"May", None))
        self.cb_group_type.setItemText(2, QCoreApplication.translate("GroupPost", u"Random", None))

        self.ck_image.setText(QCoreApplication.translate("GroupPost", u"\u0110\u0103ng \u1ea3nh", None))
        self.btn_select_image.setText(QCoreApplication.translate("GroupPost", u"Ch\u1ecdn \u1ea2nh", None))
        self.ck_status.setText(QCoreApplication.translate("GroupPost", u"\u0110\u0103ng status", None))
        self.groupBox.setTitle(QCoreApplication.translate("GroupPost", u"Chrome", None))
        self.label.setText(QCoreApplication.translate("GroupPost", u"Ngh\u1ec9 t\u1eeb", None))
        self.label_2.setText(QCoreApplication.translate("GroupPost", u"\u0111\u1ebfn", None))
        self.btn_run.setText(QCoreApplication.translate("GroupPost", u"Ch\u1ea1y", None))
        self.btn_stop.setText(QCoreApplication.translate("GroupPost", u"D\u1eebng", None))
        self.btn_schedule.setText(QCoreApplication.translate("GroupPost", u"H\u1eb9n l\u1ecbch", None))
    # retranslateUi

