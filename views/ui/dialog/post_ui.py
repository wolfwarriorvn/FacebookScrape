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
        self.sp_numposts.setMaximum(999)
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

        self.le_free_groups = QLabel(self.group_option)
        self.le_free_groups.setObjectName(u"le_free_groups")

        self.horizontalLayout_3.addWidget(self.le_free_groups)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.txt_contents = QTextEdit(self.group_option)
        self.txt_contents.setObjectName(u"txt_contents")
        self.txt_contents.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout.addWidget(self.txt_contents)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb_image_enable = QRadioButton(self.group_option)
        self.rb_image_enable.setObjectName(u"rb_image_enable")
        self.rb_image_enable.setChecked(False)

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
        self.chb_md5_enable.setChecked(True)

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
        self.sp_idle_from.setMaximum(99999)
        self.sp_idle_from.setSingleStep(10)
        self.sp_idle_from.setValue(100)

        self.gridLayout.addWidget(self.sp_idle_from, 0, 2, 1, 1)

        self.label_6 = QLabel(self.group_setting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(20, 16777215))

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.sp_idle_to = QSpinBox(self.group_setting)
        self.sp_idle_to.setObjectName(u"sp_idle_to")
        self.sp_idle_to.setMaximumSize(QSize(100, 16777215))
        self.sp_idle_to.setMaximum(99999)
        self.sp_idle_to.setSingleStep(10)
        self.sp_idle_to.setValue(200)

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
        self.le_free_groups.setText(QCoreApplication.translate("Post", u"R\u00e3nh: ", None))
        self.txt_contents.setHtml(QCoreApplication.translate("Post", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X\u01b0\u1edfng Th\u00eau Vi T\u00ednh Tita chuy\u00ean c\u00e1c m\u1eb7c h\u00e0ng qu\u1ea7n \u00e1o, gi\u00e0y d\u00e9p, balo, t\u00fai x\u00e1ch t\u1eeb h\u00e0ng ch\u1ee3 \u0111\u1ebfn h\u00e0ng shop, xu\u1ea5t kh\u1ea9u. Anh ch\u1ecb c\u00f3 nhu c\u1ea7u th\u00eau h\u00e0ng nhanh ch\u00f3ng, \u0111\u1eb9p, h\u1ee3p t\u00fai ti\u1ec1n th\u00ec li\u00ean h\u1ec7 x\u01b0\u1edfng b\u00ean em nh\u00e9"
                        " ! Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn th\u00eau QU\u1ea6N \u00c1O, GI\u00c0Y D\u00c9P, BALO, T\u00daI X\u00c1CH..., c\u00f3 kinh nghi\u1ec7m l\u00e2u n\u0103m trong ngh\u1ec1, th\u00eau h\u00e0ng nhanh ch\u00f3ng l\u1ea5y h\u00e0ng 1-2 ng\u00e0y, gi\u00e1 c\u1ea3 ph\u1ea3i ch\u0103ng. LH S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn th\u00eau vi t\u00ednh, m\u1eabu m\u00e3 ch\u1ea5t l\u01b0\u1ee3ng, u\u00fd t\u00edn. Lh em S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA nh\u1eadn th\u00eau vi t\u00ednh c\u00e1c lo\u1ea1i m\u1eb7t h\u00e0ng, t\u1eeb qu\u1ea7n \u00e1o \u0111\u1ebfn gi\u00e0y d\u00e9p. Kinh nghi\u1ec7m l\u00e2u n\u0103m - l\u00e0m \u0103n chuy\u1ec7n nghi\u1ec7p - gi\u00e1 h\u1ee3p l\u00fd. LH ngay S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA c\u1ea7n t\u00ecm ngu\u1ed3n th\u00eau s\u1ed1 l\u01b0\u1ee3ng l\u1edbn, h\u00e0"
                        "ng quanh n\u0103m. \u0110\u1ea3m b\u1ea3o th\u00eau h\u00e0ng bao ch\u1ea5t l\u01b0\u1ee3ng, uy t\u00edn, l\u00e0m vi\u1ec7c nhanh ch\u00f3ng. LH S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng th\u00eau vi t\u00ednh TITA chuy\u00ean nh\u1eadn th\u00eau t\u1eeb h\u00e0ng ch\u1ee3 \u0111\u1ebfn h\u00e0ng shop, xu\u1ea5t kh\u1ea9u, l\u00e0m vi\u1ec7c nhanh, th\u00eau h\u00e0ng ch\u1ea5t l\u01b0\u1ee3ng, \u0111\u00fang ti\u1ebfn \u0111\u1ed9. LH ngay SDT/ZALO 0354.777.297 |X\u01b0\u1edfng th\u00eau vi t\u00ednh TITA chuy\u00ean nh\u1eadn th\u00eau vi t\u00ednh c\u00e1c m\u1eb7t h\u00e0ng th\u1eddi trang t\u1eeb h\u00e0ng ch\u1ee3 \u0111\u1ebfn h\u00e0ng shop, xu\u1ea5t kh\u1ea9u. Th\u00eau h\u00e0ng nhanh ch\u00f3ng, \u0111\u1eb9p, h\u1ee3p t\u00fai ti\u1ec1n. LH ngay S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng Th\u00eau Vi T\u00ednh Tita chuy\u00ean c\u00e1c m\u1eb7c h\u00e0ng qu\u1ea7n \u00e1o, gi\u00e0y d\u00e9p, balo, t\u00fai x\u00e1ch t\u1eeb h\u00e0ng ch\u1ee3 \u0111\u1ebfn h\u00e0ng shop, xu\u1ea5t kh\u1ea9"
                        "u. Anh ch\u1ecb c\u00f3 nhu c\u1ea7u th\u00eau h\u00e0ng nhanh ch\u00f3ng, \u0111\u1eb9p, h\u1ee3p t\u00fai ti\u1ec1n th\u00ec li\u00ean h\u1ec7 x\u01b0\u1edfng b\u00ean em nh\u00e9 ! Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng th\u00eau vi t\u00ednh TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh c\u00e1c lo\u1ea1i m\u1eb7t h\u00e0ng, t\u1eeb qu\u1ea7n \u00e1o \u0111\u1ebfn gi\u00e0y d\u00e9p. Kinh nghi\u1ec7m l\u00e2u n\u0103m - l\u00e0m \u0103n chuy\u1ec7n nghi\u1ec7p - gi\u00e1 h\u1ee3p l\u00fd. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH \u1edf qu\u1eadn 12, l\u00e0m vi\u1ec7c t\u1eadn t\u00e2m, uy t\u00edn. Em c\u1ea7n t\u00ecm t\u00ecm ngu\u1ed3n h\u00e0ng gia c\u00f4ng h\u1ee3p t\u00e1c l\u00e2u d\u00e0i. S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng th\u00eau vi t\u00ednh TITA chuy\u00ean nh\u1eadn th\u00eau t\u1ea5t c\u1ea3 m\u1eb7c h\u00e0ng th\u1eddi trang. Ai c\u1ea7n TH\u00caU VI T\u00cdNH l\u1ea5y h\u00e0ng trong ng\u00e0y, gi\u00e1 m"
                        "\u1ec1m th\u00ec h\u00e3y t\u00ecm \u0111\u1ebfn em. L\u00e0m \u0103n v\u1edbi em th\u00ec ch\u1ec9 c\u00f3 y\u00ean t\u00e2m LH ngay 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA v\u1edbi kinh nghi\u1ec7m l\u00e2u n\u0103m, t\u01b0 v\u1ea5n nhi\u1ec7t t\u00ecnh, gi\u00e1 m\u1ec1m. C\u1ea7n th\u00eau li\u00ean h\u1ec7 em ST\u0110/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn th\u00eau c\u00e1c m\u1eb7t h\u00e0ng qu\u1ea7n \u00e1o, balo, t\u00fai x\u00e1ch. M\u1eabu m\u00e3 \u0111\u1eb9p, ch\u1ea5t l\u01b0\u1ee3ng, uy t\u00edn. C\u1ea7n th\u00eau li\u00ean h\u1ec7 ST\u0110/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn th\u00eau vi t\u00ednh theo y\u00eau c\u1ea7u, gi\u00e1 m\u1ec1m, \u0111\u1ea3m b\u1ea3o ch\u1ea5t l\u01b0\u1ee3ng. C\u1ea7n th\u00eau li\u00ean h\u1ec7 ST\u0110/ZALO:0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau c\u00e1c lo\u1ea1i h\u00e0ng th\u1eddi trang, xu\u1ea5t kh\u1ea9"
                        "u, ba l\u00f4, t\u00fai x\u00e1ch, m\u0169 n\u00f3n\u2026 tr\u00ean c\u00e1c lo\u1ea1i ch\u1ea5t li\u1ec7u nh\u01b0 v\u1ea3i, simili, da\u2026Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn th\u00eau \u0111\u1ea3m b\u1ea3o y\u00eau c\u1ea7u v\u1ec1 ch\u1ea5t l\u01b0\u1ee3ng. Gi\u00e1 c\u1ea3 h\u1ee3p l\u00fd. Nh\u1eadn thi\u1ebft k\u1ebf m\u1eabu th\u00eau vi t\u00ednh. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau vi t\u00ednh t\u1ea5t c\u1ea3 c\u00e1c m\u1eb7t h\u00e0ng gi\u00e0y d\u00e9p, qu\u1ea7n \u00e1o, logo c\u00e1c lo\u1ea1i GI\u00c1 C\u1ea0NH TRANH . Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh - Th\u00eau Logo - Thi\u00eau Nh\u00e3n - Th\u00eau theo y\u00eau c\u1ea7u - Thi\u1ebft k\u1ebf logo. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TI"
                        "TA chuy\u00ean th\u00eau \u0111\u1ed3ng ph\u1ee5c c\u00f4ng ty, t\u1eeb m\u1eabu c\u01a1 b\u1ea3n \u0111\u1ebfn n\u00e2ng cao. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh, gi\u00e1 c\u1ea3 h\u1ee3p l\u00fd, \u0111\u00fang ti\u1ebfn \u0111\u1ed9, giao h\u00e0ng \u0111\u00fang h\u1eb9n. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh. \u0110\u1ea3m b\u1ea3o h\u00e0ng th\u00eau ch\u1ea5t l\u01b0\u1ee3ng, \u0111\u01b0\u1eddng kim m\u0169i ch\u1ec9 m\u1ec1m m\u1ea1i, logo khi th\u00eau l\u00ean kh\u00f4ng b\u1ecb r\u00fat ch\u1ec9, nh\u0103n v\u1ea3i. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau \u0111\u1ed3ng ph\u1ee5c c\u00f4ng ty, t\u1eeb m\u1eabu c\u01a1 b\u1ea3n \u0111\u1ebfn n\u00e2ng cao. Gi\u00e1 c\u1ea3 h\u1ee3p l\u00fd, \u0111\u00fang ti\u1ebfn \u0111\u1ed9, gia"
                        "o h\u00e0ng \u0111\u00fang h\u1eb9n. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau \u0111\u1ed3ng ph\u1ee5c c\u00f4ng ty. \u0110\u1ea3m b\u1ea3o h\u00e0ng th\u00eau ch\u1ea5t l\u01b0\u1ee3ng, \u0111\u01b0\u1eddng kim m\u0169i ch\u1ec9 m\u1ec1m m\u1ea1i, logo khi th\u00eau l\u00ean kh\u00f4ng b\u1ecb r\u00fat ch\u1ec9, nh\u0103n v\u1ea3i. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh t\u1eeb h\u00e0ng ch\u1ee3 \u0111\u1ebfn h\u00e0ng shop, xu\u1ea5t kh\u1ea9u, l\u00e0m vi\u1ec7c nhanh, th\u00eau h\u00e0ng ch\u1ea5t l\u01b0\u1ee3ng, \u0111\u00fang ti\u1ebfn \u0111\u1ed9, gi\u00e1 c\u1ea3 h\u1ee3p l\u00fd. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau \u0111\u1ed3ng ph\u1ee5c c\u00f4ng ty. Anh ch\u1ecb c\u00f3 nhu c\u1ea7u th\u00eau h\u00e0ng nhanh ch\u00f3ng, \u0111\u1eb9p, h\u1ee3p t\u00fai "
                        "ti\u1ec1n th\u00ec li\u00ean h\u1ec7 x\u01b0\u1edfng b\u00ean em nh\u00e9. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean nh\u1eadn Th\u00eau Vi T\u00ednh. Kinh nghi\u1ec7m l\u00e2u n\u0103m - l\u00e0m \u0103n chuy\u1ec7n nghi\u1ec7p - gi\u00e1 h\u1ee3p l\u00fd. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA Chuy\u00ean TH\u00caU VI T\u00cdNH tr\u00ean gi\u00e0y d\u00e9p, balo, t\u00fai x\u00e1ch, qu\u1ea7n \u00e1o, kh\u1ea9u trang. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 \u0111\u1ec3 \u0111\u01b0\u1ee3c nh\u1eefng m\u1eabu m\u00e3 \u0111\u1eb9p, ch\u1ea5t l\u01b0\u1ee3ng. |X\u01b0\u1edfng TH\u00caU VI T\u00cdNH TITA chuy\u00ean th\u00eau gi\u00e0y d\u00e9p, balo, t\u00fai x\u00e1ch, qu\u1ea7n \u00e1o, kh\u1ea9u trang. Li\u00ean h\u1ec7 S\u0110T/ZALO: 0354.777.297 \u0111\u1ec3 \u0111\u01b0\u1ee3c nh\u1eefng m\u1eabu m\u00e3 \u0111\u1eb9p, ch\u1ea5t l\u01b0\u1ee3ng</p></body></html>", None))
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

