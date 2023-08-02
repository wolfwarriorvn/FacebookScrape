from PySide6.QtWidgets import QWidget

from views.ui.group_view_ui import Ui_Form

class GroupView(QWidget):
    def __init__(self):
        super(GroupView, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        