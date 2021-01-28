# Written by Edward Lentz
import os, urllib2,time,shutil

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
    
# filedata3 = urllib2.urlopen('https://raw.githubusercontent.com/cqsimple/tech/main/irontec.repo')
# datatowrite = filedata3.read()
# with open('irontec.repo', 'wb') as f:
#    f.write(datatowrite) 
    

files = ['initial.py', 'update.py', 'Tools.py']
for file in files:
    os.chmod(file, 0o0777)

# original = r'/irontec.repo'
# target = r'/etc/yum.repos.d/irontec.repo'
# shutil.move(original,target)    
    
print("You should have the latest version now.")
time.sleep(10)

clear = os.system("clear")
