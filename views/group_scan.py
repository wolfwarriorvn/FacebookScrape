from PySide6.QtWidgets import QWidget

from views.ui.group_scan_ui import Ui_Form

class GroupScan(QWidget):
    def __init__(self):
        super(GroupScan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        