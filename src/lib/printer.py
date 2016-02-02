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
        return self.status() == "idle" and not self.has_errors()

    @timeout(120)
    def send(self, saved_image):
        if not self.ready_to_print():
            raise RuntimeException("attempting to print %s but the printer is not ready to print" % self.status())


        saved_image.update_media_as_printing()

        print "%s - sent to printer, waiting to print (90 secs)" % saved_image.media.id
        job_id = self.connection.printFile(self.printer_name, saved_image.file_path, "", {})

        # it takes about a minute to print an image. 1.5 mins is conservative.

        time.sleep(30)
        print "wait 30 secs"
        print "has_errors? %s, errors are %s" % (self.has_errors(), self.errors())
        print "printer", self
        print "jobs %s", self.connection.getJobs()

        time.sleep(30)
        print "wait 30 secs"
        print "has_errors? %s, errors are %s" % (self.has_errors(), self.errors())
        print "printer", self
        print "jobs %s", self.connection.getJobs()

        time.sleep(30)
        print "wait 30 secs"
        print "has_errors? %s, errors are %s" % (self.has_errors(), self.errors())
        print "printer", self
        print "jobs %s", self.connection.getJobs()

        saved_image.update_media_as_printed()

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
