# README for IP Address Management Script

## Overview
This project consists of a Python script that retrieves the local machine's IP address and sends it to a specified domain via a TCP socket. It also includes bash scripts for installation and uninstallation, with the installation script setting up the Python script as a systemd service to run at startup.

## Requirements
- Python 3 with socket module
- Linux distribution with systemd

## Installation
nYou will be prompted to enter the domain name for the pi script during the installation process.

nYou will be prompted to enter the domain name for the pi script during the installation process.

nYou will be prompted to enter the domain name for the pi script during the installation process.

You can use the provided 'install.sh' script to copy the Python script and create the systemd service. Run the following commands to install one of the components:

    ./install.sh {client|server|pi}

## Uninstallation
If you wish to remove the service and the Python script, you can use the provided 'uninstall.sh' script. Run the following command:

    ./uninstall.sh

## Configuration
n## Domain Name Configuration
- The domain name for the pi script will be prompted during installation.
- The domain name for the client script will be provided at runtime.

n## Domain Name Configuration
- The domain name for the pi script will be prompted during installation.
- The domain name for the client script will be provided at runtime.

n## Domain Name Configuration
- The domain name for the pi script will be prompted during installation.
- The domain name for the client script will be provided at runtime.
- The domain name to which the IP address will be sent should be replaced in the 'pi.py' script at the variable definition.

domain_name = ''  # Fill in the domain name

## Usage
- The Python script will run in a loop, sending the current IP address to the specified domain every 10 seconds until it receives a success response.

## Stopping the Service
If you need to stop the service manually:
1. Stop the systemd service:
   sudo systemctl stop pi.service
2. Disable the service:
   sudo systemctl disable pi.service

## License
This is free and unencumbered software released into the public domain. For more information, please refer to [UNLICENSE](https://unlicense.org/)
