def aVeryBigSum(ar):
    # Write your code here
    for x in ar:
        x = sum(ar)
    return x

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))
# print(ar)