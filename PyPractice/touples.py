# from ast import Tuple


# n = int(input())
# integer_list = map(int, input().split())
# list = list(integer_list)
# print(hash(Tuple(list)))


n = int(input())
list = []
integer_list = map(int, input().split())
for i in integer_list:
    list.append(i)
t = tuple(list)
print(hash(t))