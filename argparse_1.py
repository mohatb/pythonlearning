#!/usr/bin/env python3
import argparse

#build the parse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int , help='the file to read')
parser.add_argument('--version', '-v' , help='Print the tool version', action='version', version='%(prog)s 1.2')

args = parser.parse_args()

print(args)

#Parse the arguments

# read the file, reverse the content and print.
