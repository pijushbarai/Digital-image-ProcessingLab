def solve(s):
    list = []
    list = s.split(' ')
    string = ''
    for i in range(len(list)):
        x = str(list[i])
        x = x.capitalize()
        # print(x)
        string = string + x + ' '
    return string
        


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)