from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMenu,QVBoxLayout, QAbstractItemView
from PySide6.QtCore import QSortFilterProxyModel,QRegularExpression
from PySide6.QtSql import QSqlTableModel
from PySide6.QtCore import Signal, Slot, Qt

from views.ui.account_ui import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui
from views.add_accounts import AddAccount
from controllers.main_ctrl import MainController
from views.edit_accounts import EditAccount
from views.table_custome import TableCustome



class Account(QWidget, Ui_Form):
    def __init__(self, controller: MainController):
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
        # self.proxy = CustomProxyModel()
        # self.proxy.setSourceModel(self.model)
        self.table_accounts.proxy.setSourceModel(self.model)
        self.table_accounts.ui.tableView.setModel(self.table_accounts.proxy)
        self.header = self.table_accounts.ui.tableView.horizontalHeader()

        # self.view_data()

        self.btn_add_accounts.clicked.connect(self.add_new_accounts)
        self.btn_refresh.clicked.connect(self.refresh)

        # Align center text in cell of table
        # delegate = AlignDelegate(self.tableView)
        # self.tableView.setItemDelegate(delegate)
        # Align specific colunm
        # self.tableWidget.setItemDelegateForColumn(2, delegate)
        
        self.table_accounts.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.table_accounts.ui.tableView.customContextMenuRequested.connect(self.open_menu)


        # self.horizontalHeader = self.tableView.horizontalHeader()
        # self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)

        # self._controller.signals.table_get_completed.connect(
        #     self.on_reload_table_view)
        self._controller.signals.add_user_completed.connect(
            self.on_add_user_completed)
        # self._controller.signals.add_user_error.connect(self.on_add_user_error)
        self._controller.signals.save_account_completed.connect(self.on_save_account_completed)

        # self._controller.signals.table_on_load.emit()
        # self.on_init_tableview()
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

        
    def on_add_user_completed(self):
        self.refresh()
        self.add_dialog.close()

    def add_new_accounts(self):
        self.add_dialog = AddAccount(self._controller)
        self.add_dialog.show()
        self.add_dialog.trigger.connect(self.save_account)

    def save_account(self):
        # self.view_data()
        # self._controller.signals.table_on_load.emit()
        self.add_dialog.close()
        self.refresh()

    def open_menu(self, position):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return

        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        self.seleted_id = [self.table_accounts.ui.tableView.model().data(i) for i in sorted(indexes)]

        menu = QMenu()
        # menu.setStyleSheet
        open_chrome = QtGui.QAction("Open Chrome", self)
        login_chrome = QtGui.QAction("Login Chrome", self)
        # edit_menu = QtGui.QAction("Edit", self)
        table_delete_action = QtGui.QAction("Delete: {}".format(len(self.seleted_id)), self)

        menu.addAction(open_chrome)
        menu.addAction(login_chrome)
        # menu.addAction(edit_menu)
        menu.addAction(table_delete_action)
        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        login_chrome.triggered.connect(self.on_login_chrome)
        # edit_menu.triggered.connect(self.on_open_edit_dialog)
        table_delete_action.triggered.connect(self.delete_selected_row)
        # table_delete_action.triggered.connect(lambda: self._controller.delete_account(
        #     self.tableView.model(), self.tableView.selectionModel().selectedRows()))
        action = menu.exec_(self.table_accounts.ui.tableView.mapToGlobal(position))

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
    def delete_selected_row(self):
        sql_query = "DELETE FROM accounts WHERE ID IN ({})".format(",".join([str(id) for id in self.seleted_id]))
        self.model.setQuery(sql_query)
        self.model.submitAll()
        # self.model.setTable('accounts')
        # self.model.submitAll()
        # self.model.select()
        self.refresh()
    def on_login_chrome(self):
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(1)
        selected_id_proxy = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

        self._controller.login_chrome(selected_id_proxy)
    def on_open_edit_dialog(self):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        # seleted_row_index = [index.row() for index in sorted(indexes)]
        idexs_sql = [self.table_accounts.ui.tableView.model().data(i) for i in sorted(indexes)]
        print(idexs_sql)
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
        # print(self.activeUID)
    
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(1) 
        selected_id_proxy = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

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
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()

        index = self.table_accounts.ui.tableView.selectedIndexes()[0]
        id = str(self.table_accounts.ui.tableView.model().data(index))
        print("id is ", id)
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())
        
    def on_save_account_completed(self):
        self._controller.signals.table_on_load.emit()
        self.edit_dialog.close()

    Slot()
    def on_add_user_error(self):
        QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                       "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)


    def refresh(self):
        self.model.setTable('accounts')
        self.model.select()
        # self.header.moveSection(9,3)

        # self.table_accounts.ui.tableView.resizeColumnsToContents()
        self.table_accounts.ui.tableView.setColumnWidth(1,120)
        self.table_accounts.ui.tableView.setColumnWidth(4,100)
        self.table_accounts.ui.tableView.setColumnWidth(5,120)