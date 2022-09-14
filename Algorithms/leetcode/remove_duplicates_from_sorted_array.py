## Mugisha
"""
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums
"""

## Approach
"""

Use two pointers, with the first/left pointer moving over the array one step slower
than the second/right pointer.
- Initialize the two pointers left and right; left starting from 0 and right from 1,
  and a counter variable to keep track of the number frequencies
- Move the left pointer if counter <= 2 and the left pointer value == the right pointer value.
- If counter becomes greater than 2, the left pointer stays at the index where the counter was 2,
- then look for a new value and reset the counter to 1, the next element from the left pointer becomes
  the new right pointer value found
- return the length of the left pointer 'sub-array'.

"""

def removeDuplicates(nums: list) -> int:
    """Removes duplicates while keeping atmost two occurences of the
    duplicate number.
    """
    left_pointer = 0
    counter = 1
    for right_pointer in range(1, len(nums)):
        if nums[left_pointer] == nums[right_pointer]:
            counter += 1
        else:
            counter = 1
        if counter <= 2:
            left_pointer += 1
            nums[left_pointer] = nums[right_pointer]
    return left_pointer + 1  #left pointer count starts at 0 so actual len is +1 of the count. 

    ## Approach2
    '''
    len = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[len-2]:
            nums[len] = nums[i]
            len += 1
    return len
    '''

#if __name__=="__main__":
    #list = [0,0,1,1,1,1,2,3,3]
    #print(removeDuplicates(list))
