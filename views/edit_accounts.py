from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.account_edit_menu_ui import Ui_Form
from views.connection import Connection
from controllers.controller import Controller

class EditAccount(QWidget, Ui_Form):

    def __init__(self, controller: Controller, model, indexs, raw_idx):
        super(EditAccount, self).__init__()
        self._controller = controller
        self.model = model
        self.raw_idx = raw_idx
        self.setupUi(self)
        #TODO: implement logic for it