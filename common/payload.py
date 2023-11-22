from dataclasses import dataclass, asdict


class BaseSetting():
    def __init__(self, idle_from, idle_to, threads) -> None:
        self.idle_from = idle_from
        self.idle_to = idle_to
        self.threads = threads


class SeedingSetting():
    def __init__(self, auto_getlink, posted_links, seedings, like, comment, contents, idle_from, idle_to, threads) -> None:
        self.auto_getlink = auto_getlink
        self.posted_links = posted_links
        self.seedings = seedings
        self.like = like
        self.comment = comment
        self.contents = contents
        self.idle_from = idle_from
        self.idle_to = idle_to
        self.threads = threads


class PostSetting(BaseSetting):
    def __init__(self, post_group_enable, post_count, type_group, contents, post_status_enable, background_enable, post_image_enable, md5_enalbe, photo_count, photos, idle_from, idle_to, threads) -> None:
        super().__init__(idle_from, idle_to, threads)
        self.post_group_enable = post_group_enable
        self.post_count = post_count
        self.type_group = type_group
        self.contents = contents
        self.post_status_enable = post_status_enable
        self.background_enable = background_enable
        self.post_image_enable = post_image_enable
        self.md5_enalbe = md5_enalbe
        self.photo_count = photo_count
        self.photos = photos


class AccountFormat:
    """Set of format account user input."""

    UID_PASS = "Uid | Pass"
    CUSTOM1 = "Uid | Pass | 2FA | Email | Pass Mail | Cookie | Token | Birthday"
    CUSTOM2 = "UID | Pass | 2FA | Cookie | Token | Email | Pass Mail | Birthday"
    DUYAN_5K = "DUYAN_5K"


@dataclass
class SocialGroupProfile():
    Group_Name: str
    Group_Link: str
    Category: str = None
    Numbers: str = None
    Details: str = None


