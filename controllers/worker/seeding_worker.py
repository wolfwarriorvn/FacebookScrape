from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange


class SeedingWorker(BaseWorker):
    def __init__(self, available_links, settings, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)
        self.available_links = available_links
        self.settings = settings

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return

            for href in self.available_links:
                if self.settings.like:
                    if self.fb_scraper.like_url_posted(href):
                        self.signals.seeding_status.emit(self._uid, href, 'Liked')
                if self.settings.comment:
                    pass

                sleep(randrange(self.settings.idle_from, self.settings.idle_to))

            self.signals.update_message.emit(self._uid, 'Seeding completed!!!')
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