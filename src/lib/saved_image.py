
class SavedImage:

    def __init__(self, media, file_path):
        self.media = media
        self.file_path = file_path

    def __str__(self):
        return "saved_image(%s, %s)" % (media.id, file_path)
