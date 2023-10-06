# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanpages_post.ui'
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

class Ui_FanpagePost(object):
    def setupUi(self, FanpagePost):
        if not FanpagePost.objectName():
            FanpagePost.setObjectName(u"FanpagePost")
        FanpagePost.resize(630, 473)
        self.horizontalLayout = QHBoxLayout(FanpagePost)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fr_function = QWidget(FanpagePost)
        self.fr_function.setObjectName(u"fr_function")
        self.fr_function.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.fr_function)

        self.fr_acc = QFrame(FanpagePost)
        self.fr_acc.setObjectName(u"fr_acc")
        self.fr_acc.setFrameShape(QFrame.StyledPanel)
        self.fr_acc.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fr_acc)


        self.retranslateUi(FanpagePost)

        QMetaObject.connectSlotsByName(FanpagePost)
    # setupUi

    def retranslateUi(self, FanpagePost):
        FanpagePost.setWindowTitle(QCoreApplication.translate("FanpagePost", u"Form", None))
    # retranslateUi

