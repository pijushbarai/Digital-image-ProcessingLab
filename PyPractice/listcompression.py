if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                # print(i,j,k)
                arr = []
                if(i+j+k != n):
                    # print(i,j,k)
                    arr.append(i)
                    arr.append(j)
                    arr.append(k)
                    # print(arr)
                    list.append(arr)
    print(list)