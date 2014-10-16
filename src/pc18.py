import utils,gzip,difflib

url = 'http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz'

# save to file because gzip.open must read from filename
gzfilename = 'pc18-deltas.gz'
gzf = file(gzfilename, 'w')
gzf.write(utils.getUrlToStr(url))
gzf.close()

# decompress and read
ugz = gzip.open(gzfilename, 'r')
lines = ugz.readlines()
ugz.close()

# split to two part (left and right)
cols = ([],[])

for i in range(len(lines)):
    (l,r) = (lines[i][:53], lines[i][56:])
    cols[0].append(l+'\n')
    cols[1].append(r)

# diff the line
diff_list = list(difflib.Differ().compare(cols[0], cols[1]))

# split diff to three type: equal(' ',initial space),plus('+', initial plus),minus('-', initial minus)
# [''.join(filter(lambda l: l[0] == d, column_diffs)) for d in " +-"]
split_png = [''.join([line[2:len(line)-1] for line in diff_list if line.startswith(c)]) for c in (' +-')]

for i in range(len(split_png)) :
    f = open('pc18-%d.png' % (i+1), 'wb')
    f.write(''.join([hexc.decode('hex') for hexc in split_png[i].split(' ')]))
    f.close()

















