from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange
import random

class SeedingSignals(BaseSignals):
    seeding_status = Signal(str, str, str)

class SeedingWorker(BaseWorker):
    def __init__(self, semaphore, user_id, settings) -> None:
        super().__init__(semaphore, user_id)
        self.settings = settings
        self.signals = SeedingSignals()

    def setup_before_execution(self, db_manager, ui_signals):
        super().setup_before_execution(db_manager, ui_signals)
        if self.settings.auto_getlink:
            self.settings.posted_links = db_manager.get_post_approved_link()
        if self.settings.auto_getlink:
            liked_links = db_manager.get_seeding_liked_link(self._uid)
            set_available_links = set(
                self.settings.posted_links).difference(set(liked_links))
            if len(set_available_links) < self.settings.seedings:
                raise ValueError(f"Không đủ link để like. Số link còn lại: {len(set_available_links)}")

            self.available_links = random.sample(
                sorted(set_available_links), self.settings.seedings)
        else:
            self.available_links = self.settings.posted_links

    def on_update_seeding_status(self, uid, href, action):
        try:
            if action == 'Liked':
                self.db_manager.update_post_liked_counts(href)
            elif action == 'Commented':
                self.db_manager.update_post_commented_counts(href)

            self.db_manager.add_seeding_action(uid, href, action)
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        super().connect_signals()
        self.signals.seeding_status.connect(self.on_update_seeding_status)
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