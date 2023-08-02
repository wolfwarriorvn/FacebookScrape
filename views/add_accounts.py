from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.addmenu_ui import Ui_Addaccount
from views.connection import Connection


class AddAccount(QWidget, Ui_Addaccount):
    trigger = Signal()

    def __init__(self, controller):
        super(AddAccount, self).__init__()
        self._controller = controller
        self.setupUi(self)
        # self.acc_db = Connection()
        self.btn_save.clicked.connect(lambda: self._controller.add_new_account(self.txt_accounts.toPlainText()))
    


