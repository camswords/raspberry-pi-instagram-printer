#!/usr/bin/env bash

# install the latest patches for installed software
apt-get update
apt-get upgrade --assume-yes

# install git, install code
apt-get install git --assume-yes
git clone https://github.com/camswords/raspberry-pi-instagram-printer.git

# install python modules
apt-get install python-dev --assume-yes
pip install python-instagram

# install cups
apt-get install cups --assume-yes
usermod -a -G lpadmin pi
cp ./raspberry-pi-instagram-printer/files/etc/cups/cupsd.conf /etc/cups/cupsd.conf
mkdir -p /usr/share/printer-definitions
cp ./raspberry-pi-instagram-printer/files/usr/share/printer-definitions/canon-cp910.ppd /usr/share/printer-definitions
/etc/init.d/cups restart
