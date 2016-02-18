from subprocess import check_call
import time

class Power:

    def turn_off(self):
        check_call(["/home/pi/send", "001000001111101000000110"])
        time.sleep(1)

    def turn_on(self):
        check_call(["/home/pi/send", "001000001111101000001110"])
        time.sleep(1)

    def cycle_printer(self):
        self.turn_off()
        self.turn_off()
        self.turn_off()
        self.turn_off()
        time.sleep(5)

        # turn on
        self.turn_on()
        self.turn_on()
        self.turn_on()
        self.turn_on()
        time.sleep(15)
