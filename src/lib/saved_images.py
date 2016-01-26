from media_server import MediaServer
from saved_image import SavedImage
from timeout import timeout
from subprocess import check_call

class SavedImages:

    def __init__(self, media_server):
        self.media_server = media_server

    @timeout(30)
    def save_to_filesystem(self, media):
        check_call(["rm", "-rf", "/tmp/image.jpg"])
        check_call(["wget", media.url, "--quiet", "-O", "/tmp/image.jpg"])

    def next(self):
        media = self.media_server.next()
        self.save_to_filesystem(media)
        print("%s - saved to file system at /tmp/image.jpg" % media.id)
        return SavedImage(media, "/tmp/image.jpg")
