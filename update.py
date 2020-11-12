# Written by Ed Lentz
import os
clear = os.system("clear")
os.remove("Tools.py")
tools = os.system('wget https://raw.githubusercontent.com/cqsimple/tech/main/Tools.py')
os.remove("initial.py")
tools = os.system('wget https://raw.githubusercontent.com/cqsimple/tech/main/initial.py')
print("You should have the latest version now.")
