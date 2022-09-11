def merge_the_tools(string, k):
    l = len(string)
    list = []
    for i in range(0,l,k):
        str = string[i:i+k]
        list.append(str)
    for i in range(len(list)):
        s = set()
        for j in range(len(list[i])):
            if list[i][j] in s:
                continue
            else:
                print(list[i][j],end='')
                s.add(list[i][j])
        print()
        s.clear()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)