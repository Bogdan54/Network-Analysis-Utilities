#!/bin/bash

# Read input from the user for proxy domain, IP, and credentials
read -p "Enter the proxy domain: " PROXY_DOMAIN
read -p "Enter the proxy IP: " PROXY_IP
read -p "Enter the proxy username: " PROXY_USER
read -p "Enter the proxy password: " PROXY_PASSWORD

# Construct the proxy URL
PROXY_URL="http://${PROXY_DOMAIN}:${PROXY_IP}/"

# Read input from the user for the URL to test
read -p "Enter the URL to test: " URL

# Use wget to check the proxy
wget -q --proxy-user="$PROXY_USER" --proxy-password="$PROXY_PASSWORD" --spider --proxy="$PROXY_URL" "$URL"

# Check the exit status of wget
if [ $? -eq 1 ]; then
    STATUS="Proxy isn't working"
else
    STATUS="Proxy is working."
fi

# Print the result
echo $STATUS
