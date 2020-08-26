nums = []
stop_word = 'done'
def prompt_input(message: str):
    """ Prompt user for input."""
    while True:
        try:
            num = input(message+':\n')
            if num==stop_word:
                print(f'Max: {max(nums)} Min: {min(nums)}')
            else:
                nums.append(int(num))
                continue
        except ValueError:
            print('Invalid Argument supplied')
            continue
        else:
            break

if __name__=='__main__':
    prompt_input('Enter any number')
