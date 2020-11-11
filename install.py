import os, sys, stat
tools = os.system('wget https://raw.githubusercontent.com/cqsimple/tech/main/Tools.py')
initial = os.system('wget https://raw.githubusercontent.com/cqsimple/tech/main/initial.py')
update = os.system('wget https://raw.githubusercontent.com/cqsimple/tech/main/update.py')
files = ['initial.py', 'update.py', 'Tools.py']
for file in files:
    os.chmod(file, 0o0777)
f = open('.bash_profile', 'a')
f.write("python initial.py")
f.close()
