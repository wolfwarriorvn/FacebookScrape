from PySide6.QtWidgets import QWidget,QWidgetAction
from PySide6.QtWidgets import QWidget, QMenu,QInputDialog,QLineEdit,QHeaderView
from PySide6.QtCore import QSortFilterProxyModel,QRegularExpression, Qt,QItemSelectionModel
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (QApplication, QMenu, QFrame, QVBoxLayout, QSizePolicy,QPushButton,
    QWidget)
from views.ui.fanpages.joined_groups_ui import Ui_JoinedGroup
from views.table_custome import TableCustome
from controllers.controller import Controller
import logging

class CustomProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._filters = dict()

    @property
    def filters(self):
        return self._filters
    def clearFilters(self):
        self._filters.clear()
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
    def setFilter(self, expresion, column):
        if expresion:
            self._filters[column] = expresion
        elif column in self._filters:
            del self._filters[column]
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for column, expresion in self._filters.items():
            text = self.sourceModel().index(source_row, column, source_parent).data()
            regex = QRegularExpression(
                expresion, QRegularExpression.CaseInsensitiveOption
            )
            if not regex.match(text).hasMatch():
                return False
        return True

class GroupView(QWidget):
    def __init__(self, controller: Controller):
        super(GroupView, self).__init__()
        self._controller = controller
        self.ui = Ui_JoinedGroup()
        self.ui.setupUi(self)
        self.activeUID = None
        
        self._controller.signals.scan_group_completed.connect(self.refresh)

        
        self.verticalLayout = QVBoxLayout(self.ui.tbl_group)
        self.table_group_view = TableCustome()
        self.verticalLayout.addWidget(self.table_group_view)


        self.model = QSqlTableModel(self)
        # self.model.setQuery('SELECT * from fanpages')
        # self.model.select()
        # self.table_group_view.ui.tableView.setModel(self.model)

        #TODO: show model in table with custome condition
        self.page_model = QSqlTableModel(self)
        self.page_model.setQuery('SELECT * from fanpages')
        self.page_model.select()

        self.acc_model = QSqlTableModel(self)
        self.acc_model.setQuery('SELECT * FROM accounts')
        self.ui.cb_uids.setModel(self.acc_model)
        self.ui.cb_uids.setModelColumn(1)

        # self.ui.cb_pages.setModel(self.page_model)
        # self.ui.cb_pages.setModelColumn(2) 
        
        self.ui.cb_uids.installEventFilter(self)

        self.ui.btn_view_group.clicked.connect(self.show_default_group)
        self.ui.btn_view_scan_group.clicked.connect(self.show_scan_group_by_keyword)
        self.ui.btn_scan_by_key.clicked.connect(self.scan_groups_by_keyword)
        self.ui.btn_posts.clicked.connect(self.view_posts_table)
        self.ui.btn_history_posts.clicked.connect(self.scan_post_history)

        self.table_group_view.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.table_group_view.ui.tableView.customContextMenuRequested.connect(self.open_group_menu)


        self.horizontalHeader = self.table_group_view.ui.tableView.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)

        # self.headers =   self.table_group_view.ui.tableView.horizontalHeader()
        self.horizontalHeader.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.horizontalHeader.customContextMenuRequested.connect(self.header_popup)
    
        # self.horizontalHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        # self.table_group_view.ui.tableView.setColumnWidth(0,10)
        self.table_group_view.ui.tableView.setColumnWidth(1,100)
        self.on_init()

    def scan_post_history(self):
        selected_ids = []
        selected_ids.append(self.ui.cb_uids.currentText())
        loop_scan, ok = QInputDialog.getInt(self, "Quét history post",
                                        "Loop Scan:", 1, 1, 100, 1)
        if not ok:
            return
        self._controller.signals.scan_post_history.emit(selected_ids , loop_scan, 1)
    def header_popup(self, pos) :
        self.header_right_click_column =  self.horizontalHeader.logicalIndexAt(pos)
        menu = QMenu()
        ql = QLineEdit()
        ql.textChanged.connect(self.onTextChanged)
        wAction = QWidgetAction(self)
        wAction.setDefaultWidget(ql)
        menu.addAction(wAction)
        action = menu.exec_(self.table_group_view.ui.tableView.mapToGlobal(pos))

    def onTextChanged(self, text):
        self.proxy.setFilter(text, self.header_right_click_column)
    def open_group_menu(self, position):
        indexes = self.table_group_view.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        
        
        # selected_indexs = self.table_group_view.ui.tableView.selectionModel().selectedRows(0)

        # self.seleted_id = [self.model.data(self.proxy.mapToSource(index)) for index in sorted(selected_indexs)]  
        selected_indexs = self.table_group_view.ui.tableView.selectionModel().selectedRows()

        self.seleted_id = [self.table_group_view.ui.tableView.model().data(i) for i in sorted(selected_indexs)]
        
        menu = QMenu()
        table_delete_action = QtGui.QAction("Delete: {}".format(len(self.seleted_id)), self)
        edit_type = QtGui.QAction("Edit Type", self)
        menu.addAction(edit_type)
        menu.addAction(table_delete_action)
        edit_type.triggered.connect(self.edit_type)
        table_delete_action.triggered.connect(self.delete_selected_row)
        

        if self.active_tb == 'groups_tita':
            check_allow_page_interact = QtGui.QAction("Kiểm tra nhóm chấp nhận tương tác Page")
            menu.addAction(check_allow_page_interact)
            check_allow_page_interact.triggered.connect(self.on_check_allow_page_interact)
        elif self.active_tb == 'posts':
            menu.removeAction(edit_type)
            scan_approve_post = QtGui.QAction("Quét approve post", self)
            menu.addAction(scan_approve_post)
            scan_approve_post.triggered.connect(self.on_scan_approve_post)
        else:
            filter_notsave = QtGui.QAction("Lọc nhóm chưa lưu", self)
            save_action = QtGui.QAction("Lưu", self)
            menu.addAction(filter_notsave)
            menu.addAction(save_action)
            save_action.triggered.connect(self.save_database)
            filter_notsave.triggered.connect(self.filter_notsave)
            
        action = menu.exec_(self.table_group_view.ui.tableView.mapToGlobal(position))

    def on_check_allow_page_interact(self):
        COLUMN_GROUP_LINK = 1
        uid = self.ui.cb_uids.currentText()
        selected_indexs = self.table_group_view.ui.tableView.selectionModel().selectedRows(COLUMN_GROUP_LINK)

        self.group_links = [self.table_group_view.ui.tableView.model().data(i) for i in sorted(selected_indexs)]

        self._controller.signals.check_group_allow_page.emit(uid, self.group_links)
    def on_scan_approve_post(self):
        uid = self.ui.cb_uids.currentText()
        selected_indexs = self.table_group_view.ui.tableView.selectionModel().selectedRows(3)

        self.post_links = [self.table_group_view.ui.tableView.model().data(i) for i in sorted(selected_indexs)]

        self._controller.signals.check_approval_post.emit(uid, self.post_links)

    def filter_notsave(self):
        sql_query = "DELETE FROM {}  WHERE {}.Group_Link  IN (SELECT Group_Link FROM groups_tita)".format(self.active_tb, self.active_tb)
        self.model.setQuery(sql_query)
        if self.model.lastError().isValid():
            logging.error(self.model.lastError().text())
        
        self.model.setQuery(sql_query)
        self.model.submitAll()
        self.model.setTable(self.active_tb)
        # #refresh table
        self.model.submitAll()
        self.model.select()
        self.refresh_header_size()

    def edit_type(self):
        g_type, ok = QInputDialog.getText(self, "Edit Type",
                                        "Type:", QLineEdit.Normal,None)
        if not ok:
            return
        
        sql_query = "UPDATE {} SET Type='{}' WHERE ID IN ({})".format(self.active_tb, g_type, ",".join([str(id) for id in self.seleted_id]))
        self.model.setQuery(sql_query)
        self.model.submitAll()
        self.model.setTable(self.active_tb)
        # #refresh table
        self.model.submitAll()
        self.model.select()
        self.refresh_header_size()

    def save_database(self):
        sql_query = "INSERT INTO groups_tita(Group_Link,Group_Name,Category,Numbers,Details,Type) SELECT Group_Link,Group_Name,Category,Numbers,Details,Type FROM {} WHERE ID IN ({}) AND {}.Group_Link  NOT IN (SELECT Group_Link FROM groups_tita)".format(self.active_tb, ",".join([str(id) for id in self.seleted_id]), self.active_tb)
        self.model.setQuery(sql_query)
        if self.model.lastError().isValid():
            logging.error(self.model.lastError().text())
        
        self.model.setQuery(sql_query)
        self.model.submitAll()
        self.model.setTable(self.active_tb)
        # #refresh table
        self.model.submitAll()
        self.model.select()     
        self.refresh_header_size()  
    def delete_selected_row(self):
        sql_query = "DELETE FROM {} WHERE ID IN ({})".format(self.active_tb, ",".join([str(id) for id in self.seleted_id]))

        # for index in sorted(indexes):
        #     mapped_index = self.proxy.mapToSource(index)
        #     self.model.removeRow(mapped_index.row())
        
        self.model.setQuery(sql_query)
        self.model.submitAll()
        self.model.setTable(self.active_tb)
        # #refresh table
        self.model.submitAll()
        self.model.select()
        self.refresh_header_size()

    def scan_groups_by_keyword(self):
        keyword = self.ui.le_key_search.text()
        loop_scan = int(self.ui.number_of_groups.value()/9)
        if not keyword:
            QtWidgets.QMessageBox.critical(None, "Quét Nhóm","Chọn Từ khoá.", QtWidgets.QMessageBox.Cancel)
            return

        uid = self.ui.cb_uids.currentText()
        self._controller.signals.scan_group_by_keyword.emit(uid, keyword, loop_scan)

    def view_posts_table(self):
        self.proxy.clearFilters()
        self.active_tb = 'posts'
        self.model.setTable(self.active_tb)
        status = self.model.select()

        # self.proxy = CustomProxyModel()
        self.proxy.setSourceModel(self.model)

        self.table_group_view.ui.tableView.setModel(self.proxy)
        self.refresh_header_size()

    def show_scan_group_by_keyword(self):
        self.proxy.clearFilters()
        uid = self.ui.cb_uids.currentText()
        self.active_tb = 'groups_' + uid
        self.model.setTable(self.active_tb)
        status = self.model.select()

        # self.proxy = CustomProxyModel()
        
        self.proxy.setSourceModel(self.model)
        
        self.table_group_view.ui.tableView.setModel(self.proxy)     
        self.refresh_header_size() 
    def show_default_group(self):
        self.proxy.clearFilters()
        self.active_tb = 'groups_tita'
        self.model.setTable(self.active_tb)
        status = self.model.select()

        # self.proxy = CustomProxyModel()
    
        self.proxy.setSourceModel(self.model)

        self.table_group_view.ui.tableView.setModel(self.proxy)
        self.refresh_header_size()

    def eventFilter(self,target,event):
        if target == self.ui.cb_uids and event.type() == QtCore.QEvent.MouseButtonPress:
            self.acc_model = QSqlTableModel(self)
            self.acc_model.setQuery('SELECT * FROM accounts')
            self.ui.cb_uids.setModel(self.acc_model)
            self.ui.cb_uids.setModelColumn(1)
        return False
    
    def refresh(self):
        self.proxy.clearFilters()
        self.active_pageid = ''
        self.model.setTable('groups_' + self.active_pageid)
        status = self.model.select()

        # self.proxy = QSortFilterProxyModel()
        # self.proxy = CustomProxyModel()
        
        self.proxy.setSourceModel(self.model)

        self.table_group_view.ui.tableView.setModel(self.proxy)

        # self.proxy_model.setFilterFixedString('Dep')
        # self.proxy_model.setFilterKeyColumn(4)

    def on_init(self):
        # index = self.ui.cb_pages.model().index(self.ui.cb_pages.currentIndex(),3)
        # self.activeUID = self.ui.cb_pages.model().data(index)

        # page_index = self.ui.cb_pages.model().index(self.ui.cb_pages.currentIndex(),1)
        # self.active_pageid = self.ui.cb_pages.model().data(page_index)

        self.proxy = CustomProxyModel()
        self.refresh()


    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex   = logicalIndex
        #disable  specific column menu
        if self.active_tb == 'posts':
            if self.logicalIndex  not in [1,4]:
                return
        elif self.active_tb == 'groups_tita':
            if self.logicalIndex not in [3,6,7,11]:
                return
        else:
            if self.logicalIndex  not in [3,6,7]:
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
        headerPos = self.table_group_view.ui.tableView.mapToGlobal(self.horizontalHeader.pos())
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


    def refresh_header_size(self):
        # self.horizontalHeader.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table_group_view.ui.tableView.resizeColumnsToContents()
        if self.active_tb == 'groups_tita':
            self.table_group_view.ui.tableView.setColumnWidth(1,50)
            self.table_group_view.ui.tableView.setColumnWidth(2,200)
            self.table_group_view.ui.tableView.setColumnWidth(5,100)
        elif self.active_tb == ('groups_' + self.ui.cb_uids.currentText()):
            self.table_group_view.ui.tableView.setColumnWidth(1,100)
            self.table_group_view.ui.tableView.setColumnWidth(5,150)
        elif self.active_tb == 'posts': 
            self.table_group_view.ui.tableView.setColumnWidth(2,100)
