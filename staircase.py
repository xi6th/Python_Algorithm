"""
    Problem 1: Find the total len of the number
    Problem 2: 
"""

def staircase(n):
    position = 0
    total_len = n
    for i in range(1, n+1):
        print(''*(total_len-1)+'#'*i)
    # Write your code here


n = 6
print(staircase(n))