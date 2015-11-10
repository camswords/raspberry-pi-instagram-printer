from instagram.client import InstagramAPI
import os
import time
import cups
from xhtml2pdf import pisa
import sys
from subprocess import call

# Note this is heavily inspired from https://nicshackle.wordpress.com/2014/04/09/hashtag-activated-instagram-printer/

def addToPrintQueue(url):
    html = '<h1 style="text-align:center">Your image:</h1>\n'
    html += '<p style="text-align:center"><img src="' + url + '" align="middle"></p>'
    pdf = pisa.CreatePDF(html, file("/tmp/instagram-print.pdf", "w"))

    call(["/usr/bin/pdftops", "/tmp/instagram-print.pdf", "/tmp/instagram-print.ps"])
    print "converted to ps file"

    if not pdf.err:
        pdf.dest.close()
        connection = cups.Connection()
        printer = connection.getDefault()

        printers = connection.getPrinters()
        for printer in printers:
            print printer, printers[printer]["device-uri"]
            printer_name = printers.keys()[0] #use first printer in list

            connection.printFile(printer_name, "/tmp/instagram-print.ps", "instagram", {})
            print("added image document to print queue")
    else:
        print("failed to add image document to print queue")

api = InstagramAPI(client_id=os.environ['INSTAGRAM_CLIENT_ID'], client_secret=os.environ['INSTAGRAM_CLIENT_SECRET'])

mostRecentId = 0
url = ''
previous_url = ''

while True:
    try:
        sys.stdout.write('.')
        sys.stdout.flush()
        recent_media = api.tag_recent_media(1, mostRecentId, 'soccer')

        for media in recent_media[0]:
            url = media.images['standard_resolution'].url
            mostRecentId = media.id

            if (url != previous_url):
                print "\n---received an image---"
                print str(media.user)
                print str(media.caption)
                print "url: " + str(url)
                previous_url = url
                addToPrintQueue(url)
                print "\n"

    except Exception, e:
        print "failed to retrieve recent media due to"
        print e

    # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
    time.sleep(5)
