
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal, QObject
from PySide6 import QtCore, QtGui, QtWidgets
from views.ui.dialog.dialog_scan_posted_history_ui import Ui_DialogScanPost
import glob
from PySide6.QtSql import QSqlTableModel
from views.ui.dialog.post_ui import Ui_Post
from views.connection import Connection
from lib_type import PostSetting


from views.ui.dialog.dialog_scan_posted_history_ui import Ui_DialogScanPost
from views.ui.dialog.seeding_ui import Ui_Seeding
from views.connection import Connection
from lib_type import SeedingSetting

class ScanPostDialog(QWidget, Ui_DialogScanPost):
    trigger = Signal()

    def __init__(self, controller, selected_uid):
        super(ScanPostDialog, self).__init__()
        self._controller = controller
        self.selected_uid = selected_uid
        self.setupUi(self)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_runnow.clicked.connect(self.on_scan_post_history)
    
    def on_scan_post_history(self):
        self._controller.signals.scan_post_history.emit(self.selected_uid, self.scrolls.value(), self.syncs.value())
        self.close()