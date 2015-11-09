from instagram.client import InstagramAPI
import os
import time
import cups
from xhtml2pdf import pisa

# Note this is heavily inspired from https://nicshackle.wordpress.com/2014/04/09/hashtag-activated-instagram-printer/

def addToPrintQueue(url):
    html = '<h1 style="text-align:center">Your image:</h1>\n'
    html += '<p style="text-align:center"><img src="' + url + '" align="middle"></p>'
    pdf = pisa.CreatePDF(html, file("/tmp/instagram-print.pdf", "w"))

    if not pdf.err:
        pdf.dest.close()
        connection = cups.Connection()
        printer = connection.getDefault()

        if printer is None:
            print("failed to print as a default printer has not been set up in cups.")
        else:
            connection.printFile(printer, "/tmp/instagram-print.pdf", "instagram", {})
            print("added image document to print queue")
    else:
        print("failed to add image document to print queue")

api = InstagramAPI(client_id=os.environ['INSTAGRAM_CLIENT_ID'], client_secret=os.environ['INSTAGRAM_CLIENT_SECRET'])

mostRecentId = 0
url = ''
previous_url = ''
recent_media = api.tag_recent_media(1, mostRecentId, 'soccer')

while True:
    try:
        for media in recent_media[0]:
            url = media.images['standard_resolution'].url
            mostRecentId = media.id

            if (url != previous_url):
                print "---received an image---"
                print str(media.user)
                print str(media.caption)
                print "url: " + str(url) + "\n"
                previous_url = url
                addToPrintQueue(url)

    except Exception, e:
        print "failed to retrieve recent media due to"
        print e

    # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
    time.sleep(5)
