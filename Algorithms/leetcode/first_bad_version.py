# Author: Stephen Mugisha
"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


def firstBadVersion(n: int) -> int:
    """First bad version using binary search."""
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if isBadVersion(start): #isBadVersion defined in the leetcode test backend
            return start
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    else:
        return start