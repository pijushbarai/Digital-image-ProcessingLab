def main():
    n = int(input())
    name = {}
    for i in range(n):
        x = input()
        if x in name:
            name[x] += 1
        else :
            name[x] = 1
    print(len(name))
    # print(name.values(),end=' ')
    for value in name.values():
        print(value,end=' ')
    
   
main()