import random
from os import system, name

random.seed()
roles = ['top', 'mid', 'jungle', 'adc', 'support', 'fill']


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

t = random.sample(roles,2)
if(t[0] == 'fill'):
    print('fill')
else: print(' '.join(t))


while 1:
    x = input()
    if x == '':
        clear()
        t = random.sample(roles,2)
        if(t[0] == 'fill'):
            print('fill')
        else: print(' '.join(t))

    if x == 'exit':
        break
