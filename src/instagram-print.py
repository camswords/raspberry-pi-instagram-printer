#!/usr/bin/env python

from instagram.client import InstagramAPI
import os
import time
import sys
from subprocess import check_call
import traceback
import urllib2

# Note this is heavily inspired from https://nicshackle.wordpress.com/2014/04/09/hashtag-activated-instagram-printer/

def addToPrintQueue(url):
        print "downloading..."
        check_call(["wget", url, "--quiet", "-O", "/tmp/image.jpg"])
        print "adding to print queue..."
        check_call(["/home/pi/raspberry-pi-instagram-printer/src/send-file-to-default-printer.sh", "/tmp/image.jpg"])
        print "done."

        # it takes about a minute to print an image.
        print "wait a minute, give it a chance to print..."
        time.sleep(90)

def hasInternetConnectivity():
    # from http://stackoverflow.com/questions/3764291/checking-network-connection
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

api = InstagramAPI(client_id=os.environ['INSTAGRAM_CLIENT_ID'], client_secret=os.environ['INSTAGRAM_CLIENT_SECRET'])

mostRecentId = 0
url = ''
previous_url = ''

while True:
    try:
        if (!hasInternetConnectivity()):
            print "skipping check for instagram media, no internet connection can be established."

        sys.stdout.write('.')
        sys.stdout.flush()
        recent_media = api.tag_recent_media(1, mostRecentId, os.environ['INSTAGRAM_HASHTAG'])

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
                print "---done---"
                print "\n"

    except:
        print "failed to retrieve and print instagram images. Stack trace follows."
        traceback.print_exc(file=sys.stdout)

    # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
    time.sleep(5)
