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
