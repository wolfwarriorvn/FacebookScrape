# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'joined_groups.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_JoinedGroup(object):
    def setupUi(self, JoinedGroup):
        if not JoinedGroup.objectName():
            JoinedGroup.setObjectName(u"JoinedGroup")
        JoinedGroup.resize(710, 477)
        JoinedGroup.setMinimumSize(QSize(0, 100))
        self.verticalLayout = QVBoxLayout(JoinedGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(JoinedGroup)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.cb_uids = QComboBox(self.frame)
        self.cb_uids.setObjectName(u"cb_uids")
        self.cb_uids.setMaximumSize(QSize(400, 16777215))
        self.cb_uids.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout.addWidget(self.cb_uids, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.pushButton, 1, 6, 1, 1)

        self.btn_view_group = QPushButton(self.frame)
        self.btn_view_group.setObjectName(u"btn_view_group")
        self.btn_view_group.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btn_view_group, 0, 10, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 8, 1, 1)

        self.btn_scan_by_key = QPushButton(self.frame)
        self.btn_scan_by_key.setObjectName(u"btn_scan_by_key")
        self.btn_scan_by_key.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btn_scan_by_key, 0, 6, 1, 1)

        self.le_key_search_2 = QLineEdit(self.frame)
        self.le_key_search_2.setObjectName(u"le_key_search_2")
        self.le_key_search_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.le_key_search_2, 1, 3, 1, 1)

        self.le_key_search = QLineEdit(self.frame)
        self.le_key_search.setObjectName(u"le_key_search")
        self.le_key_search.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.le_key_search, 0, 3, 1, 1)

        self.btn_view_scan_group = QPushButton(self.frame)
        self.btn_view_scan_group.setObjectName(u"btn_view_scan_group")
        self.btn_view_scan_group.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btn_view_scan_group, 0, 9, 1, 1)

        self.number_of_groups = QSpinBox(self.frame)
        self.number_of_groups.setObjectName(u"number_of_groups")
        self.number_of_groups.setMinimumSize(QSize(50, 0))
        self.number_of_groups.setMinimum(10)
        self.number_of_groups.setMaximum(1000)

        self.gridLayout.addWidget(self.number_of_groups, 0, 5, 1, 1)

        self.btn_scan_joined_group = QPushButton(self.frame)
        self.btn_scan_joined_group.setObjectName(u"btn_scan_joined_group")
        self.btn_scan_joined_group.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.btn_scan_joined_group, 0, 8, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.btn_posts = QPushButton(self.frame)
        self.btn_posts.setObjectName(u"btn_posts")

        self.gridLayout.addWidget(self.btn_posts, 1, 10, 1, 1)

        self.btn_history_posts = QPushButton(self.frame)
        self.btn_history_posts.setObjectName(u"btn_history_posts")

        self.gridLayout.addWidget(self.btn_history_posts, 1, 9, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.tbl_group = QFrame(JoinedGroup)
        self.tbl_group.setObjectName(u"tbl_group")
        self.tbl_group.setFrameShape(QFrame.StyledPanel)
        self.tbl_group.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.tbl_group)


        self.retranslateUi(JoinedGroup)

        QMetaObject.connectSlotsByName(JoinedGroup)
    # setupUi

    def retranslateUi(self, JoinedGroup):
        JoinedGroup.setWindowTitle(QCoreApplication.translate("JoinedGroup", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("JoinedGroup", u"L\u01b0u Type:", None))
        self.cb_uids.setPlaceholderText(QCoreApplication.translate("JoinedGroup", u"Ch\u1ecdn Nick", None))
        self.pushButton.setText(QCoreApplication.translate("JoinedGroup", u"L\u01b0u", None))
        self.btn_view_group.setText(QCoreApplication.translate("JoinedGroup", u"Nh\u00f3m Th\u00eau", None))
        self.label.setText(QCoreApplication.translate("JoinedGroup", u"T\u1eeb kho\u00e1:", None))
        self.pushButton_2.setText(QCoreApplication.translate("JoinedGroup", u"L\u1ecdc nh\u00f3m", None))
        self.btn_scan_by_key.setText(QCoreApplication.translate("JoinedGroup", u"Qu\u00e9t", None))
        self.btn_view_scan_group.setText(QCoreApplication.translate("JoinedGroup", u"Nh\u00f3m \u0110\u00e3 Qu\u00e9t", None))
        self.btn_scan_joined_group.setText(QCoreApplication.translate("JoinedGroup", u"Qu\u00e9t nh\u00f3m tham gia", None))
        self.label_3.setText(QCoreApplication.translate("JoinedGroup", u"S\u1ed1 nh\u00f3m", None))
        self.btn_posts.setText(QCoreApplication.translate("JoinedGroup", u"Posts", None))
        self.btn_history_posts.setText(QCoreApplication.translate("JoinedGroup", u"Qu\u00e9t History", None))
    # retranslateUi

