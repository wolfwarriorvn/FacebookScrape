from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.page_add_ui import Ui_PageAdd
from views.connection import Connection
from common.payload import AccountFormat


class PageAdd(QWidget, Ui_PageAdd):

    def __init__(self, controller):
        super(PageAdd, self).__init__()
        self._controller = controller
        self.setupUi(self)
    

    


