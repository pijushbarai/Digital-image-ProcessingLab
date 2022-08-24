from itertools import product
def main():
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = list(product(a,b))
    for i in range(len(ans)):
        print(ans[i],end=' ')
    print()

main()