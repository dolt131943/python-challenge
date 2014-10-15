import pickle,urllib

f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

o = pickle.load(f)

for l in o:
    s = ''
    for t in l:s += ''.join(t[0] for __ in range(t[1]))
    print s


