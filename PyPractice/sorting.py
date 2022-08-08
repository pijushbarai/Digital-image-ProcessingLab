
def main():
    str = input()
    l = list(str)
    low=[]
    up = []
    digit = []
    for i in l:
        if(i >= 'a' and i <= 'z'):
            low.append(i)
        elif(i >= 'A' and i <= 'Z'):
           up.append(i)
        else :
            digit.append(i)
    low.sort()
    up.sort()
    digit.sort()
    for i in low:
        print(i,end='')
    for i in up:
        print(i,end='')
    for i in digit:
        print(i,end='')
    print()
main()