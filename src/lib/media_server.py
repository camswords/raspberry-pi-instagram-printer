from instagram.client import InstagramAPI
from database import Database
import os
import time
import traceback
from timeout import timeout

class MediaServer:

    def __init__(self):
        self.client_id = client_id=os.environ['INSTAGRAM_CLIENT_ID']
        self.client_secret = os.environ['INSTAGRAM_CLIENT_SECRET']
        self.hashtag = os.environ['INSTAGRAM_HASHTAG']

        self.api = InstagramAPI(client_id = self.client_id, client_secret = self.client_secret)

        self.database = Database()

        if not self.database.has_key("most-recent-id"):
            self.database.save("most-recent-id", 0)

        if not self.database.has_key("downloaded-media"):
            self.database.save("downloaded-media", [])

    def persist(self, medias):
        for media in medias:
            self.database.save("most-recent-id", media.id)
            downloaded = self.database.retrieve("downloaded-media")

            if not self.database.has_key(media.id):
                downloaded.insert(0, media.id)
                self.database.save("downloaded-media", downloaded)
                self.database.save(media.id, {"url": media.images['standard_resolution'].url})

    @timeout(30)
    def fetch(self):
        try:
            recent_media = self.api.tag_recent_media(1, self.database.retrieve("most-recent-id"), self.hashtag)
            self.persist(recent_media[0])
        except:
            exceptiondata = traceback.format_exc().splitlines()
            print "failed to fetch media from instagram, error was %s" % (exceptiondata[-1])


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
