import cups
from printer import Printer

class System:

    def __init__(self):
        self.printerConnection = cups.Connection()

    def printer_name(self, printer):
        printers = self.printerConnection.getPrinters()

        for index, this_printer_name in enumerate(printers.keys()):
            this_printer = printers[this_printer_name]

            if this_printer["device-uri"] == printer["device-uri"]:
                return this_printer_name

        raise RuntimeException("failed to determine printer name of printer %s", printer["device-uri"])

    def printer(self):
        if (self.printerConnection.getDefault()):
            default = self.printerConnection.getDefault()
            return Printer(self.printerConnection, self.printer_name(default), default)

        printers = self.printerConnection.getPrinters()

        if printers.has_key("Canon_CP910_2"):
            return Printer(self.printerConnection, self.printer_name(printers["Canon_CP910_2"]), printers["Canon_CP910_2"])

        return None

    def has_printer(self):
        return self.printer() is not None
