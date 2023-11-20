from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QObject
from views.ui.group_add_ui import Ui_GroupAdd
from views.connection import Connection
from common.payload import AccountFormat
from views.messages import show_error_message

class GroupAdd(QWidget, Ui_GroupAdd):
    add_completed = Signal()
    def __init__(self, controller):
        super(GroupAdd, self).__init__()
        self._controller = controller
        self.setupUi(self)
        self.btn_save.clicked.connect(self.on_add_group)
        

    def on_add_group(self):
        request = {
            'table' : 'groups',
            'data': [{
                'Group_ID': self.uid.text(),
                'Group_Name': self.group_name.text(),
                'Approve': self.approve.toPlainText(),
                'Decline': self.decline.toPlainText()
            }],
        }
        self._controller.database_operation.emit('insert', self.on_add_groups_reponse, request)

    def on_add_groups_reponse(self, result, error):
        if error:
            show_error_message(error, self)
        else:
            self.add_completed.emit()
            self.close()
        