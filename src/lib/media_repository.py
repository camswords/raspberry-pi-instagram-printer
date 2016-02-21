from database import Database
from media import Media
from support_team import SupportTeam

class MediaRepository:

    def __init__(self):
        self.database = Database()

    def update_latest(self, media):
        self.database.save("latest-media", media)

    def latest(self):
        if not self.database.has_key("latest-media"):
            return Media.EMPTY()

        return self.database.retrieve("latest-media")

    def new_media_ids(self):
        def is_new(media_id): self.database.retrieve(media_id).status == "new"
        return filter(is_new, self.database.keys());

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

        self.update_latest(media)
        self.save(media)

    def update(self, media):
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
