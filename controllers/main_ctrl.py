from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot

class MainController(QObject):
    sg_wrong_user_input = Signal()
    def __init__(self, model):
        super().__init__()
        self._model = model

    def add_new_account(self):
        print("Add new account kia")
        print("sleep done")
        self.sg_wrong_user_input.emit()