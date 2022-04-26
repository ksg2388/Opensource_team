# modul2.py
# bin-to-hex conversion

def binTohex(bin): #2진수
    intNum = int(bin)
    hexNum = hex(intNum)
    return hexNum

if __name__ == '__main__':
    print("테스트코드")
    bin = input("input bin number: ")
    print("hexa number:",binTohex(bin))