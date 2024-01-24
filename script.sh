#!/bin/bash

# Check if the input file argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file="$1"
output_file="best_ip_$(date +'%Y%m%d_%H%M%S').txt"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

# Initialize variables
best_ip=""
best_avg_time=999999
best_ttl=255

# Display loading screen
echo -n "Processing"

for i in {1..5}; do
    sleep 0.5
    echo -n "."
done

echo ""

# Loop through each IP address in the input file
while IFS= read -r ip_address; do
    # Perform the ping and extract the average round-trip time and TTL value
    ping_result=$(ping -c 5 "$ip_address" 2>/dev/null | grep "rtt min/avg/max/mdev" | awk '{print $4}' | cut -d '/' -f 2)
    ttl_result=$(ping -c 1 "$ip_address" 2>/dev/null | grep "ttl" | awk '{print $6}')

    # Check if the ping was successful
    if [ -n "$ping_result" ] && [ -n "$ttl_result" ]; then
        # Compare average round-trip time and TTL with the best values so far
        if [ "$(echo "$ping_result < $best_avg_time" | bc -l)" -eq 1 ] || [ "$(echo "$ping_result == $best_avg_time && $ttl_result < $best_ttl" | bc -l)" -eq 1 ]; then
            best_ip="$ip_address"
            best_avg_time="$ping_result"
            best_ttl="$ttl_result"
        fi
    else
        echo "Ping failed for $ip_address"
    fi
done < "$input_file"

# Display the best results in the terminal
echo "Best IP Address: $best_ip"
echo "Best Average Round-Trip Time: $best_avg_time ms"
echo "Best TTL: $best_ttl"

# Output the best IP address, average time, and TTL to the output file
echo "Best IP Address: $best_ip" > "$output_file"
echo "Best Average Round-Trip Time: $best_avg_time ms" >> "$output_file"
echo "Best TTL: $best_ttl" >> "$output_file"

echo "Script completed. Results written to $output_file"
