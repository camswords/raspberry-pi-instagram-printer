
from lib.system import System
import time

system = System()

print "has printer?", system.has_printer()

if system.has_printer():
    printer = system.printer()
    print "using printer", printer
    print "sending job to printer..."
    job = printer.send_to_printer("/tmp/image.jpg")

    print system.printer()
    print job.attributes()
    time.sleep(5)

    print system.printer()
    print job.attributes()
    time.sleep(5)

    print system.printer()
    print job.attributes()
    time.sleep(5)

    print system.printer()
    print job.attributes()
    time.sleep(5)

    print system.printer()
    print job.attributes()
    time.sleep(5)

    print system.printer()
    print job.attributes()
    time.sleep(5)
