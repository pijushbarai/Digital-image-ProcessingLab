def main():

    n,m = list(map(int,input().split()))
    luck = list(map(int,input().split()))
    set1 = set(map(int,input().split()))
    set2 = set(map(int,input().split()))
    happyness = 0
    for i in range(n):
        if(luck[i] in set1):
            happyness += 1
        elif (luck[i] in set2):
            happyness -= 1
    print(happyness)
main()