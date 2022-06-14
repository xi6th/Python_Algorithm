from collections import Counter
from traceback import print_tb

from numpy import arange

# def compareList(l1,l2):
#     l1.sort()
#     l2.sort()
#     if(l1==l2):
#       return "Equal"
#     else:
#       return "Non equal"
#     return "Equal" if (l1==l2) else "Non equal"

# def sockMerchant(n, ar):
#     # Write your code here
#     total_count = n
#     c = []
#     duplicate_count = [item for item, count in Counter(ar).items() if count > 1]
#     for x in duplicate_count:
#         t = [ar.count(x)]
#         for countd in t:
#             c.append(countd)
#             for w in c:
#               b = w %2
#               print(b)
#     # for d in duplicate_count:
#     #     if d in ar:
#     #         counts = Counter(ar)
#     #         print(d)
# #     empty_list = []
# #     if ar:
# #         empty_list = [ar]
# #         for x in empty_list:
# #             return x
# #  [ar] if ar else []
# #     return x
    


def sockMerchant(n, ar):
  arrays = []
  arrays.append(ar)
  duplicate_count = [item for item, count in Counter(ar).items() if count > 1]
  for x in ar:
      if x in duplicate_count:
        pairs = x
        list_pairs = []
        list_pairs.extend(pairs)
        print(list_pairs)
n = 9

ar = [10, 20, 20, 10, 10, 30,30,30,0,50, 50, 10, 20]

result = sockMerchant(n, ar)
print(result)