#!/usr/bin/env bash

# install the latest patches for installed software
apt-get update
apt-get upgrade --assume-yes

# install git, install code
apt-get install git --assume-yes
git clone https://github.com/camswords/raspberry-pi-instagram-printer.git

# install python modules
apt-get install python-dev python-pip libjpeg8-dev --assume-yes
pip install python-instagram
pip install xhtml2pdf

# install cups
apt-get install cups cups-pdf python-cups --assume-yes
usermod -a -G lpadmin pi
lpadmin -x PDF
/etc/init.d/cups restart

# install a later version of gutenprint that has the Canon Selphy driver
apt-get install gettext libcups2-dev automake libtool libtool-bin autopoint jade libcupsimage2-dev --assume-yes
wget http://sourceforge.net/projects/gimp-print/files/gutenprint-5.2/5.2.11-pre1/gutenprint-5.2.11-pre1.tar.bz2

tar xvfj gutenprint-5.2.11-pre1.tar.bz2
cd gutenprint-5.2.11-pre1

mkdir -p /usr/share/foomatic/db
./autogen.sh --enable-debug --disable-shared --with-cups-nickname=" - CUPS+Gutenprint-CVS v" --disable-libgutenprintui2 --without-doc --enable-cups-ppds --enable-testpattern
make
make install

# copy configuration files for printer
cp /home/pi/raspberry-pi-instagram-printer/files/etc/cups/cupsd.conf /etc/cups/cupsd.conf
cp /home/pi/raspberry-pi-instagram-printer/files/etc/cups/printers.conf /etc/cups/printers.conf

/etc/init.d/cups restart
/etc/init.d/cups force-reload
