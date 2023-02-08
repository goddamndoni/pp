def histogram(my_list): 
    for i in my_list:
        for j in range(i):
            print("*", end = "")
        print()
a = list(map(int,input().split()))
print(histogram(a))
# print by space