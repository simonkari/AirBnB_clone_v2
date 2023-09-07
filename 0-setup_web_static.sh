#!/usr/bin/env bash
# This script configures an Nginx server with specified folders and files.

# Update the package repository to fetch the latest package information
sudo apt-get -y update

# Upgrade the installed packages to their latest versions
sudo apt-get -y upgrade

# Install the Nginx web server
sudo apt-get -y install nginx

# Create directories for the web application's static content
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create an index.html file with the content "Holberton School" in the specified location
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to make 'test' the current version of the web application
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change the ownership of the directories and files to 'ubuntu:ubuntu'
sudo chown -hR ubuntu:ubuntu /data/

# Define an Nginx location block configuration in the 'default' site configuration file
conf="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "45i $conf" /etc/nginx/sites-available/default

# Start the Nginx service
sudo service nginx start

# Restart the Nginx service to apply the configuration changes
sudo service nginx restart

# Reload the Nginx configuration to activate the new location block
sudo service nginx reload
