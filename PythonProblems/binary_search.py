data = [2,4,5,7,8,9,12,14,17,19,22,25,27,33,37]
target = 28

# linear search: each item through list

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# binary search solves it in log(n) time
# iterative Binary search
# take advantage of the list being sorted
# split the list in half. is the element we are looking for greater than or less than target?

def binary_search_iterative(data,target):
    low = 0
    high = len(data) - 1 #the minus 1 is important

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

# Recursive binary search

def binary_search_recursive(data, target, low, high):

#check whether the low point is higher than the high point

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))
