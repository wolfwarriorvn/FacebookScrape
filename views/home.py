from PySide6.QtWidgets import QWidget, QTableWidgetItem,QMenu
from PySide6.QtSql import QSqlTableModel

from views.ui.pages.ui_home import Ui_Form
from PySide6 import QtWidgets,QtCore,QtGui
from views.add_accounts import AddAccount

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class Home(QWidget, Ui_Form):
    def __init__(self, controller):
        super(Home, self).__init__()
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

    def add_new_accounts(self):
        self.add_dialog = AddAccount(self._controller)
        self.add_dialog.show()
        self.add_dialog.trigger.connect(self.save_account)

    def save_account(self):
        self.view_data()
        self.add_dialog.close()

    def open_menu(self,position):
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        
        menu = QMenu()
        menu.setStyleSheet
        open_chrome = QtGui.QAction("Open Chrome", self)
        table_delete_action = QtGui.QAction("Delete", self)

        menu.addAction(open_chrome)
        menu.addAction(table_delete_action)
        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        table_delete_action.triggered.connect(lambda: self.table_delete(position))
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

    def table_open_chrome(self, position):
        row = self.tableView.rowAt(position.y())
        col = self.tableView.columnAt(position.x())
        print(row,col)
        index = self.tableView.model().index(row,col)
        print(self.tableView.model().data(index))
        indexes = self.tableView.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())

    def table_delete(self, position):
        print("Delete row")

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('accounts')
        self.model.select()
        self.tableView.setModel(self.model)


        
