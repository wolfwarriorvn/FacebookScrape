# pylint: disable=comparison-with-itself
import sys
import signal
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon
from PySide6 import QtWidgets
from views.ui.main_window_ui import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QStandardPaths, QSettings

from controllers.main_ctrl import MainController
from model.model import Model

from views.dashboard import DashBoard
from views.account import Account
from views.proxy import Proxy
from views.group_view import GroupView
from views.group_join import GroupJoin
from views.group_scan import GroupScan
from views.tumbr import Tumbr
from views.youtube import Youtube
from database import Database
from setting import main_setting

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, model, main_controller):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Kungfu Seeding")
        self.setWindowIcon(QIcon(":/icon/views/icon/panda (1).png"))
        self._model = model
        self._main_controller = main_controller

        "Create a dick for menu button and tab windows"
        self.menu_btn_dict = {
            self.btn_dashboard: DashBoard(self._main_controller),
            self.btn_account: Account(self._main_controller),
            self.btn_proxy: Proxy(self._main_controller),
            self.btn_group_view: GroupView(self._main_controller),
            self.btn_youtube: Youtube(),
            self.btn_tumb: Tumbr()
        }
        "Show home window"
        self.show_home_window()

        "Connect signal and slot"
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.btn_dashboard.clicked.connect(self.show_home_window)
        self.btn_account.clicked.connect(self.show_selected_window)
        self.btn_proxy.clicked.connect(self.show_selected_window)
        self.btn_group_view.clicked.connect(self.show_selected_window)
        self.btn_tumb.clicked.connect(self.show_selected_window)
        self.btn_youtube.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.btn_dashboard.text())
        self.set_btn_checked(self.btn_dashboard)

        if result[0]:
            self.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.btn_dashboard.text()
            curIndex = self.tabWidget.addTab(self.menu_btn_dict[self.btn_dashboard], tab_title)
            self.tabWidget.setCurrentIndex(curIndex)
            self.tabWidget.setVisible(True)

    def set_btn_checked(self, btn):
        for button in self.menu_btn_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def close_tab(self, index):
        self.tabWidget.removeTab(index)

        if self.tabWidget.count() == 0:
            self.toolBox.setCurrentIndex(0)
            self.show_home_window()

    def show_selected_window(self):
        button = self.sender()
        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.tabWidget.addTab(
                self.menu_btn_dict[button], tab_title)
            self.tabWidget.setCurrentIndex(curIndex)
            self.tabWidget.setVisible(True)

    def open_tab_flag(self, btn_text):
        open_tab_count = self.tabWidget.count()

        for i in range(open_tab_count):
            tab_title = self.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i
            else:
                continue
        return False,


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        #connect mvc structure
        self.db = Database()
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainWindow(self.model, self.main_ctrl)
        self.main_view.showMaximized()



if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    app = App(sys.argv)
    sys.exit(app.exec())
    
