from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from PyQt6.QtCore import QThreadPool

from PySide6.QtSql import QSqlTableModel
from model.model import Model
from time import sleep
from controllers.worker import FacebookWorker

class AccountInfo:
    def __init__(self,uid, pw, proxy) -> None:
        self.uid = uid
        self.pw = pw
        self.proxy = proxy

class MySignals(QObject):
    #Edit account signal
    get_account_completed = Signal(object)
    save_account_completed = Signal()

    wrong_user_input = Signal()
    table_get_completed = Signal(object)
    table_on_load = Signal()
    add_user_completed = Signal()
    add_user_error = Signal()


class MainController(QObject):
    # sg_wrong_user_input = Signal()
    signals = MySignals()

    def __init__(self, model: Model):
        super().__init__()
        self._model = model
        self.signals.table_on_load.connect(self.update_table_view)
    

    def open_chrome(self, selected_ids):
        for id in selected_ids:
            uid, pw, proxy = self._model.get_account_info(id)
            proxy_extension = self._model.get_proxy_extension(proxy)

            print("proxy_extension: ", proxy_extension)

            pool = QThreadPool.globalInstance()
            worker = FacebookWorker(uid, pw, proxy_extension)
            pool.start(worker)


    Slot(str)
    def get_account_info(self, indexs):
        # sleep(5)
        if len(indexs) == 1:
            uid, pw, proxy =self._model.get_account_info(indexs[0])
            self.signals.get_account_completed.emit(AccountInfo(uid, pw, proxy))

    def save_account_info(self, index, account_info):
        self._model.save_account_info(account_info, index)
        self.signals.save_account_completed.emit()

    Slot(str)
    def add_new_account(self, raw_input):
        accs_raw = raw_input.splitlines()
        try:
            for acc in accs_raw:
                if len(acc.split('|')) == 2:
                    uid, pwd = acc.split('|')
                    self._model.add_new_account(uid, pwd)
                    self.signals.add_user_completed.emit()
                elif len(acc.split('|')) == 3:
                    uid, pwd, proxy_id = acc.split('|')
                    self._model.add_new_account(uid, pwd, proxy_id)
                    self.signals.add_user_completed.emit()
                else:
                    print("Input khong dung format")
                    self.signals.add_user_error.emit()
                
        except Exception as e:
            print("Error is {}".format(e))
            self.signals.add_user_error.emit()

    Slot()
    def update_table_view(self):
        self.signals.table_get_completed.emit(self._model._get_table())

    Slot()
    def update_account(self):
        pass

    Slot(object,list)
    def delete_account(self, tb_model, acc_index):
        ids = []
        for index in sorted(acc_index):
            id = str(tb_model.data(index))
            ids.append(id)
        self._model.delete_account(ids)
        self.signals.table_get_completed.emit(self._model._get_table())
