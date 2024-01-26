import subprocess
import time
from datetime import datetime
import re

def display_loading_screen():
    print("Processing", end='', flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print()

def extract_ping_results(ip_address):
    try:
        ping_result = subprocess.check_output(["ping", "-c", "5", ip_address], stderr=subprocess.DEVNULL, text=True)
        avg_time_match = re.search(r'rtt min/avg/max/mdev = [^/]*/([^/]*)/', ping_result)
        ttl_match = re.search(r'ttl=([0-9]+)', ping_result)

        if avg_time_match and ttl_match:
            avg_time = float(avg_time_match.group(1))
            ttl_result = int(ttl_match.group(1))
            return avg_time, ttl_result

    except subprocess.CalledProcessError:
        print("Ping failed for {}".format(ip_address))

    return None, None

def main():
    # Check if the input file argument is provided
    import sys
    if len(sys.argv) == 1:
        print("Usage: {} <input_file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "best_ip_{}.txt".format(datetime.now().strftime('%Y%m%d_%H%M%S'))

    # Check if the input file exists
    import os
    if not os.path.isfile(input_file):
        print("Error: Input file '{}' not found.".format(input_file))
        sys.exit(1)

    # Initialize variables
    best_ip = ""
    best_avg_time = 999999
    best_ttl = 255

    # Display loading screen
    display_loading_screen()

    # Loop through each IP address in the input file
    with open(input_file, 'r') as file:
        for ip_address in file:
            ip_address = ip_address.strip()

            # Perform the ping and extract the average round-trip time and TTL value
            avg_time, ttl_result = extract_ping_results(ip_address)

            if avg_time is not None and ttl_result is not None:
                # Compare average round-trip time and TTL with the best values so far
                if avg_time < best_avg_time or (avg_time == best_avg_time and ttl_result < best_ttl):
                    best_ip = ip_address
                    best_avg_time = avg_time
                    best_ttl = ttl_result

    # Display the best results in the terminal
    print("Best IP Address:", best_ip)
    print("Best Average Round-Trip Time: {} ms".format(best_avg_time))
    print("Best TTL:", best_ttl)

    # Output the best IP address, average time, and TTL to the output file
    with open(output_file, 'w') as file:
        file.write("Best IP Address: {}\n".format(best_ip))
        file.write("Best Average Round-Trip Time: {} ms\n".format(best_avg_time))
        file.write("Best TTL: {}\n".format(best_ttl))

    print("Script completed. Results written to {}".format(output_file))

if __name__ == "__main__":
    main()
