from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Signal, Slot

from views.ui.account_ui import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui
from views.add_accounts import AddAccount
from controllers.main_ctrl import MainController
from views.edit_accounts import EditAccount


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class Account(QWidget, Ui_Form):
    def __init__(self, controller: MainController):
        super(Account, self).__init__()
        # self.ui = Ui_Form()
        self._controller = controller

        self.setupUi(self)
        self.view_data()

        self.btn_add_accounts.clicked.connect(self.add_new_accounts)

        # Align center text in cell of table
        delegate = AlignDelegate(self.tableView)
        self.tableView.setItemDelegate(delegate)
        # Align specific colunm
        # self.tableWidget.setItemDelegateForColumn(2, delegate)
        self.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.open_menu)
        self._controller.signals.table_get_completed.connect(
            self.on_reload_table_view)
        self._controller.signals.add_user_completed.connect(
            self.on_add_user_completed)
        self._controller.signals.add_user_error.connect(self.on_add_user_error)
        self._controller.signals.save_account_completed.connect(self.on_save_account_completed)

        self._controller.signals.table_on_load.emit()
        self.on_init_tableview()

    def on_add_user_completed(self):
        self._controller.signals.table_on_load.emit()
        self.add_dialog.close()

    def add_new_accounts(self):
        self.add_dialog = AddAccount(self._controller)
        self.add_dialog.show()
        self.add_dialog.trigger.connect(self.save_account)

    def save_account(self):
        # self.view_data()
        self._controller.signals.table_on_load.emit()
        self.add_dialog.close()

    def open_menu(self, position):
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            return

        menu = QMenu()
        menu.setStyleSheet
        open_chrome = QtGui.QAction("Open Chrome", self)
        edit_menu = QtGui.QAction("Edit", self)
        table_delete_action = QtGui.QAction("Delete", self)

        menu.addAction(open_chrome)
        menu.addAction(edit_menu)
        menu.addAction(table_delete_action)
        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        edit_menu.triggered.connect(self.on_open_edit_dialog)
        table_delete_action.triggered.connect(lambda: self._controller.delete_account(
            self.tableView.model(), self.tableView.selectionModel().selectedRows()))
        action = menu.exec_(self.tableView.mapToGlobal(position))

        # if action == quitAction:
        #     row = self.tableView.rowAt(position.y())
        #     col = self.tableView.columnAt(position.x())
        #     print(row,col)
        #     index = self.tableView.model().index(row,col)
        #     print(self.tableView.model().data(index))
        #     indexes = self.tableView.selectionModel().selectedRows()
        #     for index in sorted(indexes):
        #         print('Row %d is selected' % index.row())
        # elif action == openAction:
        #     print('Quyt')

    def on_open_edit_dialog(self):
        indexes = self.tableView.selectionModel().selectedRows()
        # seleted_row_index = [index.row() for index in sorted(indexes)]
        idexs_sql = [self.tableView.model().data(i) for i in sorted(indexes)]
        print(idexs_sql)
        # for idx in indexes:
        #     record = self.model.record(idx.row())
        #     record.setValue("ProxyID","2")
        #     self.model.setRecord(idx.row(), record)
        if idexs_sql:
            self.edit_dialog = EditAccount(self._controller, self.model, idexs_sql, indexes)
            self.edit_dialog.show()

    def table_open_chrome(self, position):
        selected_indexs = self.tableView.selectionModel().selectedRows()
        selected_id_proxy = [self.tableView.model().data(i) for i in selected_indexs]

        self._controller.open_chrome(selected_id_proxy)

        # row = self.tableView.rowAt(position.y())
        # col = self.tableView.columnAt(position.x())
        # print(row, col)
        # index = self.tableView.model().index(row, col)
        # print("index is ", index)
        # print(self.tableView.model().data(index))
        # indexes = self.tableView.selectionModel().selectedRows()
        # for index in sorted(indexes):
        #     print('Row %d is selected' % index.row())

    def table_delete(self, position):
        print("Delete row")
        indexes = self.tableView.selectionModel().selectedRows()

        index = self.tableView.selectedIndexes()[0]
        id = str(self.tableView.model().data(index))
        print("id is ", id)
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('accounts')
        self.model.select()
        self.tableView.setModel(self.model)
        
    
    def on_save_account_completed(self):
        self._controller.signals.table_on_load.emit()
        self.edit_dialog.close()

    Slot()
    def on_add_user_error(self):
        QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                       "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)

    Slot(object)
    def on_reload_table_view(self, tb_model):
        self.tableView.setModel(tb_model)
        # self.tableView.setColumnHidden(1,True)

    def on_init_tableview(self):
        self.headerView = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        # self.tableView.setColumnHidden(1,True)
        # self.tableView.setColumnWidth(0,100 )
        # self.tableView.setColumnWidth(1,100 )
        # self.tableView.setColumnWidth(3,100 )

        #RENAME HEADER
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal,"ID")
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Name")
        # self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")
        self.tableView.setModel(self.model)