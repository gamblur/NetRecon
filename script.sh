#!/bin/sh
DOMAIN=nashermiles.com
echo $DOMAIN
echo "Starting Sublist3r...."
python /root/Sublist3r/sublist3r.py -d $DOMAIN -b -p 80,443,21,20 -v -t 50 -o ${DOMAIN}_sub_domain.txt
echo "Starting DNSMap...."
dnsmap $DOMAIN -c ${DOMAIN}_sub_domain1.txt
echo "Starting dnsrecon...."
dnsrecon -d $DOMAIN -v -w -z --threads 50 --lifetime 5 -n NS_SERVER --csv ${DOMAIN}_sub_domain2.csv