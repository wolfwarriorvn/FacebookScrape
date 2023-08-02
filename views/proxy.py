from PySide6.QtWidgets import QWidget,QMenu
from PySide6 import QtWidgets, QtSql, QtGui
from PySide6.QtSql import QSqlTableModel

from views.ui.proxy_ui import Ui_Form

import parse
from extension import proxies
from model.sqlutils import SqlUtils
class Proxy(QWidget, Ui_Form):
    def __init__(self):
        super(Proxy, self).__init__()
        self.ui = Ui_Form()
        self.setupUi(self)
        self.on_init()
        #add right click menu
        self.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.open_menu)
        self.sqlquery = SqlUtils()
        self.btn_add.clicked.connect(self.on_add_new_proxy)
    

    def open_menu(self, position):
        indexes = self.tableView.selectionModel().selectedRows()
        if not indexes:
            return
        menu = QMenu()
        delete = QtGui.QAction("Delete", self)
        menu.addAction(delete)
        delete.triggered.connect(self.on_delete_proxy)
        action = menu.exec_(self.tableView.mapToGlobal(position))
    
    def on_delete_proxy(self):
        selected_indexs = self.tableView.selectionModel().selectedRows()
        selected_id_proxy = [self.tableView.model().data(i) for i in selected_indexs]

        if selected_id_proxy:
            print("ID la: ", selected_id_proxy)
            self.sqlquery.delete_mul_proxy(selected_id_proxy)
            self.reload_tableview()


    def on_add_new_proxy(self):
        proxy = parse.parse('{0}:{1}@{3}:{4}', self.le_proxy.text())
        if proxy:
            user_proxy = proxy[0]
            pass_proxy = proxy[1]
            endpoint_proxy = proxy[2]
            port_proxy = proxy[3]
            extension_zip = proxies(user_proxy, pass_proxy, endpoint_proxy, port_proxy, user_proxy)
            try:
                self.sqlquery.add_proxy_query(self.le_proxy.text(), user_proxy)
                self.reload_tableview()
            except Exception as e:
                print(e)
    def on_init(self):
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS proxy (ID integer primary key, ProxyID UNIQUE, zip_proxy VARCHAR(20))")
        self.reload_tableview()

        self.tableView.setColumnWidth(1, 400)

        # self.tableView.horizontalHeader().resizeSection(1, 200)
    def reload_tableview(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('proxy')
        self.model.select()
        self.tableView.setModel(self.model)
        