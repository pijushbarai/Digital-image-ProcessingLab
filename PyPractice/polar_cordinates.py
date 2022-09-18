import cmath
from itertools import count
def main():
    s = input()
    l = len(s)
    dec = 0
    x = 0.0
    for i in reversed(range(l-1)):
        if(s[i] == '-'):
            x = -1.0 * x
            break
        elif(s[i] ==  '+'):
            break
        x = x+(float(s[i])*(10**dec))
        dec += 1


    dec = dec + 2
    y = 0
    dec2 = 0

    for i in reversed(range(l-dec)):
        if(s[i] == '-'):
            y = -1.0 * y
            break
        y += (float(s[i])*(10**dec2))
        dec2 += 1


    # print(y)


    temp = x
    x = y
    y = temp  

    r = abs(complex(x,y))
    print(r)
    p = cmath.phase(complex(x,y))
    print(p)

main()