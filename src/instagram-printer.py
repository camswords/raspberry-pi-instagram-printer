from lib.media_server import MediaServer
from lib.media_repository import MediaRepository
from lib.saved_images import SavedImages
import time
import sys
import traceback
import signal


class InstagramPrinter:

    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.running = False
        self.media_repository = MediaRepository()
        self.media_server = MediaServer(self.media_repository)
        self.saved_images = SavedImages(self.media_server)

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running == True:
            try:
                saved_image = self.saved_images.next()
                print "%s - printed" % saved_image.media.id
                self.media_repository.save(saved_image.media.as_printed())

            except:
                exceptiondata = traceback.format_exc().splitlines()
                print "failed to fetch media from instagram, error was %s" % (exceptiondata[-1])

            finally:
                sys.stdout.flush()
                time.sleep(3)

    def stop(self, signum, frame):
        self.running = False



if __name__ == '__main__':
    InstagramPrinter().start()
