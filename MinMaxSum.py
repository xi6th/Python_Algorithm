"""
    Problem 1: Find the minimum number 
    Problem 2: Find the maximum number 
    Problem 3: Print the out put

    Set 1: arange the array in various sequence 
    step 2: find the posibile max number
"""


def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))


arr = [1, 2, 6, 4, 46,89,5]
miniMaxSum(arr)