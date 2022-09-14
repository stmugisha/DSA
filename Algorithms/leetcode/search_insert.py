"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

def searchInsert(nums: list, target: int) -> int:
    #if target not in nums:
     #   nums.append(target) }-> O(nlogn) if doing a linear search and insert first
      #  nums.sort()
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
                

## Minimum-sum-of-four-digit-number-after-splitting-digits
'''
You are given a positive integer num consisting of exactly four digits.
Split num into two new integers new1 and new2 by using the digits found in num.
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3.
Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2
'''

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [i for i in str(num)]
        pairs = [0,0,0,0]
        counter = 0
        a = 0
        b = 0
        while num > 0:
            pairs[counter] = num % 10
            num = num // 10
            counter += 1
        pairs = sorted(pairs)
        a = pairs[0] * 10 + pairs[3]
        b = pairs[1] * 10 + pairs[2]
        #print(a,b)
        return a+b
        
