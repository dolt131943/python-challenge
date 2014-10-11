import urllib,xmlrpclib

phonebook = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print phonebook.phone('Bert')

