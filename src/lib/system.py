import cups
from printer import Printer
from jobs import Jobs
from job import Job

class System:

    def __init__(self):
        self.connection = cups.Connection()

    def printer_name(self, printer):
        printers = self.connection.getPrinters()

        for index, this_printer_name in enumerate(printers.keys()):
            this_printer = printers[this_printer_name]

            if this_printer["device-uri"] == printer["device-uri"]:
                return this_printer_name

        raise RuntimeException("failed to determine printer name of printer %s", printer["device-uri"])

    def printer(self):
        if (self.connection.getDefault()):
            return Printer(self.connection, self.connection.getDefault())

        printers = self.connection.getPrinters()

        if printers.has_key("Canon_CP910_2"):
            return Printer(self.connection, self.printer_name(printers["Canon_CP910_2"]))

        return None

    def has_printer(self):
        return self.printer() is not None

    def has_jobs(self):

        if len(self.connection.getJobs()) > 0:
            print "has jobs!", self.connection.getJobs()

        return len(self.connection.getJobs()) > 0

    def jobs(self):
        return Jobs(self.connection)

    def job(self, job_id):
        return Job(self.connection, job_id)
