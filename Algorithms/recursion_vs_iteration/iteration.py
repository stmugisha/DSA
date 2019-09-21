# Generating an entire fibonacci sequence upto a given number
from typing import Generator

def fibonacci(x:int)->Generator[int,None,None]:
    yield 0
    if x > 0:
        yield 1 
    last: int = 0   # initializing fibonacci to 0
    next: int = 1   # initializing fibonacci to 1

    for _ in range(1, x):
        '''
        set the last to previous value of next and next to the sum of 
        previous last and next values
        '''
        last, next = next, last + next
        yield next  # generate next number
    return next


if __name__=='__main__':
    for num in fibonacci(0):
        print(num)