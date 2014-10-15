import re,string

in_str = ''.join([line.rstrip() for line in open('pc3-data.txt')])

# print in_str

# pattern = re.compile(r'([A-Z]{3})([a-z]{1})([A-Z]{3})')

output = ''

'''
for match in re.finditer(r'([A-Z]{3})([a-z]{1})([A-Z]{3})', in_str):
    #print match.group()
    #if match.group(1) == match.group(3):
    output += match.group(2)
'''

pos = 0
test = 0x0
for c in in_str :
    # print str(pos) + "->" + c
    test = test << 1
    if c in string.ascii_lowercase:
        test = test | 0x0 
    else:
        test = test | 0x1        
    # 011101110
    if test & 0x1ff == 0xee:
	# print in_str[pos-7:pos]
        # print in_str[pos-7:pos-4] + "=" + in_str[pos-3:pos]
	output += in_str[pos - 4]

    pos+=1

print output
