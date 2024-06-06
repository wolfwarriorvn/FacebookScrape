from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QMenu,QVBoxLayout

from PySide6.QtWidgets import QWidget, QMenu,QVBoxLayout, QAbstractItemView
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Signal, Slot, Qt

from views.ui.approve_request_ui import Ui_ApproveRequest
from controllers.controller import Controller
from views.table_custome import TableCustome
from model.request import DeleteRequest
from model.db_model import Op

class AproveRequest(QWidget, Ui_ApproveRequest):
    def __init__(self, controller: Controller):
        super(AproveRequest, self).__init__()
        self._controller = controller

        self.setupUi(self)
        self.table_name = 'approve_request'

        #Load table
        vlayout = QVBoxLayout(self.frame_group)
        self.tb_view = TableCustome()
        vlayout.addWidget(self.tb_view)
        self.model = QSqlTableModel(self)
        self.model.setTable(self.table_name)
        self.model.select()

        self.tb_view.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tb_view.ui.tableView.customContextMenuRequested.connect(self.open_menu)

        self.tb_view.ui.tableView.setModel(self.model)
        self.btn_refresh.clicked.connect(self.refresh)
        self.refresh()

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
        request = DeleteRequest(
            table=self.table_name,
            column='ID',
            values_list=self.seleted_id
        )
        self._controller.database_operation.emit(Op.DELETE, self.on_delete_response, request)

    
    def on_delete_response(self, result, error):
        if error:
            print(f"Error now: {error}")
        else:
            self.refresh()

    def refresh(self):
        self.model.setTable(self.table_name)
        self.model.select()
        self.tb_view.ui.tableView.setWordWrap(True)
        # self.tb_view.ui.tableView.resizeColumnsToContents()
        self.tb_view.ui.tableView.resizeRowsToContents()

        self.tb_view.ui.tableView.setColumnWidth(1,120)
        self.tb_view.ui.tableView.setColumnWidth(2,120)