#!/usr/bin/env python3

import sys

# Check if the number of arguments is exactly 3 (script name + 2 arguments)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)

# Assign command-line arguments to variables
name = sys.argv[1]
age = sys.argv[2] 

# Print the exact output
print(f"Hi {name}, you are {age} years old.")
