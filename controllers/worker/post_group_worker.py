from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange
import random
from common.payload import PostSetting
import logging

class PostGroupWorker(BaseWorker):
    def __init__(self, group_links, settings: PostSetting, page_id, semaphore_id, account) -> None:
        super().__init__(semaphore_id,account)
        self.page_id = page_id
        self.group_links = group_links
        self.settings = settings

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return
            
            for index, group_link in enumerate(self.group_links, 1):
                content = random.choices(self.settings.contents)
                photo = random.sample(sorted(self.settings.photos), self.settings.photo_count)

                logging.info(photo, content)

                status = self.fb_scraper.post_group(group_link, content, photo)

                status = 'Pending' if status else 'Error'
                self.signals.posted_group_completed.emit( self.page_id, group_link, status)

                self.signals.update_message.emit(self._uid, f'Post Group {index:02}/{len(self.group_links):02} - {status}')
                if status:
                    sleep(random.randint(self.settings.idle_from, self.settings.threads))

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