import zipfile,urllib,StringIO,re

f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

zf = zipfile.ZipFile(StringIO.StringIO(f.read()))

target_file = 'readme.txt'

target_nums = []

while True:
     s = zf.read(target_file)
     # print s
     a = re.findall('[(from)|(is)] (\d+)', s)
     if len(a) > 0:
        target_nums.append(a[0])
        target_file = a[0] + '.txt'
     else:
        print s
        break


# print target_nums

result = ''.join([zf.getinfo('%s.txt' %p).comment for p in target_nums])
print result
