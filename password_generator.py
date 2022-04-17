'''
Author : Pooya Naderpour 
'''
from string import ascii_letters,digits
from random import shuffle,choice

all = list(ascii_letters + digits + '@#$%^')

def random_pass_generator():
    '''
    This function create random passwords with ideal quantity and length
    '''
    passwords = []
    while True:
        try:
            quantity = int(input('How many password do you wanna generate: '))
            length = int(input('Please enter the passwords length: '))
            break
        except(ValueError):
            print('Please enter only integer number for quantity and length of passwords')
        except(KeyboardInterrupt):
            print('\nProgram stopped.')
            break
        except:
            print('Wrong format!')
    shuffle(all)
    for _ in range(quantity):
        password_chars = []
        for _ in range(length):
            password_chars.append(choice(all))
        shuffle(password_chars)
        password = ''.join(password_chars)
        passwords.append(password)
    for index,item in enumerate(passwords):
        print(f'#{index} --> {item}')
    while True:
        try:
            save = input('Do you wanna save passwords into a .txt file: ')
            save.lower()
            break
        except(ValueError):
            print('Please answer with yes or no!')
        except(TypeError):
            print('Do not enter integer or float value!')
        except(KeyboardInterrupt):
            break
    if save == 'y' or save == 'yes' or save == '1':
        with open('pwlist_log.txt','a') as file:
            for item in passwords:
                file.writelines(item+'\n')
            print('Passwords saved.')
    elif save == 'n' or save == 'no' or save == '0':
        pass
    else:
        print('format of input value is not correct so program cannot create log file.')
# call function
random_pass_generator()