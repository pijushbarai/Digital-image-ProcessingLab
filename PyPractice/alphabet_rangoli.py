def print_rangoli(size):
    arr = []
    n = size
    for i in range(n):
        x = i*2
        length = ((n*2)-1) + ((n*2)-2)
        ch = ord('a') + n
        str = ''
        for j in range(length):
            if(j<x):
                str = str+'-'
            elif(j >= (length-x)):
                str = str + '-'
            elif(j%2 == 1):
                str = str + '-'
            else:
                if(j%2 == 0):
                    if(j <= length//2):
                        str = str + chr(ch-1)
                        ch = ch - 1
                    else:
                        str = str + chr(ch+1)
                        ch = ch + 1
        arr.append(str)
    for i in range(n):
        print(arr[n-1-i])
    for i in range(n-1):
        print(arr[i+1])
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)