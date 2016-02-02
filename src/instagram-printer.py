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
        self.media_repository = MediaRepository()
        self.media_server = MediaServer(self.media_repository)
        self.saved_images = SavedImages(self.media_server, self.media_repository)

    def start(self):
        self.running = True
        self.run()

    def run(self):

        if self.system.has_printer():
            print "using system default printer %s" % self.system.printer().printer_name

        while self.running == True:
            try:

                print "printer", self.printer()

                if not self.system.has_printer():
                    print "failure - system has no default printer, skipping print"
                    continue

                if self.system.has_jobs():
                    print "failure - system has incomplete jobs, cancelling all of them"
                    self.system.printer().cancel_all_jobs()

                    print "failure - restarting printer (90 secs)"
                    # deal with failure: restart printer
                    time.sleep(90)
                    continue

                self.system.printer().send(self.saved_images.next())

            except:
                exceptiondata = traceback.format_exc().splitlines()
                print "failure - uncaught error, %s. skipping print" % (exceptiondata[-1])

            finally:
                sys.stdout.flush()
                time.sleep(5)

    def stop(self, signum, frame):
        self.running = False

if __name__ == '__main__':
    InstagramPrinter().start()
