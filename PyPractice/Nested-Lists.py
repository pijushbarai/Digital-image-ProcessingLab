
from cgitb import reset


def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li


stu = []
record = []
n = int(input())
for i in range(n):
    stu.append(input())
    stu.append(float(input()))
    record.append(stu)
    stu = []
Sort(record)
chk = 0
result = []
for i in range(0,n):
    if(chk == 1):
        break
    if(record[i][1] != record[i+1][1]):
        for j in range(i+1,n):
            result.append(record[j][0])
            if(j == n-1):
                chk = 1
                break
            if(record[j][1]!=record[j+1][1]):
                chk = 1
                break
result.sort()
l = result.__len__()
for i in range(l):
    print(result[i])
