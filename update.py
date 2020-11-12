# Written by Edward Lentz
import os, urllib2

filedata = urllib2.urlopen('https://raw.githubusercontent.com/cqsimple/tech/main/Tools.py')
datatowrite = filedata.read()
with open('Tools.py', 'wb') as f:
    f.write(datatowrite)
    
filedata1 = urllib2.urlopen('https://raw.githubusercontent.com/cqsimple/tech/main/initial.py')
datatowrite = filedata1.read()
with open('initial.py', 'wb') as f:
    f.write(datatowrite)

filedata2 = urllib2.urlopen('https://raw.githubusercontent.com/cqsimple/tech/main/update.py')
datatowrite = filedata2.read()
with open('update.py', 'wb') as f:
    f.write(datatowrite)

files = ['initial.py', 'update.py', 'Tools.py']
for file in files:
    os.chmod(file, 0o0777)
