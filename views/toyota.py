from PySide6.QtWidgets import QWidget

from views.ui.pages.ui_toyota import Ui_Form

class Toyota(QWidget):
    def __init__(self):
        super(Toyota, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        