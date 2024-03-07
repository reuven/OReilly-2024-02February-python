def get_input():
    s = input('Enter something: ').strip()
    return s

def get_choice(choices):
    while True:
        s = input(f'Choose from {choices}: ').strip()
    
        if s in choices:   # did the user choose something from choices?
            return s
    
        print(f'{s} is invalid; try again')
        