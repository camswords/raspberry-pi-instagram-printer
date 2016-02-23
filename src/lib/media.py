from file_system_image import FileSystemImage
from support_team import SupportTeam
from timeout import timeout
from subprocess import check_call

class Media:

    def __init__(self, id, url, status):
        self.id = id
        self.url = url
        self.status = status

    @timeout(30)
    def download(self):
        check_call(["rm", "-rf", "/tmp/image-downloading.jpg"])
        check_call(["wget", self.url, "--quiet", "-O", "/tmp/image-downloading.jpg"])
        check_call(["cp", "-f", "/tmp/image-downloading.jpg", "/tmp/image.jpg"])
        SupportTeam.notify("%s - downloaded to /tmp/image.jpg" % self.id)
        return FileSystemImage(self, "/tmp/image.jpg")

    def __str__(self):
        return "media(%s, %s, %s)" % (self.id, self.status, self.url)
