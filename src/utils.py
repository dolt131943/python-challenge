import urllib,StringIO
def getUrlToStr(url):
    return urllib.urlopen(url).read()


def getUrlToFile(url):
    return StringIO.StringIO(getUrlToStr(url))


