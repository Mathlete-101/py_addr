#!/bin/bash

# Stop the systemd service
sudo systemctl stop pi.service

# Disable the service from starting on boot
sudo systemctl disable pi.service

# Remove the systemd service file
sudo rm /etc/systemd/system/pi.service

# Remove the script from the local bin directory
rm ~/.local/bin/pi.py
