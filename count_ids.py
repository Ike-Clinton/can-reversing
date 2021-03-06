#! /usr/bin/python3
# count_ids.py
# By Ike Clinton
# Python script to count CAN frame IDs from a log file
# Can logs are of the form:
# (timestamp) interface ID#FFFFFFFFFFFFFFFF
# Where timestamp is of the form: 0000000000.000000
# Where interface is usually one of vcan0 or can0
# Where frame ID is 3 hex chars: FFF
# and the data length is up to 8 bytes in hex following a pound sign
# Example:
# (1436509053.650713) vcan0 19E#6FE1CB7DE2218456
import argparse
from collections import Counter
import os.path
import sys

# Override Argument parser to throw error and generate help message
# if undefined args are passed
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

# Create argparser object to add command line args and help option
parser = MyParser(
	description = 'This program takes in a a CAN data log file as input and prints'
	+ ' the unique can IDs that it finds',
	epilog = '',
	add_help = True)

# Add a "-i" argument to receive a filename
parser.add_argument("-i", action = "store", dest="file",
					help = "log file to read in")

# Print help if no args are supplied
if len(sys.argv)==1:
	parser.print_help()
	sys.exit(1)

# Split and process arguments into "args"
args = parser.parse_args()

# Check that filename is not blank
if args.file == '':
	print("ERROR: File name must not be blank")
	parser.print_help()
	sys.exit(1)

# Make sure file exists
if os.path.isfile(args.file) == False:
	print("ERROR: File does not exist")
	parser.print_help()
	sys.exit(1)

# Open the file as read only, read the lines into text
with open(args.file, 'r') as myfile:
	text = myfile.readlines()

# Strip newlines, and split on spaces
# Select the first 3 characters (the frame ids) and count them
# Finally, use most_common() to display them decreasing order
c = Counter(l.strip().split()[2][0:3] for l in text[0:len(text)-1])
for x in c.most_common():
	print(x)
