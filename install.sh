#!/usr/bin/env bash

# as a first step, get the user to enter their instagram details
echo "For the following, you will need your instagram details which can be found from http://instagram.com/developer/."
echo "Please enter your instagram client id: "
read INSTAGRAM_CLIENT_ID

if [ -z "$INSTAGRAM_CLIENT_ID" ]; then
    echo "Please enter a valid instagram client id."
    exit 1
fi

echo "Please enter your instagram client secret: "
read INSTAGRAM_CLIENT_SECRET

if [ -z "$INSTAGRAM_CLIENT_SECRET" ]; then
    echo "Please enter a valid instagram client secret."
    exit 1
fi

echo "Please enter the instagram hashtag you would like to follow: "
read INSTAGRAM_HASHTAG

if [ -z "$INSTAGRAM_HASHTAG" ]; then
    echo "Please enter a valid instagram hashtag to follow."
    exit 1
fi

echo "Thanks! Preparing to install. This takes around one hour."

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

# copy configuration files for cups
cp /home/pi/raspberry-pi-instagram-printer/files/etc/cups/cupsd.conf /etc/cups/cupsd.conf

/etc/init.d/cups force-reload
/etc/init.d/cups restart

# set up the init.d script to start the instagram printing
cp /home/pi/raspberry-pi-instagram-printer/files/etc/init.d/instagram-print /etc/init.d/instagram-print
chmod 755 /etc/init.d/instagram-print

# replace the instagram values with the ones the user has typed in.
sed -i "s/INSTAGRAM_CLIENT_ID_VALUE/$INSTAGRAM_CLIENT_ID/g" /etc/init.d/instagram-print
sed -i "s/INSTAGRAM_CLIENT_SECRET_VALUE/$INSTAGRAM_CLIENT_SECRET/g" /etc/init.d/instagram-print
sed -i "s/INSTAGRAM_HASHTAG_VALUE/$INSTAGRAM_HASHTAG/g" /etc/init.d/instagram-print

# ensure that the script starts when the raspberrypi boots
update-rc.d instagram-print defaults

# start the service, in preparation for the user configuring their printer.
/etc/init.d/instagram-print start


# Instructions
printf "\n\n"
printf "Congratulations, your instagram printer has been configured. Next steps:\n"
printf "1. Navigate to [your ip address]:693 in a web browser.\n"
printf "2. Install your printer of choice (make sure sharing is Yes).\n"
printf "3. Make the printer the default system printer.\n"
printf "All things working, your printer should start printing the hashtags.\n\n"
printf "Note: if configuring using USB, you may need to run the following:\n"
printf "1. lpadmin -p [your printer name] -o usb-unidir-default=true\n"
printf "2. lpadmin -p [your printer name] -o usb-no-reattach-default=true\n"
printf "Note: you can change your instagram details by editing the /etc/init.d/instagram-print file.\n"
printf "Note: logs are found in /var/log/instagram-print.log and /var/log/instagram-print.err.\n"
printf "Note: you can control the service by running sudo /etc/init.d/instagram-print start|stop|restart.\n\n"
printf "Enjoy.\n"
