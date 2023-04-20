from PySide6.QtWidgets import QWidget

from views.ui.pages.ui_lexus import Ui_Form

class Lexus(QWidget):
    def __init__(self):
        super(Lexus, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        