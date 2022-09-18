from cmath import sqrt
import numpy as np

def main():
    a = int(input())
    b = int (input())
    c = sqrt((a*a)+(b*b))
    print(c)
    cm = c/2
    
    x = ((c*c)+(b*b)-(a*a))
    
    print(x)
    angC = np.arccos(x)
    print(angC)



main()