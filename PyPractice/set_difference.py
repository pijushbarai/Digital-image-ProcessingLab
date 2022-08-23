def main():
    x = int(input())
    a = set(map(int,input().split()))
    y = int(input())
    b = set(map(int,input().split()))
    ans = a.difference(b)
    print(len(ans))
main()