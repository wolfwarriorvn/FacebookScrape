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



class Account(QWidget, Ui_Form):
    def __init__(self, controller: Controller):
        super(Account, self).__init__()
        # self.ui = Ui_Form()
        self._controller = controller

        self.setupUi(self)
        

        self.verticalLayout = QVBoxLayout(self.f_account)
        self.table_accounts = TableCustome()
        self.verticalLayout.addWidget(self.table_accounts)
        # self.tableView = self.table_accounts.ui.tableView
        self.model = QSqlTableModel(self)
        self.model.setTable('accounts')
        self.model.select()

        self.table_accounts.proxy.setSourceModel(self.model)
        self.table_accounts.ui.tableView.setModel(self.table_accounts.proxy)
        self.header = self.table_accounts.ui.tableView.horizontalHeader()

        self.btn_add_accounts.clicked.connect(self.add_new_accounts)
        self.btn_refresh.clicked.connect(self.refresh)
        
        self.table_accounts.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.table_accounts.ui.tableView.customContextMenuRequested.connect(self.open_menu)

        self.refresh()

    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex   = logicalIndex
        #disable  specific column menu
        if self.logicalIndex in [0,1,2,4,5,8]:
            return
        self.menuValues     = QtWidgets.QMenu(self)
        self.signalMapper   = QtCore.QSignalMapper(self)
        # self.comboBox.blockSignals(True)
        # self.comboBox.setCurrentIndex(self.logicalIndex)
        # self.comboBox.blockSignals(True)

        valuesUnique = set([self.model.index(i, logicalIndex).data() for i in range(self.model.rowCount())])

        actionAll = QtGui.QAction("All", self)
        actionAll.triggered.connect(self.on_actionAll_triggered)
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()
        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
            action = QtGui.QAction(actionName, self)
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(self.signalMapper.map)
            self.menuValues.addAction(action)
        self.signalMapper.mappedInt.connect(self.on_signalMapper_mapped)
        headerPos = self.table_accounts.ui.tableView.mapToGlobal(self.horizontalHeader.pos())
        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)

        self.menuValues.exec_(QtCore.QPoint(posX, posY))

    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        self.proxy.setFilter("", filterColumn)

        header_label = self.model.record().fieldName(self.logicalIndex)
        self.model.setHeaderData(self.logicalIndex,QtCore.Qt.Horizontal, header_label)

    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        self.proxy.setFilter(stringAction, filterColumn)


        header_label = self.model.record().fieldName(self.logicalIndex) + ': ' + stringAction
        self.model.setHeaderData(self.logicalIndex,QtCore.Qt.Horizontal, header_label)

    def on_lineEdit_textChanged(self, text):
        self.proxy.setFilter(text, self.proxy.filterKeyColumn())

    def on_comboBox_currentIndexChanged(self, index):
        self.proxy.setFilterKeyColumn(index)

    def add_new_accounts(self):
        self.add_dialog = AddAccount(self._controller)
        self.add_dialog.added_new_account.connect(self.refresh)
        self.add_dialog.show()
        
    def open_menu(self, position):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return

        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        self.seleted_id = [self.table_accounts.ui.tableView.model().data(i) for i in sorted(indexes)]

        menu = QMenu()
        # menu.setStyleSheet
        menu.setStyleSheet('font: 13px;')
        open_chrome = QtGui.QAction("Open Chrome", self)
        login_chrome = QtGui.QAction("Login Chrome", self)
        checkpoint_956 = QtGui.QAction("Checkpoint 956", self)
        # edit_menu = QtGui.QAction("Edit", self)
        table_delete_action = QtGui.QAction("Delete: {}".format(len(self.seleted_id)), self)

        menu.addAction(open_chrome)
        menu.addAction(login_chrome)
        checkpoint = menu.addMenu('Checkpoint')
        checkpoint.addAction(checkpoint_956)
        # menu.addAction(edit_menu)
        menu.addAction(table_delete_action)
        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        login_chrome.triggered.connect(self.on_login_chrome)
        checkpoint_956.triggered.connect(self.on_checkpoint_956)
        # edit_menu.triggered.connect(self.on_open_edit_dialog)
        table_delete_action.triggered.connect(self.delete_selected_row)
   
        action = menu.exec_(self.table_accounts.ui.tableView.mapToGlobal(position))

    def on_checkpoint_956(self):
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(1) 
        selected_ids = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]
        self._controller.signals.checkpoint_956.emit(selected_ids)

    def delete_selected_row(self):
        request = {
            'table': 'accounts',
            'column': 'ID',
            'values_list' : self.seleted_id}
        self._controller.database_operation.emit('delete', self.on_delete_user_completed, request)

    def on_delete_user_completed(self, result, error):
        if error:
            print(f"Error: {error}")
        else:
            self.refresh()

    def on_login_chrome(self):
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(1)
        selected_id_proxy = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

        self._controller.login_chrome(selected_id_proxy)

    def on_open_edit_dialog(self):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        # seleted_row_index = [index.row() for index in sorted(indexes)]
        idexs_sql = [self.table_accounts.ui.tableView.model().data(i) for i in sorted(indexes)]
        # for idx in indexes:
        #     record = self.model.record(idx.row())
        #     record.setValue("ProxyID","2")
        #     self.model.setRecord(idx.row(), record)
        if idexs_sql:
            self.edit_dialog = EditAccount(self._controller, self.model, idexs_sql, indexes)
            self.edit_dialog.show()

    def table_open_chrome(self, position):
        # index = self.ui.cb_pages.model().index(self.ui.cb_pages.currentIndex(),3)
        # self.activeUID = self.ui.cb_pages.model().data(index)
    
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(1) 
        selected_id_proxy = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

        self._controller.open_chrome(selected_id_proxy)
        
    def refresh(self):
        self.model.setTable('accounts')
        self.model.select()
        # self.header.moveSection(9,3)

        # self.table_accounts.ui.tableView.resizeColumnsToContents()
        self.table_accounts.ui.tableView.setColumnWidth(1,120)
        self.table_accounts.ui.tableView.setColumnWidth(4,100)
        self.table_accounts.ui.tableView.setColumnWidth(5,120)