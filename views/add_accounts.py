from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.pages.ui_addmenu import Ui_Addaccount
from views.connection import Connection

class AddAccount(QWidget, Ui_Addaccount):
    trigger = Signal()
    def __init__(self, controller):
        super(AddAccount, self).__init__()
        self._controller = controller
        self.setupUi(self)
        # self.acc_db = Connection()
        self.btn_save.clicked.connect(self._controller.add_new_account)
        self._controller.sg_wrong_user_input.connect(self.on_list_changed)

    def on_list_changed(self):
        print("update gui")
        self.lb_show_msg.setText("Nhập lại không đúng")
    # def save_account(self):
    #     accs_raw = self.txt_accounts.toPlainText().splitlines()
    #     for acc in accs_raw:
    #         accdetail = acc.split('|')
    #         self.acc_db.add_new_account_query(accdetail[0], accdetail[1], accdetail[2])
    #     # Emit the signal.
    #     self.trigger.emit()

