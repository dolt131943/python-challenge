import pickle,urllib

f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

o = pickle.load(f)

for l in o:
    s = ''
    for t in l:
        for n in range(t[1]):
            s += t[0]
    print s


