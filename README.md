# Network Analysis Utilities

## Overview
This repository contains tools for IP address analysis and testing proxy servers. The structure is organized as follows:

- **ip-analysis:** Tools for analyzing a list of IP addresses.
  - `ip-analysis_gui.py`: Python script with a graphical user interface for IP address analysis.
  - `ip-test.py`: Python script for analyzing IP addresses and determining the best-performing one based on network latency and TTL.
  - `ip_adresses.txt`: Sample input file containing a list of IP addresses.
  - `README.md`: Instructions and information related to the IP address analysis tools.

- **proxy-test:** Tools for testing proxy servers.
  - `proxy_test.py`: Python script for testing the functionality of a proxy server using provided details and a target URL.
  - `README.md`: Instructions and information related to the proxy server testing tool.

- **bash:**
  - **ip-analysis:**
    - `script.sh`: Bash script counterpart for `ip-test.py` that uses the ping command to measure network latency and determines the best-performing IP address.
    - `ip_adresses.txt`: Sample input file containing a list of IP addresses.
  - **proxy-server-testing:**
    - `script.sh`: Bash script counterpart for `proxy_test.py` that tests the functionality of a proxy server using provided details and a target URL.

## Instructions

### IP Analysis

#### Python Script (`ip-analysis_gui.py`)

1. Ensure you have Python installed on your system.
2. Run the script using the command: `python ip-analysis_gui.py`.
3. Use the graphical user interface to load an input file and analyze IP addresses.

#### Python Script (`ip-test.py`)

1. Ensure you have Python installed on your system.
2. Edit the `ip_adresses.txt` file with the list of IP addresses you want to analyze.
3. Run the script using the command: `python ip-test.py`.
4. The script will determine the best-performing IP address based on network latency and TTL.

#### Bash Script (`script.sh`)

1. Ensure you have Bash and the ping command installed on your system.
2. Edit the `ip_adresses.txt` file with the list of IP addresses you want to analyze.
3. Run the script using the command: `bash script.sh`.
4. The script will determine the best-performing IP address based on network latency and TTL.

### Proxy Server Testing

#### Python Script (`proxy_test.py`)

1. Ensure you have Python installed on your system.
2. Edit the `proxy_test.py` script with the proxy details and target URL you want to test.
3. Run the script using the command: `python proxy_test.py`.
4. The script will test the functionality of the proxy server.

#### Bash Script (`script.sh`)

1. Ensure you have Bash installed on your system.
2. Edit the `script.sh` file with the proxy details and target URL you want to test.
3. Run the script using the command: `bash script.sh`.
4. The script will test the functionality of the proxy server.

## Note
- These tools are designed for analyzing IP addresses and testing proxy servers, providing flexibility for both Python and Bash environments.
- Customize input files and script parameters based on your specific use case.

