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

    def recover_printer(self):
        print "recover printer - cancelling all jobs"
        self.system.printer().cancel_all_jobs()

        print "recover printer - restarting printer (90 secs)"
        # deal with failure: restart printer
        time.sleep(90)

    def start(self):
        self.running = True
        self.run()

    def run(self):
        consecutive_errors = 0

        if self.system.has_printer():
            print "using system default printer %s" % self.system.printer().printer_name

        while self.running == True:
            try:

                if consecutive_errors > 20:
                    consecutive_errors = 0
                    self.recover_printer()
                    continue

                if not self.system.printer().ready_to_print():
                    consecutive_errors += 1
                    print "failure - system is not ready to print, skipping. status is %s" % self.system.printer().status()
                    continue

                if not self.system.has_printer():
                    # intentionally not a 'consecutive_error', restarting a printer won't help here.
                    print "failure - system has no default printer, skipping print"
                    continue

                if self.system.has_jobs():
                    print "failure - system has incomplete jobs"
                    self.recover_printer()
                    continue

                consecutive_errors = 0
                self.system.printer().send(self.saved_images.next())

            except:
                consecutive_errors += 1
                exceptiondata = traceback.format_exc().splitlines()
                print "failure - uncaught error, %s. skipping print" % (exceptiondata[-1])

            finally:
                sys.stdout.flush()
                time.sleep(5)

    def stop(self, signum, frame):
        self.running = False

if __name__ == '__main__':
    InstagramPrinter().start()
