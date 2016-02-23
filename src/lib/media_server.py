from instagram.client import InstagramAPI
from media_repository import MediaRepository
from support_team import SupportTeam
from media import Media
import os
import time
from timeout import timeout

class MediaServer:

    def __init__(self, media_repository):
        self.client_id = client_id=os.environ["INSTAGRAM_CLIENT_ID"]
        self.client_secret = os.environ["INSTAGRAM_CLIENT_SECRET"]
        self.hashtag = os.environ["INSTAGRAM_HASHTAG"]

        self.api = InstagramAPI(client_id = self.client_id, client_secret = self.client_secret)
        self.media_repository = media_repository

    @timeout(30)
    def fetch(self):
        SupportTeam.notify("finding instagram media for #%s" % self.hashtag)
        latest_media_id = self.media_repository.latest_media_id()
        recent_media = self.api.tag_recent_media(5, latest_media_id, self.hashtag)

        for instagram_media in recent_media[0]:
            if not self.media_repository.has_media_with_id(instagram_media.id):
                media = Media(id = instagram_media.id, url = str(instagram_media.images['standard_resolution'].url), status = "new")
                SupportTeam.notify("%s - new media %s" % (media.id, media.url))
                self.media_repository.create(media)

    def next(self):
        if not self.media_repository.has_available_media():
            self.fetch()

        if self.media_repository.has_available_media():
            return self.media_repository.peek_available_media()

        return None
