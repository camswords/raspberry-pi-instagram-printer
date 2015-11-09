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
