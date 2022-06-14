from collections import Counter


def longestSubarray(arr):
    # Write your code here
    list_counted = Counter(arr).__getattribute__()
    print(list_counted)
    # list_counted = arr
    # numbers_counted = []
    # for list_files in list_counted:
    #     counted = list_files
    #     count_again = arr.count(counted)
    #     numbers_counted.append(counted)
    #     print(counted,count_again)

arr = [5,1,2,3,4,5,4]
longestSubarray(arr)