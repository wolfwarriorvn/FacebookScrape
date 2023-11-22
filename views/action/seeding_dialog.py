
from PySide6.QtWidgets import QWidget
from views.ui.dialog.seeding_ui import Ui_Seeding
from common.payload import SeedingSetting



class SeedingDialog(QWidget, Ui_Seeding):
    def __init__(self, controller, selected_uid):
        super(SeedingDialog, self).__init__()
        self._controller = controller
        self.selected_uid = selected_uid
        self.setupUi(self)
        self.btn_runnow_2.clicked.connect(self.on_seeding_action)

    def on_seeding_action(self):
        self._controller.task_signals.seeding_action.emit(self.selected_uid, SeedingSetting(
            self.ckb_autogetlink.isChecked(),
            self.txt_links.toPlainText().split('\n'),
            self.spin_seedings.value(),
            self.ckb_like.isChecked(),
            self.ckb_comment.isChecked(),
            self.le_contents.text(),
            self.sp_idle_from.value(),
            self.sp_idle_to.value(),
            self.sp_threads.value()
        ))
