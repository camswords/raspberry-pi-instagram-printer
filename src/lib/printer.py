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
        SupportTeam.notify("recover printer - cancelling all jobs")
        self.connection.cancelAllJobs(self.printer_name)

    @timeout(120)
    def send_file_to_printer(self, image):
        SupportTeam.notify("%s - sent to printer, waiting to print (90 secs)" % image.media.id)
        job_id = self.connection.printFile(self.printer_name, image.file_path, "", {})

        # it takes about a minute to print an image. 1.5 mins is conservative.
        time.sleep(5)

    def send(self, image):
        self.cancel_all_jobs()
        self.power.cycle_printer()
        self.send_file_to_printer(image)
