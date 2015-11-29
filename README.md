# raspberry-pi-instagram-printer #

### Installation ###

#### Initial Pi setup ####

1. Download the latest raspbian instance from https://www.raspberrypi.org/downloads/ (recommend: 2015-11-21-raspbian-jessie-lite)
1. Unzip the zip file, using p7zip if unzip can't do it (`brew install p7zip`, `7za x [filename]`)
1. Install the image on to a Pi. Recommend if you have a mac: http://alltheware.wordpress.com/2012/12/11/easiest-way-sd-card-setup/
1. Boot your Pi
1. Figure out your Pi's IP address on the network
  * Run a port scan on your network eg `nmap -sn 192.168.0.0/24`
  * More info can be found at https://www.raspberrypi.org/documentation/troubleshooting/hardware/networking/ip-address.md
1. ssh into your Pi: `ssh pi@[your ip address]`. When the password prompt appears, type `raspberry`
1. If you need to configure your Pi for Wifi access, the on the Pi
  * `sudo vi /etc/wpa_supplicant/wpa_supplicant.conf`
  * Add a new section: `network={ ssid="testing" psk="testingPassword" }`, then save using `:wq`
  * `sudo ifdown wlan0`
  * `sudo ifup wlan0`
  * More info can be found at https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
1. Expand the file system and reboot using `sudo raspi-config`

#### Installation ####

For this to work, you will need your instagram client id, secret, and the hashtag that you would like to follow / print. You can find / create these at http://instagram.com/developer.

1. Download the install file `wget https://raw.githubusercontent.com/camswords/raspberry-pi-instagram-printer/master/install.sh`.
2. Make it executable `chmod +x install.sh`
3. Execute it with root permissions `sudo ./install.sh`

This installation takes around an hour, largely because it needs to compile gutenprint.

### Is it working? ###

You can check the tags on instagram here: https://instagram.com/explore/tags/[tag-name]/

### Printers ###

It's easiest to add a printer through the administration terminal. Head to `https://[your ip address]:693` and add printers under the administration tab.

Note, if you want your printer to just keep working I recommend setting the Error Policy (in default options) to Abort job.

This script prints to the default printer in the system, so be sure to configure your printer as the default.
