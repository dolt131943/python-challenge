import urllib,StringIO,Image

gfx = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx').read()

def openrw(fn):return open(fn, 'w')

f = map(openrw, ['1.jpg', '2.png', '3.gif','4.png','5.jpg'])

for i in range(len(gfx)/5):
    for j in range(5): f[j].write(gfx[i*5+j])

for fn in f : fn.close()



