#!/usr/bin/env python
from lib.system import System
from lib.media_repository import MediaRepository
from lib.media_server import MediaServer
from lib.saved_images import SavedImages
import signal
import traceback
import sys
import time

class InstagramPrinter:

    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.running = False
        self.system = System()
        self.mediaRepository = MediaRepository()
        self.mediaServer = MediaServer(self.mediaRepository)
        self.savedImages = SavedImages(self.mediaServer)

    def start(self):
        self.running = True
        self.run()

    def run(self):

        if self.system.has_printer():
            print "using system default printer %s" % self.system.printer().printer_name

        while self.running == True:
            try:

                if not self.system.has_printer():
                    print "system has no default printer, skipping print"
                    continue

                if self.system.has_jobs():
                    print "system has incomplete jobs, dealing with failure"
                    print "cancelling all pending print jobs"
                    self.system.printer().cancel_all_jobs()

                    print "restarting printer"
                    # deal with failure: restart printer
                    print "waiting for printer to restart"
                    time.sleep(90)
                    continue

                # save print job to the media repository
                job = self.system.printer().send(self.savedImages.next())
                print "%s successfully sent to printer" % job

            except:
                exceptiondata = traceback.format_exc().splitlines()
                print "failed to instagram print, error was %s. skipping print" % (exceptiondata[-1])

            finally:
                sys.stdout.flush()
                time.sleep(5)

    def stop(self, signum, frame):
        self.running = False

if __name__ == '__main__':
    InstagramPrinter().start()
