import Image,utils

im = Image.open(utils.getUrlToFile("http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif"))
w,h = im.size

magenta = 195

bars = []

for j in range(h):
    for i in range(w):
        if im.getpixel((i,j)) == magenta and im.getpixel((i+4, j)) == magenta:
            bars.append((i,j))

shift = Image.new(im.mode,(w,h),0)
shift.palette = im.palette
for j in range(h):
    for i in range(w):
        shift.putpixel(((i+w-bars[j][0])%w, j), im.getpixel((i,j)))
shift.save('17.png')
