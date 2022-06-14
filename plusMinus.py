#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
    Step 1: Calculate the ration of elements that are 
        1.positive
        2. negative 
        3. zero
    Step 2: Print the decimal value of each fraction on a new line with 6 decimal point
"""


def plusMinus(arr):
    # Write your code here
    position = 0
    positive = []
    zero = []
    negative = []

    #Set a for loop to iterate over the list of numbers
    for numbers in arr:
        if numbers > 0:
            positive.append(numbers)
        elif numbers == 0:
            zero.append(numbers)
            # print("{:.6f}".format(zero_ratio))
        elif numbers < 0:
            negative.append(numbers)
            # print("{:.6f}".format(negative_ratio))

    positive_ratio = len(positive)/len(arr)
    zero_ratio = len(positive)/len(arr) 
    negative_ratio = len(negative)/len(arr)
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))
        # if position == len(arr):
        #     return ("Number not found")
        
    # return positive_ratio,zero_ratio,negative_ratio
    # print("{:.6f}".format(positive_ratio))
    # print("{:.6f}".format(negative_ratio))
    # print("{:.6f}".format(zero_ratio))
arr = [1, -2, -7, 9, 1, -8, -5]

print(plusMinus(arr))
