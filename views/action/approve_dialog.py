from PySide6.QtWidgets import QWidget
from views.ui.dialog.approve_ui import Ui_Approve
from common.payload import ThreadAprovalPayload,GroupApprovalSettings

class ApproveDialog(QWidget, Ui_Approve):
    def __init__(self, controller, uids):
        super(ApproveDialog, self).__init__()
        self.controller = controller
        self.uids = uids
        self.setupUi(self)
        self.btn_start.clicked.connect(self.on_start)

    def on_start(self):
        group_setting = []
        for setting in self.groups_settings.toPlainText().splitlines():
            uid, approve, decline = setting.split('|')
            group_setting.append(GroupApprovalSettings(uid, approve, decline))
        
        self.controller.task_signals.approval.emit(self.uids, ThreadAprovalPayload(post_count=self.num_posts.value(), approval_settings=group_setting))
        self.close()
