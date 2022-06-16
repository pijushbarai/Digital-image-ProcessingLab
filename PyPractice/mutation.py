def mutate_string(string, position, character):
    l = list(string)
    l[int(position)] = character
    str2 = ''
    for ele in l:
        str2+=ele
    return str2
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)