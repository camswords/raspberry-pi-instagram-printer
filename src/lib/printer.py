from support_team import SupportTeam
from power import Power
from timeout import timeout
import time

class Printer:

    def __init__(self, connection, printer_name):
        self.connection = connection
        self.printer_name = printer_name
        self.power = Power()

    def printer(self):
        printers = self.connection.getPrinters()
        return printers[self.printer_name]

    def cancel_all_jobs(self):
        self.connection.cancelAllJobs(self.printer_name)

    @timeout(120)
    def send_file_to_printer(self, image):
        job_id = self.connection.printFile(self.printer_name, image.file_path, "", {})

    def send(self, image):
        SupportTeam.notify("%s - cancelling all jobs" % image.media.id)
        self.cancel_all_jobs()

        SupportTeam.notify("%s - turning printer off (5 secs)" % image.media.id)
        self.power.turn_off()
        time.sleep(5)

        SupportTeam.notify("%s - turning printer on (15 secs)" % image.media.id)
        self.power.turn_on()
        time.sleep(15)

        # it takes about a minute to print an image. 1.5 mins is conservative.
        SupportTeam.notify("%s - sent to printer, waiting to print (90 secs)" % image.media.id)
        self.send_file_to_printer(image)
        time.sleep(90)
