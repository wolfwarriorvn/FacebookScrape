
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Signal, QObject
from PySide6 import QtCore, QtGui, QtWidgets
from views.ui.dialog.dialog_scan_posted_history_ui import Ui_DialogScanPost
import glob
from PySide6.QtSql import QSqlTableModel
from views.ui.dialog.post_ui import Ui_Post
from views.connection import Connection
from lib_type import PostSetting


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
        self._controller.db_signals.get_free_group_completed.connect(self.update_label_free_groups)
        self._controller.db_signals.get_free_group.emit(self.cb_group_type.currentText())

    def on_current_text_changed(self):
        group_type = self.cb_group_type.currentText()
        self._controller.db_signals.get_free_group.emit(group_type)

        if group_type == 'DEP':
            self.le_image_path.setText(r'H:\fbtools\image\dep')
        elif group_type == 'MAY':
            self.le_image_path.setText(r'H:\fbtools\image\may')
        
    def update_label_free_groups(self, counts):
        self.le_free_groups.setText('Rãnh: {} groups'.format(counts))
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
            print("Kiểm tra lại nội dung")
            return
        if len(photos) < self.sp_image_count.value():
            print("Kiểm ra lại thư mục hình")
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
        # print(', '.join("%s: %s" % item for item in vars(setting).items()))
        self._controller.signals.post_event.emit(self.selected_uid, setting)

        self.close()
