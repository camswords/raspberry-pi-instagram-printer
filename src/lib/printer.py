

class Printer:

    def __init__(self, printer):
        self.printer = printer

    def status(self):
        if self.printer["printer-state"] is 3:
            return "idle"
        elif self.printer["printer-state"] is 4:
            return "printing"
        elif self.printer["printer-state"] is 5:
            return "stopped"

        return "unknown (%s)" % self.printer["printer-state"]

    def safely_get(self, key):
        if self.printer.has_key(key):
            return self.printer[key]

        return None

    def safely_get_array(self, key):
        if self.printer.has_key(key):
            return self.printer[key]

        return []

    def errors(self):
        reasons = self.safely_get_array("printer-state-reasons")
        messages = self.safely_get_array("printer-state-message")

        if reasons == ["none"]:
            reasons = []

        return "messages (%s), reasons (%s)" % (",".join(messages), ",".join(reasons))

    def has_errors(self):
        reasons = self.safely_get_array("printer-state-reasons")
        messages = self.safely_get_array("printer-state-message")

        if reasons == ["none"]:
            reasons = []

        return len(messages) > 0 or len(reasons) > 0

    def __str__(self):
        info = self.safely_get("printer-info")
        status = self.status()
        accepting = self.safely_get("printer-is-accepting-jobs")
        errors = self.errors()

        if accepting is None:
            accepting = "?"

        if self.has_errors():
            return "printer(name: %s, status: %s, accepting: %s), has errors: %s" % (info, status, accepting, errors)

        return "printer(name: %s, status: %s, accepting: %s)" % (info, status, accepting)
