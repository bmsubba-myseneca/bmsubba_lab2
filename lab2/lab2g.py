#!/usr/bin/env python3
# Author: Budhi Maya Subba
# Author ID: 133270231
# Date Created: 2024/09/24

import sys

# Check if the number of arguments is correct
if len(sys.argv) == 2:
    try:
        # Assign the argument to the timer object
        timer = int(sys.argv[1])
    except ValueError:
        print("Error: Argument must be an integer.")
        sys.exit(1)
elif len(sys.argv) == 1:
    # If no arguments are passed, default timer value to 3
    timer = 3
else:
    print(f"Usage: {sys.argv[0]} [timer]")
    sys.exit(1)

# While loop that counts down from the timer value to 1
while timer > 0:
    print(timer)
    timer -= 1

# After the loop ends, print "blast off!"
print("blast off!")
