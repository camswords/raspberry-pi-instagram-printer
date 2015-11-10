# raspberry-pi-instagram-printer #

### Installation ###

#### Initial Pi setup ####

1. Download the latest raspbian instance from https://www.raspberrypi.org/downloads/
1. Unzip the zip file, using p7zip if unzip can't do it (`brew install p7zip`, `7za x [filename]`)
1. Install the image on to a Pi. Recommend if you have a mac: http://alltheware.wordpress.com/2012/12/11/easiest-way-sd-card-setup/
1. Figure out your Pi's IP address on the network https://www.raspberrypi.org/documentation/troubleshooting/hardware/networking/ip-address.md
1. ssh into your Pi: `ssh pi@[your ip address]`. When the password prompt appears, type `raspberry`
1. Install the code using `sudo bash < <(curl https://raw.githubusercontent.com/camswords/raspberry-pi-instagram-printer/master/install.sh)`
1. On the Pi, type `vi ~/.profile`, go into insert mode using `i` and type the following
`export INSTAGRAM_CLIENT_ID=[your instagram client id]
 export INSTAGRAM_CLIENT_SECRET=[your instagram client secret]`
Then hit `ESC`, then `:wq` and press `ENTER` to save the file.
1. So you can use the environment variables from the previous step without a restart, type `source ~/.profile`.

Note: if you dont have a instagram client id / secret, see http://instagram.com/developer.
Note: this has been tested using 2015-09-24-raspbian-jessie.

### Is it working? ###

You can check the tags on instagram here: https://instagram.com/explore/tags/[tag-name]/

### Printers ###

### References ###
See https://docs.oracle.com/cd/E23824_01/html/821-1451/gllgm.html

#### add a printer ####
`lpadmin -p printer-name -E -v device -P path-to-ppd`
p Specifies the name of the printer to add.
E Enables the destination and accepts jobs.
v Sets the device-uri attribute of the print queue.
m Sets the PPD file for the printer from the model directory or by using one of the driver interfaces.

eg. To add an a Canon Selphy 910 printer type the following command:

`lpadmin -p canon-selphy-910 -E -v socket://192.168.0.22 -P /usr/share/printer-definitions/canon-cp910.ppd`

#### What printers are available ####
`lpstat -p -d`
