# pylint: disable=missing-module-docstring
from PySide6.QtWidgets import QWidget

from views.ui.pages.ui_mazda import Ui_Form

class Mazda(QWidget):
    def __init__(self):
        super(Mazda, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)