import cups
from printer import Printer

class System:

    def __init__(self):
        self.printerConnection = cups.Connection()

    def printer(self):

        if (self.printerConnection.getDefault()):
            return Printer(self.printerConnection.getDefault())

        printers = self.printerConnection.getPrinters()
        if printers.has_key("Canon_CP910_2"):
            return Printer(printers["Canon_CP910_2"])

        return None

    def has_printer(self):
        return self.printer() is not None
