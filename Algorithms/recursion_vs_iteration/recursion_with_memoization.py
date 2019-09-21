'''
Memoization is a process of storing the results of completed computations
so that they can be looked up in a storage location instead of re-computing them.
'''
from typing import Dict

memory: Dict[int,int] = {0:0, 1:1} # the base cases

def fibonacci(x: int) -> int:
    '''
    Computes the fibonacci of a given number x
    Arguments: x; an integer 
    Returns: The fibonacci number of x
    '''
    if x not in memory:
        memory[x] = fibonacci(x-1) + fibonacci(x-2)
    return memory[x]


# Automatic memoization using the lru_cache decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(x: int) -> int:
    '''
    Computes the fibonacci of a given number x
    Arguments: x; an integer 
    Returns: The fibonacci number of x
    '''
    if x < 2:
        return x
    return fib(x-2) + fib(x-1)


if __name__=='__main__':
    print(f'The fibonacci of 10 is: {fibonacci(10)}')
    print(f'The fibonacci of 5 is: {fib(5)}')