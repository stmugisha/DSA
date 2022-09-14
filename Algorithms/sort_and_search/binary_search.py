def search(nums: list, low, high, target: int) -> int:
    """Recursive binary search.
    """
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
    """Iterative binary search.
    """
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
    


if __name__=='__main__':
    arr = [12,43,4,5,1,3,54,5]
    print(search(arr, 0, len(arr)-1, 12))
