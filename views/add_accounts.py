from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.addmenu_ui import Ui_Addaccount
from views.connection import Connection
from common import AccountFormat


class AddAccount(QWidget, Ui_Addaccount):
    trigger = Signal()

    def __init__(self, controller):
        super(AddAccount, self).__init__()
        self._controller = controller
        self.setupUi(self)
        self.cb_acc_format.addItems([AccountFormat.UID_PASS, 
                                     AccountFormat.CUSTOM1,
                                     AccountFormat.CUSTOM2,
                                     AccountFormat.COOKIE])

        # self.acc_db = Connection()
        self.btn_save.clicked.connect(self.on_add_account)
    
    def on_add_account(self):
        self._controller.db_signals.account_add.emit(self.txt_accounts.toPlainText(), self.cb_category.currentText(), self.cb_acc_format.currentText())
    


