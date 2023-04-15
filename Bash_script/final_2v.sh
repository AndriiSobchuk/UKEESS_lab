#!/bin/bash
#set -x
# Define number of packets and time interval
num_packets=5
interval=1

# Read list of IP addresses from file IP.txt
while read ip; do
  # Use ping to check network connection
  echo "Pinging $ip with $num_packets packets and $interval second intervals..."
  #ping -c $num_packets -i $interval $ip

  ping_output=$(ping -c $num_packets -i $interval $ip)
  #echo "$ping_output"

  # Parse ping statistics
  sent=$(echo "$ping_output" | awk '/packets transmitted/ {print $1}')
  received=$(echo "$ping_output" | awk '/packets transmitted/ {print $4}')
  lost=$(echo "$ping_output" | awk '/packet loss/ {print $6}' | tr -d '%')


  echo "TEST $sent and $lost"
  # Calculate percentage of packets lost
  percentage_lost=$(( 100 * lost / sent ))\%
  #percentage_lost="$(echo "scale=2; 100 * $lost / $sent" | bc)%"
  #percentage_lost="$(LC_NUMERIC=en_US.UTF-8 printf "%.2f" "$(echo "scale=2; 100 * $lost / $sent" | bc)" )%"



  # Write log entry
  echo "$(date '+%Y-%m-%d %H:%M:%S'),  $ip,  $sent,  $received,  $lost,  $percentage_lost" >> logs.txt

  # Duplicate ping to visualize (could be commented)
  ping -c $num_packets -i $interval $ip

  # Check ping return code to determine if connection was successful
  if [ $? -eq 0 ]; then
    echo "$ip is reachable"
  else
    echo "$ip is unreachable"
  fi

  echo "---------------------------------------------"
done < IP.txt

