def main():
    arr = []
    n = int(input())
    for i in range(n):
        str = input()
        x = str.split()
        if(x[0] == 'insert'):
            arr.insert(int(x[1]),int(x[2]))
        elif(x[0] == 'print'):
            print(arr)
        elif(x[0] == 'remove'):
            arr.remove(int(x[1]))
        elif(x[0] == 'sort'):
            arr.sort()
        elif(x[0]== 'pop'):
            l = len(arr)
            arr.pop(l-1)
        elif(x[0] == 'reverse'):
            arr.reverse()
        elif(x[0] == 'append'):
            arr.append(int(x[1]))

main()