from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange
import random
from common.payload import PostSetting
import logging

class PostGroupSignals(BaseSignals):
    posted_group_completed = Signal(str,str, str)

class PostGroupWorker(BaseWorker):
    def __init__(self, semaphore, user_id, group_links, settings: PostSetting) -> None:
        super().__init__(semaphore, user_id)
        self.group_links = group_links
        self.settings = settings
        self.signals = PostGroupSignals()

    def setup_before_execution(self, db_manager, ui_signals):
        super().setup_before_execution(db_manager, ui_signals)
        pageID = db_manager.get_account_pageid(self.user_id)
        self.activeID = self.user_id if pageID == '' else pageID

    def post_completed(self, pageid, group_link, status):
        try:
            self.db_manager.update_group_posted_status(pageid, group_link, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        super().connect_signals()
        self.signals.posted_group_completed.connect(self.post_completed)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return
            
            for index, group_link in enumerate(self.group_links, 1):
                content = random.choices(self.settings.contents)
                photo = []
                if self.settings.post_image_enable:
                    photo = random.sample(sorted(self.settings.photos), self.settings.photo_count)

                logging.info(photo, content)

                status = self.fb_scraper.post_group(group_link, content, photo)

                status = 'Pending' if status else 'Error'
                self.signals.posted_group_completed.emit( self.activeID, group_link, status)

                self.signals.update_message.emit(self._uid, f'Post Group {index:02}/{len(self.group_links):02} - {status}')
                if status:
                    sleep(random.randint(self.settings.idle_from, self.settings.idle_to))

            self.signals.update_status.emit(self._uid, 'Free')

        except NoLoginException:
            self.signals.update_status.emit(self._uid, 'Unlogin')
        except CheckpointException as ex:
            self.signals.update_status.emit(self._uid, f'{ex}')
        except :
            self.signals.update_status.emit(self._uid, 'Free')
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')

        finally:
            self.exit()