


def decimalToBinary(n):
    return bin(n).replace("0b", "")
def decimalToHex(n):
    return hex(n).replace("0x","")
def decimalToOctal(n):
    return oct(n).replace("0o","")


def main():
    n = int(input())
    for i in range(1,n+1):
        print(i," ",decimalToOctal(i)," " , decimalToHex(i)," ",decimalToBinary(i))

main()