'''
Recursion is a programming technique/style of writing functions that call themselves.
Recursive functions comprise of a base case and a recursive case
The fibonacci sequence is one numerical sequence that recursion can be applied to. i.e
the fibonacci is a sequence of numbers such that any given number is the sum of the previous two numbers.
'''
def fibonacci(x: int) -> int:
    '''
    Computes the fibonacci of a given number x
    Arguments: x; an integer 
    Returns: The fibonacci number of x
    '''
    if x < 2: # the base case
        return x
    return fibonacci(x-2) + fibonacci(x-1) # the recursive case



# Invoking the function
if __name__=='__main__':
    print(fibonacci(10))