import re,string

in_str = ''.join([line.rstrip() for line in open('pc3-data.txt')])

# print in_str

# pattern = re.compile(r'([A-Z]{3})([a-z]{1})([A-Z]{3})')

output = ''

for match in re.finditer(r'([^A-Z][A-Z]{3})([a-z]{1})([A-Z]{3}[^A-Z])', in_str):
    output += match.group(2)

print output
