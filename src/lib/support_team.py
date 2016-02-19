import sys
import datetime

class SupportTeam:

    @staticmethod
    def notify(message):
        print "%s: %s" % (datetime.datetime.now(), message)
        sys.stdout.flush()
