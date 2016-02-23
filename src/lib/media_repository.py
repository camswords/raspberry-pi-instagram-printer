from database import Database
from media import Media
from support_team import SupportTeam

class MediaRepository:

    def __init__(self):
        self.database = Database()

    def latest_media_id(self):
        if not self.database.has_key("latest-media"):
            return "0"

        return self.database.retrieve("latest-media")

    def is_new(self, media_id):
        return self.database.retrieve(media_id)["status"] == "new"

    def new_media_ids(self):
        def not_latest(key): return key != "latest-media"
        media_ids = filter(not_latest, self.database.keys())
        return filter(self.is_new, media_ids)

    def has_available_media(self):
        return len(self.new_media_ids()) > 0

    def peek_available_media(self):
        new_media_ids = self.new_media_ids()

        if len(new_media_ids) == 0:
            raise RuntimeError("failed to peek new media as there is no new media to peek")

        return self.retrieve(new_media_ids.pop())

    def create(self, media):
        if self.database.has_key(media.id):
            return media

        self.database.save("latest-media", media.id)
        self.save(media)

    def has_media_with_id(self, media_id):
        return self.database.has_key(media_id)

    def update_media_status(self, media, status):
        media.status = status
        self.save(media)

    def save(self, media):
        self.database.save(media.id, { "id": media.id, "url": media.url, "status": media.status })
        SupportTeam.notify("%s - saved to database with status %s" % (media.id, media.status))
        return media

    def retrieve(self, media_id):
        if not self.database.has_key(media_id):
            raise RuntimeError("Failed to retrieve media with id %s, it was not found in the database." % media_id)

        marshalled_media = self.database.retrieve(media_id)
        return Media(id = marshalled_media["id"], url = marshalled_media["url"], status = marshalled_media["status"])

    def __str__(self):
        return "media repository has %s" % self.database
