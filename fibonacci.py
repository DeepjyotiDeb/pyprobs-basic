# 0,1,1,2,3,5,8....
first, second = 0 , 1
n = int(input("enter limit"))

for i in range(0, n):
    if i<=1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result, end=" ")    