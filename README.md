# raspberry-pi-instagram-printer #

### Installation ###

#### Initial Pi setup ####

1. Download the latest raspbian instance from https://www.raspberrypi.org/downloads/
1. Unzip the zip file, using p7zip if unzip can't do it (`brew install p7zip`, `7za x [filename]`)
1. Install the image on to a Pi. Recommend if you have a mac: http://alltheware.wordpress.com/2012/12/11/easiest-way-sd-card-setup/
1. Figure out your Pi's IP address on the network https://www.raspberrypi.org/documentation/troubleshooting/hardware/networking/ip-address.md
1. ssh into your Pi: `ssh pi@[your ip address]`. When the password prompt appears, type `raspberry`
1. Install the code using `sudo bash < <(curl https://raw.githubusercontent.com/camswords/raspberry-pi-instagram-printer/master/install.sh)`


### Is it working? ###

You can check the tags on instagram here: https://instagram.com/explore/tags/[tag-name]/

### Printers ###

### References ###
See https://docs.oracle.com/cd/E23824_01/html/821-1451/gllgm.html

#### add a printer ####
`/usr/sbin/lpadmin -p printer-name -E -v device -m ppd`
p Specifies the name of the printer to add.
E Enables the destination and accepts jobs.
v Sets the device-uri attribute of the print queue.
m Sets the PPD file for the printer from the model directory or by using one of the driver interfaces.

eg. To add an HP LaserJet printer LaserJet by using a JetDirect network interface with the IP address 10.1.1.1, you would type the following command:

$ /usr/sbin/lpadmin -p LaserJet -E -v socket://10.1.1.1 -m laserjet.ppd

#### What printers are available ####
`lpstat -p -d`
