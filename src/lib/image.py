from media_server import MediaServer
from timeout import timeout
from subprocess import check_call

class Image:

    def __init__(self):
        self.media = MediaServer()

    @timeout(30)
    def save_to_filesystem(self, media_item):
        check_call(["rm", "-rf", "/tmp/image.jpg"])
        check_call(["wget", media_item["url"], "--quiet", "-O", "/tmp/image.jpg"])

    def next(self):
        self.save_to_filesystem(self.media.next())
        return "/tmp/image.jpg"
