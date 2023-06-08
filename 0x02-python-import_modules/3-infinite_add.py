#!/usr/bin/python3

import sys

# Convert arguments to integers and sum them
result = sum(int(arg) for arg in sys.argv[1:])

# Print the result
print(result)

