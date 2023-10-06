from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.account_edit_menu_ui import Ui_Form
from views.connection import Connection
from controllers.main_ctrl import MainController
from controllers.main_ctrl import AccountInfo

class EditAccount(QWidget, Ui_Form):

    def __init__(self, controller: MainController, model, indexs, raw_idx):
        super(EditAccount, self).__init__()
        self._controller = controller
        self.model = model
        self.raw_idx = raw_idx
        self.setupUi(self)
        # self.btn_save.clicked.connect(self.on_btn_save)
        
        self._indexs = indexs  
        if len(indexs) == 1:
            self._controller.signals.get_account_completed.connect(self.on_get_account_completed)
            self._controller.get_account_info(indexs)
            self.le_uid.setEnabled(True)
        else:
            self.le_uid.setDisabled(True)

    def on_get_account_completed(self, account_info: AccountInfo):
        self.le_uid.setText(account_info.uid)
        self.le_pass.setText(account_info.pw)
        self.le_proxy.setText(str(account_info.proxy))
            
    def on_save_account_completed(self):
        self.close()