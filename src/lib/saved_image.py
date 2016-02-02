
class SavedImage:

    def __init__(self, media, file_path, media_repository):
        self.media = media
        self.file_path = file_path
        self.media_repository = media_repository

    def update_media_as_printing(self):
        self.media.status = "printing"
        self.media_repository.update(self.media)

    def update_media_as_printed(self):
        self.media.status = "printed"
        self.media_repository.update(self.media)

    def __str__(self):
        return "saved_image(%s, %s)" % (media.id, file_path)
