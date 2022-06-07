import math


n = int(input())
str = []
for i in range(n):
    str.append(input())
key = input()


for i in range(n):
    for j in range(len(key)):
        if(str[i][j] == key[j] and j == len(key)-1):
            s, *num = str[i].split()
            result = 0
            for k in range(len(num)):
                result += float(num[k])
            result = float(result)/len(num)
            #f = round(result,2)
            print('%.2f' %result)
            i = n
            break
        if(str[i][j] == key[j]):
            continue
        else:
            break
