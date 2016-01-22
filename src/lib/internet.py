import urllib2

class Internet:

    def hasConnectivity(self):
        # from http://stackoverflow.com/questions/3764291/checking-network-connection
        try:
            response = urllib2.urlopen('http://www.google.com.au', timeout = 10)
            return True
        except urllib2.URLError as err: pass
        return False
