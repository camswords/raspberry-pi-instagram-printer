
class Media:

    def __init__(self, id, url, status):
        self.id = id
        self.url = url
        self.status = status

    def is_new(self):
        return self.status == "new"

    def as_printed(self):
        return Media(id = self.id, url = self.url, status = "sent-to-print")

    def __str__(self):
        return "media(%s, %s, %s)" % (self.id, self.status, self.url)

    @staticmethod
    def EMPTY():
        return Media(id = "0", url = "http://not-found", status = "new")
