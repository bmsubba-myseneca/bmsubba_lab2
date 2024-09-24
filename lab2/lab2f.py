#!/usr/bin/env python3
# Author: Budhi Maya Subba
# Author ID: 133270231 _ bmsubba
# Date Created: 2024/09/24

import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <timer>")
    sys.exit(1)

# Assign the argument to the timer object
try:
    timer = int(sys.argv[1])
except ValueError:
    print(f"Error: Argument must be an integer.")
    sys.exit(1)

# While loop that counts down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# After the loop ends, print "blast off!"
print("blast off!")

