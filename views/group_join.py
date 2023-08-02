# pylint: disable=missing-module-docstring
from PySide6.QtWidgets import QWidget

from views.ui.group_join_ui import Ui_Form

class GroupJoin(QWidget):
    def __init__(self):
        super(GroupJoin, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)