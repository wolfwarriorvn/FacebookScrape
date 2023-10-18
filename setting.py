from PySide6.QtCore import QStandardPaths, QSettings
import os
import re
import glob
from constants import CHROME_PROFILES
class Setting:
    def __init__(self) -> None:
        self.app_name = "KungFB"
        self.chrome_driver = ""
        self.chrome_profiles = ""
        self.settings = QSettings(self.app_name, 'app')

        self.document_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation).replace("/", "\\")
        self.root_app = f'{self.document_dir}\\{self.app_name}'

        if not os.path.exists(self.root_app):
            self.init_default_dir()

        self.chrome_driver = self.settings.value('chromeDriver')
        self.chrome_profiles = self.settings.value('chromeProfiles')
        self.proxy = self.settings.value('proxy')
        self.database = self.settings.value('database')

    def init_default_dir(self):
        chrome_driver_dir = f"{self.root_app}\\chromeDriver"
        chrome_driver = f"{self.root_app}\\chromeDriver\\chromedriver.exe"
        chrome_profiles = f"{self.root_app}\\chromeProfiles\\"
        proxy_dir = f"{self.root_app}\\proxy\\"
        database = f"{self.root_app}\\{self.app_name}.db"
        os.makedirs(self.root_app)
        os.makedirs(chrome_driver_dir)
        os.makedirs(chrome_profiles)
        os.makedirs(proxy_dir)
        self.settings.setValue('chromeDriver', chrome_driver)
        self.settings.setValue('chromeProfiles', chrome_profiles)
        self.settings.setValue('proxy', proxy_dir)
        self.settings.setValue('database', database)
    

main_setting = Setting()