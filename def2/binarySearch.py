from functools import lru_cache

@lru_cache()
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(50))

import random
nums = [random.randint(0,20) for i in range(20)]
print(sorted(nums))

def binarySearch(aList, num):
    aList.sort()
    while aList:
        mid = len(aList) // 2
        if aList[mid] == num:
            return True
        elif aList[mid]>num:
            aList = aList[:mid]
        elif aList[mid] < num:
            aList = aList[mid+1:]
    return False
print(sorted(nums))
print(binarySearch(nums, 3))

        