#!/bin/bash

sudo mkdir /opt/image
cd /opt/image/
sudo touch swap
sudo dd if=/dev/zero of=/opt/image/swap bs=1024 count=2048000
sudo mkswap /opt/image/swap  
sudo swapon /opt/image/swap 
