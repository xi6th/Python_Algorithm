#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

# def designerPdfViewer(h, word):
#     letters = list(string.ascii_lowercase)
#     words = []
#     height = []
#     length_of_word = len(word)
#     for w in word:
#         relative_position = letters.index(w)
#         words.append(relative_position)
#     for i in words:
#         index_item = h[i]
#         height.append(index_item)

#     # Write your code here
#     maximum_letter = max(height)
#     total_height = (length_of_word * 1) * maximum_letter
#     print(total_height)

# h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
# word = ["abcy"]

# designerPdfViewer(h,word)




def designerPdfViewer(h, word):
    letters = list(string.ascii_lowercase)
    words = []
    height = []
    length_of_word = len(word)
    for w in word:
        relative_position = letters.index(w)
        words.append(relative_position)
    for i in words:
        index_item = h[i]
        height.append(index_item)

    # Write your code here
    maximum_letter = max(height)
    total_height = (length_of_word * 1) * maximum_letter
    return(total_height)

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word = "abcy"

print(designerPdfViewer(h,word))