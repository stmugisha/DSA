# credit: stanford cs231n
# Quicksort implementation in python
# Find explanation of the algorithm in the readme

def quicksort(input_: list) -> list:
    """ Sorts an input list/array in ascending order
        Args:
            input: A list of integers to be sorted.
    """
    
    if(len(input_) <= 1):
        return input_
    
    pivot = input_[len(input_) // 2]  #using list median as the pivot
    
    left = [i for i in input_ if i < pivot]
    mid = [i for i in input_ if i == pivot]
    right = [i for i in input_ if i > pivot]
    return quicksort(left) + mid + quicksort(right)


def search(nums: list, low, high, target: int) -> int:
    if high > low:
        mid_point = (high - low) // 2
        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] > target:
            return search(nums, low, mid_point-1, target)
        else:
            return search(nums, mid_point+1, high, target)
    else:
        return -1

def binary_search(nums: list, target: int) -> int:
    """Iterative binary search."""
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid_point = (high + low)//2
        if nums[mid_point] < target:
            low = mid_point + 1
        elif nums[mid_point] > target:
            high = mid_point - 1
        else:
            return mid_point
    return -1

class Solution:
    def sortedSquares(self, nums: list) -> list:
        import math
        if len(nums) <= 1:
            nums = [int(math.pow(i, 2)) for i in nums]
            return nums
        else:
            pivot = nums[len(nums) // 2]
            left = [i for i in nums if i < pivot]
            mid = [i for i in nums if i==pivot]
            right = [i for i in nums if i > pivot]
            return self.sortedSquares(left) + mid + self.sortedSquares(right)
        

if __name__=='__main__':
    #arr = [12,43,4,5,1,3,54,5]
    #print(search(arr, 0, len(arr)-1, 12))
    cl = Solution()
    print(cl.sortedSquares([-4,-1,0,3,10]))


