#!/usr/bin/env python
from lib.system import System
from lib.media_repository import MediaRepository
from lib.media_server import MediaServer
from lib.saved_images import SavedImages
from lib.power import Power
from lib.support_team import SupportTeam
import signal
import traceback
import time
import os

class InstagramPrinter:

    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.running = False
        self.system = System()
        self.media_repository = MediaRepository()
        self.media_server = MediaServer(self.media_repository)
        self.saved_images = SavedImages(self.media_server, self.media_repository)
        self.power = Power()

    def start(self):
        self.running = True
        self.run()

    def run(self):

        if self.system.has_printer():
            SupportTeam.notify("using system default printer %s" % self.system.printer().printer_name)

        while self.running == True:
            try:
                if not self.system.has_printer():
                    SupportTeam.notify("failure - system has no default printer, skipping print")

                    # wait a bit longer than normal, so that the printer doesn't smash the log failed
                    time.sleep(20)
                    continue

                self.system.printer().cancel_all_jobs()
                self.power.cycle_printer()
                self.system.printer().send(self.saved_images.next())

            except:
                exceptiondata = traceback.format_exc().splitlines()
                SupportTeam.notify("failure - uncaught error, %s. skipping print" % (exceptiondata[-1]))

            finally:
                if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
                    SupportTeam.notify("debug: end loop, %s" % self.media_repository)

                time.sleep(5)

    def stop(self, signum, frame):
        self.running = False

if __name__ == '__main__':
    InstagramPrinter().start()
