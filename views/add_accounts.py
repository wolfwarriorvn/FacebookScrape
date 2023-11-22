from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.addmenu_ui import Ui_Addaccount
from views.connection import Connection
from common.payload import AccountFormat
from PySide6.QtWidgets import QErrorMessage,QMessageBox
from views.messages import show_error_message
from model.db_model import Op
from model.request import InsertRequest

class AccountFields:
    UID_PASS = ["UserID", "Password"]
    CUSTOM2 = ["UserID", "Password", "Code2FA", "Cookie", "Token", "Email", "PassEmail", "Birthday"]
    CUSTOM1 = ["UserID", "Password", "Code2FA", "Email", "PassEmail", "Cookie", "Token", "Birthday"]
    DUYAN_5K = ["UserID", "Password", "Code2FA", "Email", "PassEmail", "", "Birthday", "Cookie", "Token"]

    @classmethod
    def get_formats(cls):
        formats = []
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, list):
                formats.append('|'.join(attr))
        return formats
    @classmethod
    def get_field_keys_from_format_string(cls, format_string):
        print('format_string')
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, list) and '|'.join(attr) == format_string:
                return attr
        raise ValueError(f"Format string '{format_string}' not found")


class AddAccount(QWidget, Ui_Addaccount):
    added_new_account = Signal()

    def __init__(self, controller):
        super(AddAccount, self).__init__()
        self._controller = controller
        self.setupUi(self)
        self.table_name = 'accounts'
        self.cb_acc_format.addItems(AccountFields.get_formats())

        # self.acc_db = Connection()
        self.btn_save.clicked.connect(self.on_add_account)
    
    def parse_account_line(self, account_line, field_keys):
        account_data = account_line.split('|')
        return dict(zip(field_keys, account_data))
    
    def process_accounts(self, accounts_lines, format_string):
        accounts_list = []

        try:
            field_keys = AccountFields.get_field_keys_from_format_string(format_string)
            print(field_keys)
            for accounts_line in accounts_lines:
                parsed_line = self.parse_account_line(accounts_line, field_keys)
                accounts_list.append(parsed_line)
                
        except Exception as ex:
            print(f'Error with process data: {ex}')
        return accounts_list

    def on_add_account(self):
        accounts_lines = self.txt_accounts.toPlainText().splitlines()
        print(accounts_lines)
        format_string = self.cb_acc_format.currentText()
        if not accounts_lines:
            show_error_message("Please Input valid accounts!", self)
            return
        accounts = self.process_accounts(accounts_lines, format_string)

        request = InsertRequest(
            table=self.table_name,
            data=accounts
        )
        self._controller.database_operation.emit(Op.INSERT, self.on_add_account_response, request)

    def on_add_account_response(self, succes, error):
        if error:
            show_error_message(f"Error: {error}", self)
        else:
            self.added_new_account.emit()
            self.close()
    


