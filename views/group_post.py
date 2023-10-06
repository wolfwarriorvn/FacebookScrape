from PySide6.QtWidgets import QWidget, QMenu, QFileDialog
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (QApplication, QFrame, QVBoxLayout, QSizePolicy,QPushButton,
    QWidget)
from views.ui.fanpages.group_post_ui import Ui_GroupPost
from views.table_custome import TableCustome
from controllers.main_ctrl import MainController
from lib_type import PostSetting
from random import *

class GroupPost(QWidget):
    def __init__(self, controller: MainController):
        super(GroupPost, self).__init__()
        self._controller = controller
        self.ui = Ui_GroupPost()
        self.ui.setupUi(self)

        self.vertical_acc_layout = QVBoxLayout(self.ui.tbl_acc)
        self.table_accounts = TableCustome()
        self.vertical_acc_layout.addWidget(self.table_accounts)
        

        self.acc_model = QSqlTableModel(self)
        # self.groups_model = QSqlTableModel(self)

        self.refresh()

        self.groups_model = QSqlTableModel(self)
        self.groups_model.setQuery('SELECT DISTINCT Type FROM groups_tita')
        self.ui.cb_group_type.setModel(self.groups_model)
        self.ui.cb_group_type.installEventFilter(self)
        # self.ui.cb_group_type.setModelColumn(1)

        self.table_accounts.ui.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.table_accounts.ui.tableView.customContextMenuRequested.connect(self.open_menu)

        self.ui.btn_select_image.clicked.connect(self.get_path_image)
        self.ui.btn_run.clicked.connect(self.post_group)

        self._controller.signals.outof_free_groups.connect(self.outof_group)
    
    def outof_group(self, free_group_number):
        QtWidgets.QMessageBox.warning(None, "Hết nhóm rãnh rồi.",
                                           "Số nhóm còn lại: {}".format(free_group_number), QtWidgets.QMessageBox.Cancel)

    def eventFilter(self,target,event):
        if target == self.ui.cb_group_type and event.type() == QtCore.QEvent.MouseButtonPress:
            self.groups_model.setQuery('SELECT DISTINCT Type FROM groups_tita')
            self.ui.cb_group_type.setModel(self.groups_model)
        return False
    def post_group(self):
        uids = []
        page_ids = []
        contents = self.ui.txt_contents.toPlainText().split('|')
        photo_dir = self.ui.le_image_path.text()
        _type = self.ui.cb_group_type.currentText()
        for index in self.table_accounts.ui.tableView.selectionModel().selectedRows():
            row = index.row()
            uid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,1))
            pageid = self.table_accounts.ui.tableView.model().data(self.table_accounts.ui.tableView.model().index(row,9))
            uids.append(uid)
            page_ids.append(pageid)

        self._controller.signals.post_group.emit(uids, page_ids, self.ui.num_posts.value(), self.ui.post_start_ms.value(), self.ui.post_stop_ms.value(), contents, photo_dir, _type)    
  

    def get_path_image(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        uppath = folder_path.replace("/", '\\')
        self.ui.le_image_path.setText(uppath)
    def open_menu(self, position):
        indexes = self.table_accounts.ui.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        menu = QMenu()
        open_chrome = QtGui.QAction("Open Chrome", self)
        menu.addAction(open_chrome)
        open_chrome.triggered.connect(lambda: self.table_open_chrome(position))
        action = menu.exec_(self.table_accounts.ui.tableView.mapToGlobal(position))

    def table_open_chrome(self, position):
        PAGE_TABLE_UID_COLUMN = 1
        selected_indexs = self.table_accounts.ui.tableView.selectionModel().selectedRows(PAGE_TABLE_UID_COLUMN)
        selected_uids = [self.table_accounts.ui.tableView.model().data(i) for i in selected_indexs]

        print("id selected: ", selected_uids)

        self._controller.open_chrome(selected_uids)


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