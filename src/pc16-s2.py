import Image,utils

im = Image.open(utils.getUrlToFile('http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'))
w,h = im.size
color = 195

il = list(im.getdata())
for r in range(0,w*h,w):
    x = il.index(color,r)
    il[r:r+w] = il[x:r+w] + il[r:x]


im.putdata(il)
im.save('17.png')
