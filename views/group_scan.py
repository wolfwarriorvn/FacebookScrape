from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (QApplication, QFrame, QVBoxLayout, QSizePolicy,QPushButton,
    QWidget)

from views.ui.group_scan_ui import Ui_Form
from views.table_custome import TableCustome

class GroupScan(QWidget):
    def __init__(self):
        super(GroupScan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.verticalLayout = QVBoxLayout(self.ui.table_account)
        self.table_accounts = TableCustome()
        self.verticalLayout.addWidget(self.table_accounts)

        self.model = QSqlTableModel(self)
        self.model.setTable('accounts')
        self.model.select()
        self.table_accounts.ui.tableView.setModel(self.model)

        
        