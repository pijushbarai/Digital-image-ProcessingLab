
from turtle import width


def main():
    n = int(input())
    # # width = len("{0:b}")
    # for i in range(1,n+1):
    #     print("{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}".format(i, w = len("{0:b}".format(n))))
    
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

main()