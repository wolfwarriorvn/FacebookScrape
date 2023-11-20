from PySide6.QtWidgets import QWidget,QMenu
from PySide6 import QtWidgets, QtSql, QtGui
from PySide6.QtSql import QSqlTableModel

from views.ui.proxy_ui import Ui_Form

import parse
from common.extension import proxies
from views.messages import show_error_message
class Proxy(QWidget, Ui_Form):
    def __init__(self, controller):
        super(Proxy, self).__init__()
        self.ui = Ui_Form()
        self.controller = controller
        self.setupUi(self)
        self.on_init()
        #add right click menu
        self.tableView.setContextMenuPolicy(QtGui.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.open_menu)
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
        request = {
            'table': 'proxy',
            'column': 'ID',
            'values_list' : selected_id_proxy}
        
        self.controller.database_operation.emit('delete', self.on_delete_proxy_response, request)

    def on_delete_proxy_response(self, result, error):
        if error:
            show_error_message(f"Error: {error}", self)
        else:
            self.refresh()
    

    def on_add_new_proxy(self):
        proxy = parse.parse('{0}:{1}@{3}:{4}', self.le_proxy.text())
        if proxy:
            user_proxy = proxy[0]
            pass_proxy = proxy[1]
            endpoint_proxy = proxy[2]
            port_proxy = proxy[3]
            extension_zip = proxies(user_proxy, pass_proxy, endpoint_proxy, port_proxy, user_proxy)

            request = {
                'table': 'proxy',
                'data': [{
                    'ProxyID' : self.le_proxy.text(),
                    'zip_proxy' : user_proxy
                }]
            }
            self.controller.database_operation.emit('insert', self.on_add_proxy_completed, request)

    def on_add_proxy_completed(self, result, error):
        if error:
            show_error_message(error, self)
        else:
            self.refresh()

    def on_init(self):
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS proxy (ID integer primary key, ProxyID UNIQUE, zip_proxy VARCHAR(20))")
        self.refresh()
        
    def refresh(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('proxy')
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(1, 400)
        