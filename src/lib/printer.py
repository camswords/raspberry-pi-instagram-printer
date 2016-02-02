from timeout import timeout
import time
from job import Job

class Printer:

    def __init__(self, connection, printer_name):
        self.connection = connection
        self.printer_name = printer_name

    def printer(self):
        printers = self.connection.getPrinters()
        return printers[self.printer_name]

    def status(self):
        if self.printer()["printer-state"] is 3:
            return "idle"
        elif self.printer()["printer-state"] is 4:
            return "printing"
        elif self.printer()["printer-state"] is 5:
            return "stopped"

        return "unknown (%s)" % self.printer()["printer-state"]

    def safely_get(self, key):
        if self.printer().has_key(key):
            return self.printer()[key]

        return None

    def safely_get_array(self, key):
        if self.printer().has_key(key):
            return self.printer()[key]

        return []

    def ready_to_print(self):
        return self.status() == "idle"

    @timeout(120)
    def send(self, saved_image):
        if not self.ready_to_print():
            raise RuntimeException("attempting to print %s but the printer is not ready to print" % self.status())

        job_id = self.connection.printFile(self.printer_name, saved_image.file_path, "", {})

        # it takes about a minute to print an image.
        print "wait a minute, give it a chance to print..."
        time.sleep(90)

        return Job(self.connection, job_id)

    def errors(self):
        reasons = self.safely_get_array("printer-state-reasons")
        messages = self.safely_get_array("printer-state-message")

        if reasons == ["none"]:
            reasons = []

        return "messages (%s), reasons (%s)" % (messages, reasons)

    def has_errors(self):
        reasons = self.safely_get_array("printer-state-reasons")
        messages = self.safely_get_array("printer-state-message")

        if reasons == ["none"]:
            reasons = []

        return len(messages) > 0 or len(reasons) > 0

    def cancel_all_jobs(self):
        self.connection.cancelAllJobs(self.printer_name)

    def __str__(self):
        status = self.status()
        accepting = self.safely_get("printer-is-accepting-jobs")
        errors = self.errors()

        if accepting is None:
            accepting = "?"

        if self.has_errors():
            return "printer(name: %s, status: %s, accepting: %s), has errors: %s" % (self.printer_name, status, accepting, errors)

        return "printer(name: %s, status: %s, accepting: %s)" % (self.printer_name, status, accepting)
