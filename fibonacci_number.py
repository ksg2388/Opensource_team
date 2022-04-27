#!/usr/bin/python3

def fibonacci_number(num):
    fibonacci=[]
    for i in range(num):
        if i==0:
            fibonacci.append(1)
        elif i==1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    #print fibonacci sequence
    for i in range(num):
        print(fibonacci[i], end=' ')
    print()

    print("F%d = %d" %(num,fibonacci[num-1]))

if __name__ == '__main__':
    num = int(input("fibonacci_number: "))
    fibonacci_number(num)

