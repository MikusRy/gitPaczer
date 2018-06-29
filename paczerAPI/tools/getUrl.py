import urllib.request as urllib2


def get_url(q, url):
    return urllib2.urlopen(url).read()
