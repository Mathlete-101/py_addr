#!/bin/bash

# Check if a component is specified
if [ -z "$1" ]; then
    echo "Usage: ./install.sh {client|server|pi}"
    exit 1
fi

component="$1"

case $component in
    client)
        cp client.py ~/.local/bin/;
        chmod +x ~/.local/bin/client.py;
        echo "Client installed.";;
    server)
        cp server.py ~/.local/bin/;
        chmod +x ~/.local/bin/server.py;
        echo "Server installed.";;
    pi)
        cp pi.py ~/.local/bin/;
        chmod +x ~/.local/bin/pi.py;
        echo Creating systemd service for pi...;
        echo "[Unit]\nDescription=Send IP Address to Domain\n\n[Service]\nExecStart=/usr/bin/python3 /home/moonpie/.local/bin/pi.py\nRestart=always\nUser=moonpie\n\n[Install]\nWantedBy=default.target" | sudo tee /etc/systemd/system/pi.service;
        sudo systemctl enable pi.service;
        sudo systemctl start pi.service;
        echo "pi installed and service created.";;
    *)
        echo "Unknown component: $component";
        exit 1;;
esac

 with open( " domain.txt" , "w" ) as file: 
     file.write( domain_name )
-e # Prompt for the domain name
read -p "Enter the domain name: " domain_name
echo "" > domain.txt
