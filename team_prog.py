#!/usr/bin/python3
from modul2 import *
from fibonacci_number import *

if __name__ == '__main__':
    while True:
        n = int(input('Select menu: 1)b2h 2)set 3)fibo 4)exit ? '))
        if (n == 1):
            num = input('input bin number:')
            binTohex(num)
        elif (n == 3):
            fibo = int(input('fibonacci number:'))
            fibonacci_number(fibo)
        elif (n == 4):
            print('exit the program...')
            break
    
