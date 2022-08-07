def main():
    n = int(input())
    arr= []
    arr = list(map(int, input().split()))
    # print(len(arr),'asdfasdfasf')
    number_of_shoe = int(input())
    ans = 0
    for j in range(number_of_shoe):
        shoe_info = list(map(int,input().split()))
        temp = []
        ind = []
        for i in range(arr.index(arr[-1])+1):
            if arr[i] == shoe_info[0]:
                arr[i] = 0
                temp.append(shoe_info[1])
                ans = ans + shoe_info[1]
                break
               
    print(ans)
main()