from instagram.client import InstagramAPI
from media_repository import MediaRepository
from media import Media
import os
import time
from timeout import timeout

class MediaServer:

    def __init__(self, media_repository):
        self.client_id = client_id=os.environ['INSTAGRAM_CLIENT_ID']
        self.client_secret = os.environ['INSTAGRAM_CLIENT_SECRET']
        self.hashtag = os.environ['INSTAGRAM_HASHTAG']

        self.api = InstagramAPI(client_id = self.client_id, client_secret = self.client_secret)
        self.media_repository = media_repository

    @timeout(30)
    def fetch(self):
        latest_media = self.media_repository.latest()
        recent_media = self.api.tag_recent_media(5, latest_media.id, self.hashtag)

        for instagram_media in recent_media[0]:
            media = Media(id = instagram_media.id, url = str(instagram_media.images['standard_resolution'].url), status = "new")
            print("%s - fetched from instagram, url is %s" % (media.id, media.url))
            self.media_repository.create(media)

    def next(self):
        while not self.media_repository.has_available_media():
            self.fetch()

            # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
            time.sleep(5)

        return self.media_repository.peek_available_media()
