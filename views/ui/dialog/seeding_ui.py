# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seeding.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Seeding(object):
    def setupUi(self, Seeding):
        if not Seeding.objectName():
            Seeding.setObjectName(u"Seeding")
        Seeding.resize(460, 368)
        Seeding.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(Seeding)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Seeding)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ckb_autogetlink = QCheckBox(self.groupBox)
        self.ckb_autogetlink.setObjectName(u"ckb_autogetlink")
        self.ckb_autogetlink.setEnabled(True)
        self.ckb_autogetlink.setChecked(True)

        self.horizontalLayout_5.addWidget(self.ckb_autogetlink)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.spin_seedings = QSpinBox(self.groupBox)
        self.spin_seedings.setObjectName(u"spin_seedings")
        self.spin_seedings.setMaximum(999)
        self.spin_seedings.setValue(10)

        self.horizontalLayout_5.addWidget(self.spin_seedings)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.txt_links = QPlainTextEdit(self.groupBox)
        self.txt_links.setObjectName(u"txt_links")
        self.txt_links.setEnabled(False)

        self.verticalLayout.addWidget(self.txt_links)

        self.ckb_like = QCheckBox(self.groupBox)
        self.ckb_like.setObjectName(u"ckb_like")

        self.verticalLayout.addWidget(self.ckb_like)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ckb_comment = QCheckBox(self.groupBox)
        self.ckb_comment.setObjectName(u"ckb_comment")

        self.horizontalLayout_8.addWidget(self.ckb_comment)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.le_contents = QLineEdit(self.groupBox)
        self.le_contents.setObjectName(u"le_contents")
        self.le_contents.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.le_contents)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Seeding)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.sp_idle_from = QSpinBox(self.groupBox_2)
        self.sp_idle_from.setObjectName(u"sp_idle_from")
        self.sp_idle_from.setMaximumSize(QSize(100, 16777215))
        self.sp_idle_from.setMaximum(99999)
        self.sp_idle_from.setSingleStep(10)
        self.sp_idle_from.setValue(10)

        self.gridLayout.addWidget(self.sp_idle_from, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(20, 16777215))

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.sp_idle_to = QSpinBox(self.groupBox_2)
        self.sp_idle_to.setObjectName(u"sp_idle_to")
        self.sp_idle_to.setMaximumSize(QSize(100, 16777215))
        self.sp_idle_to.setMaximum(99999)
        self.sp_idle_to.setSingleStep(10)
        self.sp_idle_to.setValue(60)

        self.gridLayout.addWidget(self.sp_idle_to, 0, 4, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.sp_threads = QSpinBox(self.groupBox_2)
        self.sp_threads.setObjectName(u"sp_threads")
        self.sp_threads.setMaximumSize(QSize(100, 16777215))
        self.sp_threads.setValue(1)

        self.gridLayout.addWidget(self.sp_threads, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_schedule_2 = QPushButton(self.groupBox_2)
        self.btn_schedule_2.setObjectName(u"btn_schedule_2")
        self.btn_schedule_2.setStyleSheet(u"    background-color: purple;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_schedule_2)

        self.btn_runnow_2 = QPushButton(self.groupBox_2)
        self.btn_runnow_2.setObjectName(u"btn_runnow_2")
        self.btn_runnow_2.setStyleSheet(u"    background-color: green;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_runnow_2)

        self.btn_cancel_2 = QPushButton(self.groupBox_2)
        self.btn_cancel_2.setObjectName(u"btn_cancel_2")
        self.btn_cancel_2.setStyleSheet(u"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    padding: 6px;\n"
"	color: white")

        self.horizontalLayout_4.addWidget(self.btn_cancel_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(Seeding)
        self.ckb_autogetlink.clicked["bool"].connect(self.txt_links.setDisabled)
        self.ckb_comment.clicked["bool"].connect(self.le_contents.setEnabled)
        self.btn_cancel_2.clicked.connect(Seeding.close)
        self.btn_runnow_2.clicked.connect(Seeding.close)

        QMetaObject.connectSlotsByName(Seeding)
    # setupUi

    def retranslateUi(self, Seeding):
        Seeding.setWindowTitle(QCoreApplication.translate("Seeding", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Seeding", u"Seeding", None))
        self.ckb_autogetlink.setText(QCoreApplication.translate("Seeding", u"L\u1ea5y b\u00e0i t\u1eeb post \u0111\u00e3 qu\u00e9t", None))
        self.label_8.setText(QCoreApplication.translate("Seeding", u"S\u1ed1 b\u00e0i mu\u1ed1n seeding:", None))
        self.txt_links.setPlainText("")
        self.txt_links.setPlaceholderText(QCoreApplication.translate("Seeding", u"Nh\u1eadp url b\u00e0i vi\u1ebft. M\u1ed7i d\u00f2ng m\u1ed9t b\u00e0i..", None))
        self.ckb_like.setText(QCoreApplication.translate("Seeding", u"Like b\u00e0i vi\u1ebft", None))
        self.ckb_comment.setText(QCoreApplication.translate("Seeding", u"Comment", None))
        self.label_5.setText(QCoreApplication.translate("Seeding", u"N\u1ed9i dung:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Seeding", u"C\u1ea5u h\u00ecnh", None))
        self.label_2.setText(QCoreApplication.translate("Seeding", u"Th\u1eddi gian ngh\u1ec9(s):", None))
        self.label_6.setText(QCoreApplication.translate("Seeding", u"\u0111\u1ebfn", None))
        self.label_7.setText(QCoreApplication.translate("Seeding", u"S\u1ed1 lu\u1ed3ng:", None))
        self.btn_schedule_2.setText(QCoreApplication.translate("Seeding", u"L\u1eadp l\u1ecbch", None))
        self.btn_runnow_2.setText(QCoreApplication.translate("Seeding", u"Ch\u1ea1y ngay", None))
        self.btn_cancel_2.setText(QCoreApplication.translate("Seeding", u"Hu\u1ef7", None))
    # retranslateUi

