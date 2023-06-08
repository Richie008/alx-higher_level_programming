#!/usr/bin/python3

import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
print(f"Number of argument(s): {num_args}")

if num_args > 0:
    # Print "argument" or "arguments" based on the number
    plural = "s" if num_args > 1 else ""

    # Print a colon if there are arguments, otherwise print a dot
    end_char = ":" if num_args > 0 else "."

    print(f"Argument{plural}{end_char}")

    # Print each argument and its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

