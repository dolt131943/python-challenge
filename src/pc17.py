import urllib2,re,cookielib,urllib,bz2

src_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
busynothing = '12345'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
info = []
while True:
    url = src_url + busynothing
    text = opener.open(url).read()
    info.append(cj._cookies['.pythonchallenge.com']['/']['info'].value)
    print text
    a = re.findall('and the next busynothing is (\d+)',text)
    if len(a) == 0 :
        break
    busynothing=a[0]

msg = ''.join(info)

decode_msg = bz2.BZ2Decompressor().decompress(urllib.unquote_plus(msg))

print decode_msg

# is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.

import xmlrpclib
phonebook = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print phonebook.phone('Leopolp')

# http://www.pythonchallenge.com/pc/stuff/violin.php

cj._cookies['.pythonchallenge.com']['/']['info'].value = 'the+flowers+are+on+their+way'

print opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()


