from re import sub
import textwrap

def wrap(string, max_width):
    list = []
    str = ''
    length = len(string)
    for i in range(0,length,max_width):
        if(i+max_width > length-1):
            subString = string[i:length]
        else:
            subString = string[i:i+max_width]
        subString  = subString + '\n'
        str += subString
    return str
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)