#!/usr/bin/python3
# modul2.py
# bin-to-hex conversion

def binTohex(bin): #2진수
    intNum = int(bin,2)
    hexNum = hex(intNum)
    return print("hexa number:",hexNum)

if __name__ == '__main__':
    print("테스트코드")
    bin = input("input bin number: ")
    binTohex(bin)
