# The bubblesort algorithm

def bubblesort(input: list, pas=True) -> list:
    while pas:
        pas = False
        for i in range(1, len(input)):
            if input[i-1] > input[i]:
                input[i-1], input[i] = input[i], input[i-1]

                pas = True
    return input
if __name__=='__main__':
    print(bubblesort([12,43,4,5,1,3,54,5]))
