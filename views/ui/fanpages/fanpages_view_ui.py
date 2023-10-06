# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanpages_view.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QWidget)

class Ui_FanpageView(object):
    def setupUi(self, FanpageView):
        if not FanpageView.objectName():
            FanpageView.setObjectName(u"FanpageView")
        FanpageView.resize(684, 526)
        self.horizontalLayout = QHBoxLayout(FanpageView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbl_acc = QFrame(FanpageView)
        self.tbl_acc.setObjectName(u"tbl_acc")
        self.tbl_acc.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout.addWidget(self.tbl_acc)

        self.tbl_group = QFrame(FanpageView)
        self.tbl_group.setObjectName(u"tbl_group")
        self.tbl_group.setFrameShape(QFrame.StyledPanel)
        self.tbl_group.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.tbl_group)


        self.retranslateUi(FanpageView)

        QMetaObject.connectSlotsByName(FanpageView)
    # setupUi

    def retranslateUi(self, FanpageView):
        FanpageView.setWindowTitle(QCoreApplication.translate("FanpageView", u"Form", None))
    # retranslateUi

