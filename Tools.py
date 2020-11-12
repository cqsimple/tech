import os
# Written by Edward Lentz
clear = os.system("clear")
print ("")
print("CQ Simple Nimbus Command Line Tools.")
print ("Use these commands with caution.")
print("Enter the number of the command you want to run and press enter.")

ans=True
while ans:
    print("""
    1.Check System Date / Time
    2.Restart Date service
    3.Fwconsole restart
    4.Fwconsole Upgrade Modules
    5.Validate Modules
    6.Clean modules
    7.Refresh module signatures
    8.Reset file permissions
    9.PM2 List
    10.Restart Clearly Devices Module
    99.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      check_date = os.system("date")
    elif ans=="2":
      restart_ntpd = os.system("service ntpd restart")
    elif ans=="3":
      fwconsole_restart = os.system("fwconsole restart")
    elif ans=="4":
      Module_update = os.system("fwconsole ma upgradeall")
    elif ans=="5":
      validate = os.system("fwconsole validate")
    elif ans=="6":
      clean = os.system("fwconsole validate --clean")
    elif ans=="7":
      refresh = os.system("fwconsole ma refreshsignatures")
    elif ans=="8":
      file_permissions = os.system("fwconsole chown")
    elif ans=="9":
      pm2_list = os.system("fwconsole pm2 --list")
    elif ans=="10":
      restart_clearly = os.system("fwconsole pm2 --restart='clearlydevices'")
    elif ans=="99":
      Quit = os.system("exit")
      clear=os.system("clear")
      print ("")
      print("Your session is over.")
      print("Please disconnect from the system.")
      ans = None
    else:
      print("\n Not a Valid Choice Try again")
