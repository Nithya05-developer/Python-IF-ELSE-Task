# Python-IF-ELSE-Task
import math
import os
import random
import re
import sys

# Read input from user
n = int(input().strip())

# Check constraints
if n % 2 != 0:
    # If n is odd
    print("Weird")
else:
    # If n is even
    if 2 <= n <= 5:
        # If n is even and in the range of 2 to 5 (inclusive)
        print("Not Weird")
    elif 6 <= n <= 20:
        # If n is even and in the range of 6 to 20 (inclusive)
        print("Weird")
    elif n > 20:
        # If n is even and greater than 20
        print("Not Weird")
