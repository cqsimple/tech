#!/bin/bash
#====Get the deployment number from the system=====
deply=$(awk '/deploymentid/{print $NF}' /etc/schmooze/schmooze.zl)
#========End====================
WANIP=$(curl -s http://whatismyip.akamai.com/)
IP=$(ip addr show eth0 | awk '/inet / {print $2}' | cut -d/ -f 1)
MAC=$(ip link show eth0 | awk '/ether/ {print $2}')
echo "Enter the Dealer name:"
read dealer
echo " What Model is this machine (40, 100, 250, 500)?:"
read model
echo " Enter the Dashboard License #?:"
read fop2
echo "IP Address: $IP"
echo "MAC Address: $MAC"
# Generate the hash from the MAC address
# ==========Old method of making the root password out of the MAC Address ========
# md5=$(echo -n "$MAC" | md5sum | cut -f1 -d' ')
#echo " $md5"
# ========Making the Root password the same for all new installs =======

rpass="CQsimple5103#"

#===== Download the Nimbus Tools Install file ==========
wget -b -q https://raw.githubusercontent.com/cqsimple/tech/main/install.py

NOW=$(date +"%m-%d-%Y")
cat >/var/www/html/Nimbusregistrationinfo.txt << EOF
=======================================================================
                       Nimbus $model Version 4.0
Here is some info on your system.
This system was sold to : $dealer
The deployment number of this machine is: $deply
The  MAC address of this machine is : $MAC
The build date of this machine is: $NOW
The Root Technician Tools Password is : $rpass
The FOP2 License # is: $fop2
CQ Simple Tech Root password is CQSimple5103#
=======================================================================
EOF
cat >/var/www/html/Nimbusinfo.txt << EOF
=======================================================================
                       Nimbus $model Version 3.0
Thank you for your Nimbus purchase. Here is some info on your system.
This system was sold to : $dealer
The deployment number of this machine is: $deply
The  MAC address of this machine is : $MAC
The Dashboard License # is: $fop2

=======================================================================
EOF
echo  "$rpass" | passwd --stdin root
echo "Deployment ID $deply
The FOP2 license # is: $fop2
The system was sold to: $dealer
The MAC Address is: $MAC
The WAN Ip of this system is: $WANIP
The Tech Root Password is: $rpass" | mail -s "$dealer -- Deployment # $deply" deployment@cqsimple.com
echo " All Done!"
