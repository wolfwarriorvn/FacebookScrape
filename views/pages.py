from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu,QVBoxLayout
from views.ui.pages_ui import Ui_Page
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu,QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QSortFilterProxyModel,QRegularExpression
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Signal, Slot, Qt

from views.ui.account_ui import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui
from views.pages_add import PageAdd
from controllers.controller import Controller
from views.edit_accounts import EditAccount
from views.table_custome import TableCustome

class Pages(QWidget, Ui_Page):
    def __init__(self, controller: Controller):
        super(Pages, self).__init__()
        self._controller = controller

        self.setupUi(self)

        #Load table
        vlayout = QVBoxLayout(self.frame_page)
        self.tb_view = TableCustome()
        vlayout.addWidget(self.tb_view)
        self.model = QSqlTableModel(self)
        self.model.setTable('groups')
        self.model.select()

        self.tb_view.ui.tableView.setModel(self.model)

        self.btn_add_page.clicked.connect(self.on_add_page)

    def on_add_page(self):
        self.group_dialog = PageAdd(self._controller)
        self.group_dialog.show()