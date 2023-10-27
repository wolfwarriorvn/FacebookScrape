from PySide6.QtWidgets import QWidget, QMenu,QVBoxLayout, QInputDialog, QLineEdit
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QIcon

from views.ui.dashboard_ui import Ui_DashBoard
from PySide6 import QtGui
from controllers.main_ctrl import MainController
from views.table_custome import TableCustome

from views.action.post_dialog import PostDialog
from views.action.scan_history_dialog import ScanPostDialog
from views.action.seeding_dialog import SeedingDialog

class DashBoard(QWidget, Ui_DashBoard):
    def __init__(self, controller: MainController):
        super(DashBoard, self).__init__()
        self._controller = controller
        
        self.setupUi(self)
 
        self.verticalLayout = QVBoxLayout(self.tb_dashboard)
        self.table_accounts = TableCustome()
        self.verticalLayout.addWidget(self.table_accounts)
        self.model = QSqlTableModel(self)
        self.tableView = self.table_accounts.ui.tableView  

        #Right click menu
        self.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.right_click_menu)

        self._controller.signals.update_dashboard.connect(self.refresh)

        self.model.setQuery('SELECT ID,UserID, PageID, Category, Status, Message  FROM accounts')
        self.model.select()
        self.table_accounts.proxy.setSourceModel(self.model)
        self.tableView.setModel(self.table_accounts.proxy)

        self.btn_refresh.clicked.connect(self.refresh)

        self.refresh()

    def right_click_menu(self, position):
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        
        selected_indexs = self.tableView.selectionModel().selectedRows()
        self.seleted_ids = [self.tableView.model().data(i) for i in sorted(selected_indexs)]

        selected_indexs = self.tableView.selectionModel().selectedRows(1) 
        self.selected_uids = [self.tableView.model().data(i) for i in selected_indexs]

        menu = QMenu()
        menu.setStyleSheet('font: 13px;')
        open_chrome = QtGui.QAction(QIcon(":/icon/views/icon/chrome.png"),"Open Chrome", self)
        change_category = QtGui.QAction(QIcon(":/icon/views/icon/options.png"),"Set Category", self)
        scan_post_history = QtGui.QAction(QIcon(":/icon/views/icon/post.png"),"Scan History Post", self)
        seeding = QtGui.QAction(QIcon(":/icon/views/icon/positive-vote.png"), "Seeding", self)
        post_group = QtGui.QAction(QIcon(":/icon/views/icon/blog.png"), "Post Group", self)
        menu.addAction(open_chrome)
        menu.addAction(change_category)
        menu.addAction(scan_post_history)
        menu.addAction(seeding)
        menu.addAction(post_group)
        open_chrome.triggered.connect(self.open_chrome)
        change_category.triggered.connect(self.change_category)
        scan_post_history.triggered.connect(self.scan_history_post)
        seeding.triggered.connect(self.seeding)
        post_group.triggered.connect(self.posting)
        
        action = menu.exec_(self.table_accounts.ui.tableView.mapToGlobal(position))

    def open_chrome(self):
        selected_indexs = self.tableView.selectionModel().selectedRows(1) 
        selected_id_proxy = [self.tableView.model().data(i) for i in selected_indexs]

        self._controller.open_chrome(selected_id_proxy)

    def change_category(self):
        category, ok = QInputDialog.getText(self, "Edit Category", "Category: ", QLineEdit.Normal, None)
        if not ok:
            return
        sql_query = "UPDATE accounts SET Category='{}' WHERE ID IN ({})".format(category, ",".join([str(id) for id in self.seleted_ids]))
        self.model.setQuery(sql_query)
        self.model.submitAll()
        self.refresh()
    
    def scan_history_post(self):
        selected_indexs = self.tableView.selectionModel().selectedRows(1) 
        selected_ids = [self.tableView.model().data(i) for i in selected_indexs]

        self.scan_post_dialog = ScanPostDialog(self._controller, selected_ids)
        self.scan_post_dialog.show()

    def seeding(self):
        selected_indexs = self.tableView.selectionModel().selectedRows(1) 
        selected_ids = [self.tableView.model().data(i) for i in selected_indexs]
        self.scan_post_dialog = SeedingDialog(self._controller, selected_ids)
        self.scan_post_dialog.show()
    
    def posting(self):
        self.scan_post_dialog = PostDialog(self._controller, self.selected_uids)
        self.scan_post_dialog.show()
    def refresh(self):
        self.model.setQuery('SELECT ID,UserID, PageID, Category, Status, Message  FROM accounts')
        self.model.select()
        # self.table_accounts.proxy.setSourceModel(self.model)
        # self.tableView.setModel(self.table_accounts.proxy)
        self.table_accounts.ui.tableView.setColumnWidth(1,120)
        self.table_accounts.ui.tableView.setColumnWidth(2,120)
