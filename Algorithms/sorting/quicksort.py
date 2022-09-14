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
