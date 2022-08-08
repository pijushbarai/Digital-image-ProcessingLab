def main():
    n = int(input())
    s = set()
    l = []
    for i in range(n):
        x = input()
        s.add(x)
        l.append(x)
    setLen = len(s)
    print(setLen)
    for i in s:
        print(l.count(i),end=' ')
main()