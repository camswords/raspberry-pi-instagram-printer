
class FileSystemImage:

    def __init__(self, media, file_path):
        self.media = media
        self.file_path = file_path

    def __str__(self):
        return "saved_image(%s, %s)" % (self.media.id, self.file_path)
