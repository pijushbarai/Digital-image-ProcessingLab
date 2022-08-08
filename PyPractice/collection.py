def main():
    n = int(input())
    arr= []
    customer = []
    arr = list(map(int, input().split()))
    # print(len(arr),'asdfasdfasf')
    number_of_shoe = int(input())
    for j in range(number_of_shoe):
        shoe_info = list(map(int,input().split()))
        customer.append(shoe_info)
    # for i in range(number_of_shoe):
    #     for j in range(i+1,number_of_shoe):
    #         if(customer[i][1] <= customer[j][1]):
    #             temp = customer[i]
    #             customer[i] = customer[j]
    #             customer[j] = temp
    ans = 0 
    for i in range(number_of_shoe):
        for j in range(n):
            if(arr[j] == customer[i][0]):
                ans = ans + customer[i][1]
                arr[j] = 0
                break
    print(ans)

    # print(customer)
main()