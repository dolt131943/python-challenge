import Image,urllib,StringIO

im = Image.open(StringIO.StringIO(urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg').read()))
w,h = im.size

for i in range(w):
    for j in range(h):
        if ((i+j) % 2) == 1:
            im.putpixel((i,j),0)

im.save('cave_new.png')
