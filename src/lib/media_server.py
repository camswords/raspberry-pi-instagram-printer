from instagram.client import InstagramAPI
from repository import Repository
import os
import time

class MediaServer:

    def __init__(self):
        self.client_id = client_id=os.environ['INSTAGRAM_CLIENT_ID']
        self.client_secret = os.environ['INSTAGRAM_CLIENT_SECRET']
        self.hashtag = os.environ['INSTAGRAM_HASHTAG']

        self.api = InstagramAPI(client_id = self.client_id, client_secret = self.client_secret)

        self.database = Repository()

        if not self.database.has_key("most-recent-id"):
            self.database.save("most-recent-id", 0)

        if not self.database.has_key("downloaded-media"):
            self.database.save("downloaded-media", [])

    def fetch(self):
        recent_media = self.api.tag_recent_media(1, self.database.retrieve("most-recent-id"), self.hashtag)

        for media in recent_media[0]:
            self.database.save("most-recent-id", media.id)
            downloaded = self.database.retrieve("downloaded-media")

            if not self.database.has_key(media.id):
                downloaded.insert(0, media.id)
                self.database.save("downloaded-media", downloaded)
                self.database.save(media.id, {"url": media.images['standard_resolution'].url})

    def hasNext(self):
        downloaded = self.database.retrieve("downloaded-media")
        return len(downloaded) > 0

    def next(self):
        while not self.hasNext():
            self.fetch()

            # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
            time.sleep(5)

        downloaded = self.database.retrieve("downloaded-media")
        mediaId = downloaded.pop()
        self.database.save("downloaded-media", downloaded)

        return self.database.retrieve(mediaId)
