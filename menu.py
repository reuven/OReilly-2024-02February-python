def get_input():
    s = input('Enter something: ').strip()
    return s

def get_choice(choices):
    while True:
        s = input(f'Choose from {choices}: ').strip()
    
        if s in choices:   # did the user choose something from choices?
            return s
    
        print(f'{s} is invalid; try again')

# the below code will *not* run when we import the module!
# but it will run if we execute the module as a program

if __name__ == '__main__':
    user_choice = get_choice(['a', 'b', 'c'])
    print(f'User chose {user_choice}')