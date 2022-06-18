if __name__ == '__main__':
    s = input()
    
    alphabet = 0
    digit = 0
    lowerCase = 0
    upperCase = 0
    len = len(s)
    for x in range(len):
        if(s[x].isdigit()):
            digit +=1
        if(s[x].islower()):
            lowerCase += 1
        if(s[x].isupper()):
            upperCase +=1
        if(s[x].isalpha()):
            alphabet +=1
            # print(s[x])
    # print(s.isalnum())
    if((alphabet > 0 and digit > 0) or s.isalnum()):
        print('True')
    else:
        print('False')
    if(alphabet > 0):
        print('True')
    else:
        print('False')
    if(digit > 0):
        print('True')
    else:
        print('False')
    if(lowerCase > 0):
        print('True')
    else:
        print('False')
    if(upperCase > 0):
        print('True')
    else:
        print('False')
        