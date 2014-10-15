import urllib

begin_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

nothing = str(16044 /2)

while True:
    f = urllib.urlopen(begin_url + nothing)
    line = f.read()
    print line
    if ' ' in line:
        nothing = line[line.rindex(' ')+1:]
        if not nothing.isdigit():
            break
    else:
        break

print nothing
