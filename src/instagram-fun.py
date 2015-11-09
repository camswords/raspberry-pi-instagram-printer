from instagram.client import InstagramAPI
import os
import time

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

    except Exception, e:
        print "failed to retrieve recent media due to"
        print e

    # lets not go mental, rate limit seems to be 5000 / hr. (5 secs = 720 requests per hr)
    time.sleep(5)
