#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

"""

Steps 1: Roundup if the grade next multiple of 5 is less than 3
Step 2: Create a muplple of 5 

Expectation: Grades after rounding as appropriate

"""

def gradingStudents(grades):
    # Write your code here
    multiple_of_five = []
    for x in range(0,100,5):
         multiple_of_five.append(x)
    if grades == multiple_of_five:
        print(grades)
    print(multiple_of_five)


grades = [4,73,67,38,75,33]


gradingStudents(grades)