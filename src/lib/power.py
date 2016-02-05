from subprocess import check_call
import time

class Power:

    def __init__(self):

    def cycle_printer(self):
        # turn off
        check_call(["/home/pi/send", "001000001111101000000110"])
        time.sleep(20)

        # turn on
        check_call(["/home/pi/send", "001000001111101000001110"])
        time.sleep(70)
