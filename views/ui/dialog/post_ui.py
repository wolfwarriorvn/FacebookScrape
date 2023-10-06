# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_Post(object):
    def setupUi(self, Post):
        if not Post.objectName():
            Post.setObjectName(u"Post")
        Post.resize(578, 440)
        self.verticalLayout_3 = QVBoxLayout(Post)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_option = QGroupBox(Post)
        self.group_option.setObjectName(u"group_option")
        self.verticalLayout = QVBoxLayout(self.group_option)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ckb_post_to_groups = QCheckBox(self.group_option)
        self.ckb_post_to_groups.setObjectName(u"ckb_post_to_groups")
        self.ckb_post_to_groups.setEnabled(True)
        self.ckb_post_to_groups.setChecked(True)

        self.horizontalLayout_3.addWidget(self.ckb_post_to_groups)

        self.label_3 = QLabel(self.group_option)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.sp_numposts = QSpinBox(self.group_option)
        self.sp_numposts.setObjectName(u"sp_numposts")
        self.sp_numposts.setSingleStep(2)
        self.sp_numposts.setValue(10)

        self.horizontalLayout_3.addWidget(self.sp_numposts)

        self.label_4 = QLabel(self.group_option)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cb_group_type = QComboBox(self.group_option)
        self.cb_group_type.setObjectName(u"cb_group_type")
        self.cb_group_type.setEditable(True)

        self.horizontalLayout_3.addWidget(self.cb_group_type)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.txt_contents = QTextEdit(self.group_option)
        self.txt_contents.setObjectName(u"txt_contents")
        self.txt_contents.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout.addWidget(self.txt_contents)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb_image_enable = QRadioButton(self.group_option)
        self.rb_image_enable.setObjectName(u"rb_image_enable")

        self.gridLayout_2.addWidget(self.rb_image_enable, 2, 0, 1, 1)

        self.le_image_path = QLineEdit(self.group_option)
        self.le_image_path.setObjectName(u"le_image_path")
        self.le_image_path.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_image_path, 2, 4, 1, 1)

        self.rb_status = QRadioButton(self.group_option)
        self.rb_status.setObjectName(u"rb_status")
        self.rb_status.setChecked(True)

        self.gridLayout_2.addWidget(self.rb_status, 0, 0, 1, 2)

        self.btn_select_image = QPushButton(self.group_option)
        self.btn_select_image.setObjectName(u"btn_select_image")
        self.btn_select_image.setEnabled(False)

        self.gridLayout_2.addWidget(self.btn_select_image, 2, 5, 1, 1)

        self.chb_md5_enable = QCheckBox(self.group_option)
        self.chb_md5_enable.setObjectName(u"chb_md5_enable")
        self.chb_md5_enable.setEnabled(False)

        self.gridLayout_2.addWidget(self.chb_md5_enable, 2, 1, 1, 2)

        self.chb_background_enable = QCheckBox(self.group_option)
        self.chb_background_enable.setObjectName(u"chb_background_enable")

        self.gridLayout_2.addWidget(self.chb_background_enable, 0, 2, 1, 3)

        self.sp_image_count = QSpinBox(self.group_option)
        self.sp_image_count.setObjectName(u"sp_image_count")
        self.sp_image_count.setEnabled(False)
        self.sp_image_count.setMinimumSize(QSize(40, 0))
        self.sp_image_count.setValue(2)

        self.gridLayout_2.addWidget(self.sp_image_count, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.group_option)

        self.group_setting = QGroupBox(Post)
        self.group_setting.setObjectName(u"group_setting")
        self.verticalLayout_2 = QVBoxLayout(self.group_setting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(-1, -1, 300, -1)
        self.label_2 = QLabel(self.group_setting)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.sp_idle_from = QSpinBox(self.group_setting)
        self.sp_idle_from.setObjectName(u"sp_idle_from")
        self.sp_idle_from.setMaximumSize(QSize(100, 16777215))
        self.sp_idle_from.setMaximum(999)
        self.sp_idle_from.setSingleStep(10)
        self.sp_idle_from.setValue(10)

        self.gridLayout.addWidget(self.sp_idle_from, 0, 2, 1, 1)

        self.label_6 = QLabel(self.group_setting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(20, 16777215))

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.sp_idle_to = QSpinBox(self.group_setting)
        self.sp_idle_to.setObjectName(u"sp_idle_to")
        self.sp_idle_to.setMaximumSize(QSize(100, 16777215))
        self.sp_idle_to.setMaximum(999)
        self.sp_idle_to.setSingleStep(10)
        self.sp_idle_to.setValue(60)

        self.gridLayout.addWidget(self.sp_idle_to, 0, 4, 1, 1)

        self.label_7 = QLabel(self.group_setting)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.sp_threads = QSpinBox(self.group_setting)
        self.sp_threads.setObjectName(u"sp_threads")
        self.sp_threads.setMaximumSize(QSize(100, 16777215))
        self.sp_threads.setValue(1)

        self.gridLayout.addWidget(self.sp_threads, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_schedule = QPushButton(self.group_setting)
        self.btn_schedule.setObjectName(u"btn_schedule")
        self.btn_schedule.setStyleSheet(u"    background-color: purple;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_schedule)

        self.btn_runnow = QPushButton(self.group_setting)
        self.btn_runnow.setObjectName(u"btn_runnow")
        self.btn_runnow.setStyleSheet(u"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_runnow)

        self.btn_cancel = QPushButton(self.group_setting)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.group_setting)


        self.retranslateUi(Post)
        self.rb_status.toggled.connect(self.chb_background_enable.setEnabled)
        self.rb_image_enable.toggled.connect(self.chb_md5_enable.setEnabled)
        self.rb_image_enable.toggled.connect(self.le_image_path.setEnabled)
        self.rb_image_enable.toggled.connect(self.btn_select_image.setEnabled)
        self.rb_image_enable.toggled.connect(self.sp_image_count.setEnabled)
        self.btn_cancel.clicked.connect(Post.close)

        QMetaObject.connectSlotsByName(Post)
    # setupUi

    def retranslateUi(self, Post):
        Post.setWindowTitle(QCoreApplication.translate("Post", u"Form", None))
        self.group_option.setTitle(QCoreApplication.translate("Post", u"Tu\u1ef3 ch\u1ecdn", None))
        self.ckb_post_to_groups.setText(QCoreApplication.translate("Post", u"\u0110\u0103ng b\u00e0i v\u00e0o nh\u00f3m", None))
        self.label_3.setText(QCoreApplication.translate("Post", u"S\u1ed1 nh\u00f3m mu\u1ed1n \u0111\u0103ng:", None))
        self.label_4.setText(QCoreApplication.translate("Post", u"Th\u1ec3 lo\u1ea1i", None))
        self.txt_contents.setPlaceholderText(QCoreApplication.translate("Post", u"N\u1ed9i dung theo \u0111\u1ecbnh d\u1ea1ng {a | b c|...}", None))
        self.rb_image_enable.setText(QCoreApplication.translate("Post", u"\u0110\u0103ng \u1ea3nh", None))
        self.rb_status.setText(QCoreApplication.translate("Post", u"\u0110\u0103ng status", None))
        self.btn_select_image.setText(QCoreApplication.translate("Post", u"Ch\u1ecdn \u1ea2nh", None))
        self.chb_md5_enable.setText(QCoreApplication.translate("Post", u"\u0110\u1ed5i MD5 image", None))
        self.chb_background_enable.setText(QCoreApplication.translate("Post", u"D\u00f9ng background", None))
        self.group_setting.setTitle(QCoreApplication.translate("Post", u"C\u1ea5u h\u00ecnh", None))
        self.label_2.setText(QCoreApplication.translate("Post", u"Th\u1eddi gian ngh\u1ec9(s):", None))
        self.label_6.setText(QCoreApplication.translate("Post", u"\u0111\u1ebfn", None))
        self.label_7.setText(QCoreApplication.translate("Post", u"S\u1ed1 lu\u1ed3ng:", None))
        self.btn_schedule.setText(QCoreApplication.translate("Post", u"L\u1eadp l\u1ecbch", None))
        self.btn_runnow.setText(QCoreApplication.translate("Post", u"Ch\u1ea1y ngay", None))
        self.btn_cancel.setText(QCoreApplication.translate("Post", u"Hu\u1ef7", None))
    # retranslateUi

