'''
Step 1: find the maximum number
Step 2: Divide the maximum number by the total cores 
Step 3: Sort the list in order format and sum it up
'''

def minTime(files, numCores, limit):
    # Write your code here
    list_files = []
    for file in files:
        list_files.append(file)
    sorted_list = sorted(list_files)
    maximum_number = max(sorted_list)
    remove_maximum_number = list(sorted_list[:-1])
    s = numCores % limit == 0
    if s == True:
         remove_maximum_number = list(sorted_list[:-1])
         remove_maximum_number.append(s)
         minimum_time = sum(sort_again)
    if numCores <= 1:
        minimum_time = sum(sorted_list)
    else:
        divide_max_numCores = int(maximum_number/limit)
        remove_maximum_number.append(divide_max_numCores)
        sort_again = sorted(remove_maximum_number)
        minimum_time = sum(sort_again)

    return minimum_time

files = [3,5,3,10,5,5]
numCores = 1
limit = 5

print(minTime(files, numCores, limit))

