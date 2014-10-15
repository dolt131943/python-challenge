import urllib, StringIO, Image

src_img = Image.open(StringIO.StringIO(urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/wire.png').read()))
new_img = Image.new(src_img.mode, (100,100), 0)

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
(x,y,z) = (-1,0,0)
for i in range(200):
    d = dirs[i % 4]
    for j in range(100 - (i +1) // 2):
        x += d[0]
        y += d[1]
        # print "%d,%d <= %d" % (x,y,z)
        new_img.putpixel((x,y), src_img.getpixel((z,0)))
        z+=1

new_img.save('15.png')
