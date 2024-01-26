# Network Analysis Utilities

## IP Analysis script

### Description
This Python script analyzes a list of IP addresses provided in an input file to determine the best-performing IP address based on average round-trip time and TTL (Time To Live) values. It utilizes the ping command to measure network latency and extracts relevant information for comparison.

### Usage

python script.py <input_file> 
Replace '<input_file>' with the path to the file containing a list of IP addresses to be analyzed.

### Requirements

* Python 3.x
* The script uses the ping command, which should be available in the system's command-line environment.

### Output

The script displays the best IP address, its average round-trip time, and TTL in the terminal. Additionally, the results are written to a timestamped output file (best_ip_<timestamp>.txt).


