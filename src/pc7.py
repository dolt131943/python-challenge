import urllib,StringIO,Image,re

img = Image.open(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()))

w,h = img.size

str1 = ''.join(map(chr, [img.getpixel((i,h//2))[0] for i in range(0,w,7)]))

str2 = re.findall('\[(.*)\]', str1)[0]

arr = str2.split(',')

result = ''.join(map(chr, map(int,arr)))

print result


