# credit: stanford cs231n
# Quicksort implementation in python
# Find explanation of the algorithm in the readme

def quicksort(input: list) -> list:
    """ Sorts an input list/array in ascending order
        Args:
            input: A list of integers to be sorted.
    """
    
    if(len(input) <= 1):
        return input
    
    pivot = input[len(input) // 2]  #using list median as the pivot
    
    left = [i for i in input if i < pivot]
    mid = [i for i in input if i == pivot]
    right = [i for i in input if i > pivot]
    return quicksort(left) + mid + quicksort(right)

if __name__=='__main__':
    print(quicksort([12,43,4,5,1,3,54,5]))
