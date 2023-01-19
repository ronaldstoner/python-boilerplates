#!/usr/bin/env python3
# python argparse_demo.py 1 -r 'argument' -o 2 -f -l 3 4 5
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Example argparse script')

# Add a required positional argument
parser.add_argument('positional', type=int, help='A positional argument')

# Add a required argument
parser.add_argument('-r', '--required', required=True, type=str, help='A required argument')

# Add an optional argument with a default value
parser.add_argument('-o', '--optional', type=int, default=0, help='An optional argument')

# Add a boolean flag argument
parser.add_argument('-f', '--flag', action='store_true', help='A flag argument')

# Add an argument that takes a list of values
parser.add_argument('-l', '--list', type=int, nargs='+', help='An argument that takes a list of values')

# Parse the command line arguments
args = parser.parse_args()

# Print the parsed arguments
print(f'Positional argument: {args.positional}')
print(f'Required argument: {args.required}')
print(f'Optional argument: {args.optional}')
print(f'Flag argument: {"True" if args.flag else "False"}')
print(f'List argument: {args.list}')
