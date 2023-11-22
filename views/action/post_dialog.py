
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal, QObject
from PySide6 import QtCore, QtGui, QtWidgets
from views.ui.dialog.dialog_scan_posted_history_ui import Ui_DialogScanPost
import glob
from PySide6.QtSql import QSqlTableModel
from views.ui.dialog.post_ui import Ui_Post
from views.connection import Connection
from common.payload import PostSetting
from model.request import SelectRequest
from model.db_model import Op

class PostDialog(QWidget, Ui_Post):
    def __init__(self, controller, selected_uid):
        super(PostDialog, self).__init__()
        self._controller = controller
        self.selected_uid = selected_uid
        self.setupUi(self)
        self.btn_runnow.clicked.connect(self.on_post)

        self.groups_model = QSqlTableModel(self)
        self.groups_model.setQuery('SELECT DISTINCT Type FROM groups_tita')
        self.cb_group_type.currentTextChanged.connect(self.on_current_text_changed)
        self.cb_group_type.setModel(self.groups_model)
        self.cb_group_type.installEventFilter(self)
        self.btn_select_image.clicked.connect(self.choose_image_path)
        self.triger_get_free_group(self.cb_group_type.currentText())
        

    def triger_get_free_group(self, type):
        select_request = SelectRequest(
            table='groups_tita',
            columns='Group_Link',
            conditions="Type = :type and Category='Công khai ' and   Interact='Page' and (Status IS NULL or Status = 'Free')",
            parameters={'type': type}
        )

        self._controller.database_operation.emit(Op.SELECT, self.on_get_groups_reponse, select_request)

    def on_get_groups_reponse(self, result, error):
        if error:
            print("on_get_groups_reponse error: ", error)
        else:
            
            counts = len(result) if result else 0
            self.le_free_groups.setText('Rãnh: {} groups'.format(counts))
            

    def on_current_text_changed(self):
        group_type = self.cb_group_type.currentText()
        self.triger_get_free_group(group_type)

        if group_type == 'DEP':
            self.le_image_path.setText(r'H:\fbtools\image\dep')
        elif group_type == 'MAY':
            self.le_image_path.setText(r'H:\fbtools\image\may')     

    def choose_image_path(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        uppath = folder_path.replace("/", '\\')
        self.le_image_path.setText(uppath)

    def eventFilter(self, target, event):
        if target == self.cb_group_type and event.type() == QtCore.QEvent.MouseButtonPress:
            self.groups_model.setQuery('SELECT DISTINCT Type FROM groups_tita')
            self.cb_group_type.setModel(self.groups_model)
        return False

    def on_post(self):
        contents = self.txt_contents.toPlainText().split('|')
        photos = glob.glob( self.le_image_path.text() + '\*.jpg')

        if contents[0] == '':
            QtWidgets.QMessageBox.warning(None, "Kiểm tra lại nội dung.", QtWidgets.QMessageBox.Cancel)
            return
        if len(photos) < self.sp_image_count.value():
            QtWidgets.QMessageBox.warning(None, "Không có hình để đăng.", QtWidgets.QMessageBox.Cancel)
            return
        
        setting = PostSetting(
            self.ckb_post_to_groups.isChecked(),
            self.sp_numposts.value(),
            self.cb_group_type.currentText(),
            contents,
            self.rb_status.isChecked(),
            self.chb_background_enable.isChecked(),
            self.rb_image_enable.isChecked(),
            self.chb_md5_enable.isChecked(),
            self.sp_image_count.value(),
            photos,
            self.sp_idle_from.value(),
            self.sp_idle_to.value(),
            self.sp_threads.value()
        )
        self._controller.task_signals.post_event.emit(self.selected_uid, setting)
        self.close()
