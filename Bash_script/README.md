TASK: 
Scan Hosts: Write a Bash script that performs a network health check by pinging a list of hosts and logging the results to a file. The script should prompt the user for the name
of the file containing the list of hosts, the number of ping packets to send, and the time interval between ping packets. The script should output a message for each host indicating whether the ping was successful or not and log the results to a file. The log file should contain the timestamp, the host name or IP address, the number of packets sent, the number of packets received, and the percentage of packets lost.

Description:
- to scan hosts, please, fill it in file IP.txt
- to launch host scanning run one of the bash files final_1v.sh or final_2v.sh (the only difference is output format) which will read the list of IP addresses from IP.txt file
