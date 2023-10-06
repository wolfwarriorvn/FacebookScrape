from PySide6.QtWidgets import QWidget, QMenu, QInputDialog, QLineEdit
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (QApplication, QFrame, QVBoxLayout, QSizePolicy,QPushButton,
    QWidget)
from views.ui.fanpages.fanpages_view_ui import Ui_FanpageView
from views.table_custome import TableCustome
from controllers.main_ctrl import MainController


PAGE_ID_COLUMN = 9

class FanpageView(QWidget):
    def __init__(self, controller: MainController):
        super(FanpageView, self).__init__()
        self._controller = controller
        self.ui = Ui_FanpageView()
        self.ui.setupUi(self)

        self.vertical_acc_layout = QVBoxLayout(self.ui.tbl_acc)
        self.table_accounts = TableCustome()
        self.vertical_acc_layout.addWidget(self.table_accounts)
        
        self.vertical_groups_layout = QVBoxLayout(self.ui.tbl_group)
        self.table_groups = TableCustome()
        self.vertical_groups_layout.addWidget(self.table_groups)

        self.acc_model = QSqlTableModel(self)
        self.groups_model = QSqlTableModel(self)

        self.refresh()

        self.table_accounts.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.table_accounts.ui.tableView.customContextMenuRequested.connect(self.open_menu)

    def open_menu(self, position):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        menu = QMenu()
        open_chrome = QtGui.QAction("Open Chrome", self)
        scan_groups = QtGui.QAction("Quét nhóm đã tham gia", self)
        scan_groups_with_keywords = QtGui.QAction("Quét nhóm từ khoá", self)
        joined_groups = QtGui.QAction("Xem Nhóm Của Page", self)

        menu.addAction(open_chrome)
        menu.addAction(scan_groups)
        menu.addAction(scan_groups_with_keywords)
        menu.addAction(joined_groups)

        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        scan_groups.triggered.connect(self.on_scan_groups)
        scan_groups_with_keywords.triggered.connect(self.on_scan_groups_with_keyword)
        joined_groups.triggered.connect(self.view_group_of_page)
        action = menu.exec_(self.table_accounts.ui.tableView.mapToGlobal(position))

    def table_open_chrome(self, position):
        PAGE_TABLE_UID_COLUMN = 1
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(PAGE_TABLE_UID_COLUMN)
        selected_uids = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

        print("id selected: ", selected_uids)

        self._controller.open_chrome(selected_uids)

    def on_scan_groups_with_keyword(self):
        text, ok = QInputDialog.getText(self, "Quét nhóm theo từ khoá",
                                        "Từ khoá:", QLineEdit.Normal,None)
        if ok and text:
            print(text)
    def on_scan_groups(self):
        uids = []
        page_ids = []
        for index in self.table_accounts.ui.tableView.selectionModel().selectedRows():
            row = index.row()
            uid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,1))

            page_uid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,9))

            uids.append(uid)
            page_ids.append(page_uid)
        print(uids, page_ids)
        self._controller.signals.scan_group.emit(uids, page_ids)

    def view_group_of_page(self):
        first_selected_row = self.table_accounts.ui.tableView.selectionModel().selectedRows()[0]
        row = first_selected_row.row()

        uid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,1))

        page_uid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,9))

        activeID = uid if page_uid == '' else page_uid
        table_name = 'groups_' + activeID

        self.groups_model.setTable(table_name)
        self.groups_model.select()
        self.table_groups.ui.tableView.setModel(self.groups_model)
    def refresh(self):

        self.acc_model.setTable('accounts')
        self.acc_model.select()
        self.table_accounts.ui.tableView.setModel(self.acc_model)
        self.table_accounts.ui.tableView.setColumnHidden(0,True)
        self.table_accounts.ui.tableView.setColumnHidden(2,True)
        self.table_accounts.ui.tableView.setColumnHidden(3,True)
        self.table_accounts.ui.tableView.setColumnHidden(4,True)
        self.table_accounts.ui.tableView.setColumnHidden(5,True)
        self.table_accounts.ui.tableView.setColumnHidden(6,True)
        self.table_accounts.ui.tableView.setColumnHidden(7,True)
        self.table_accounts.ui.tableView.setColumnHidden(8,True)

        self.table_accounts.ui.tableView.setColumnWidth(0,120 )
        self.table_accounts.ui.tableView.setColumnWidth(1,120 )

        self.groups_model.setTable('fanpages')
        self.groups_model.select()
        self.table_groups.ui.tableView.setModel(self.groups_model)