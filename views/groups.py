from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu,QVBoxLayout
from views.ui.groups_ui import Ui_Group
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu,QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QSortFilterProxyModel,QRegularExpression
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Signal, Slot, Qt

from views.ui.account_ui import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui
from views.add_accounts import AddAccount
from controllers.controller import Controller
from views.edit_accounts import EditAccount
from views.table_custome import TableCustome
from views.groups_add import GroupAdd
from controllers.request import *

class Groups(QWidget, Ui_Group):
    def __init__(self, controller: Controller):
        super(Groups, self).__init__()
        self._controller = controller

        self.setupUi(self)

        #Load table
        vlayout = QVBoxLayout(self.frame_group)
        self.tb_view = TableCustome()
        vlayout.addWidget(self.tb_view)
        self.model = QSqlTableModel(self)
        self.model.setTable('groups')
        self.model.select()

        self.tb_view.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tb_view.ui.tableView.customContextMenuRequested.connect(self.open_menu)

        self.tb_view.ui.tableView.setModel(self.model)
        self.btn_add_group.clicked.connect(self.add_groups)
        self.btn_refresh.clicked.connect(self.refresh)

    def open_menu(self, position):
        indexes = self.tb_view.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return

        indexes = self.tb_view.ui.tableView.selectionModel().selectedRows()
        self.seleted_id = [self.tb_view.ui.tableView.model().data(i) for i in sorted(indexes)]

        menu = QMenu()
        # menu.setStyleSheet
        menu.setStyleSheet('font: 13px;')
        table_delete_action = QtGui.QAction("Delete: {}".format(len(self.seleted_id)), self)
        
        menu.addAction(table_delete_action)
        table_delete_action.triggered.connect(self.delete_selected_row)

        action = menu.exec_(self.tb_view.ui.tableView.mapToGlobal(position))
    
    def delete_selected_row(self):
        payload = {
            'table': 'groups',
            'column': 'ID',
            'values_list' : self.seleted_id}
        self._controller.database_operation.emit('delete', self.on_delete_response, payload)

    def on_delete_response(self, result, error):
        if error:
            print(f"Error now: {error}")
        else:
            self.refresh()

    def add_groups(self):
        self.group_dialog = GroupAdd(self._controller)
        self.group_dialog.add_completed.connect(self.refresh)
        self.group_dialog.show()
    def refresh(self):
        self.model.setTable('groups')
        self.model.select()