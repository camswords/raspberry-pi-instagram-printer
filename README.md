# raspberry-pi-instagram-printer #

### Installation ###

#### Initial Pi setup ####

1. Download the latest raspbian instance from https://www.raspberrypi.org/downloads/
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

#### Installation ####

1. On the Pi, type `vi ~/.profile`, go into insert mode using `i` and type the following:
  * `export INSTAGRAM_CLIENT_ID=[your instagram client id]`
  * `export INSTAGRAM_CLIENT_SECRET=[your instagram client secret]`
  * Then hit `ESC`, then `:wq` and press `ENTER` to save the file.
1. So you can use the environment variables from the previous step without a restart, at the bash prompt type `source ~/.profile`.
1. Install the code using `sudo bash < <(curl https://raw.githubusercontent.com/camswords/raspberry-pi-instagram-printer/master/install.sh)`

Note: if you dont have a instagram client id / secret, see http://instagram.com/developer.

Note: this has been tested using 2015-09-24-raspbian-jessie.

### Is it working? ###

You can check the tags on instagram here: https://instagram.com/explore/tags/[tag-name]/

### Printers ###

#### add a printer ####
It's easiest to add a printer through the administration terminal. Head to `https://[your ip address]:693` and add printers under the administration tab.

#### What printers are available ####
Run `lpstat -p -d` to find the available and the default printers.
