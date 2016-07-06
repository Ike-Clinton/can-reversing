#!/bin/bash
# Display usage parameters
display_usage() {
	echo -e "\nUsage: \nsudo $0 \n"
}

if [ $# -ne 1 ]
then
	display_usage
	exit 1
fi
# Check if user supplies --help or --h and show usage
if [[ ( $# == "--help") || $# == "-h" ]]
then
	display_usage
	exit 0
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    cansend can0 $line
done < "$1"