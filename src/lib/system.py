import cups
from printer import Printer

class System:

    def __init__(self):
        self.connection = cups.Connection()

    def printer(self):
        if (self.connection.getDefault()):
            return Printer(self.connection, self.connection.getDefault())

        return None

    def has_printer(self):
        return self.printer() is not None
