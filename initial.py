# Written by Ed Lentz
import os
clear = os.system("clear")
print ("")
print("CQ Simple Nimbus Command Line system.")
print("Enter the number of the command you want to run and press enter.")

ans=True
while ans:
    print("""
    1.Command Line Tools
    2.Update Tools program
        """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      check_date = os.system("python Tools.py")
    elif ans=="2":
      restart_ntpd = os.system("python update.py")
    elif ans=="CQSimple5103#":
      exit()
    else:
       print("\n Not a Valid Choice Try again")
       

