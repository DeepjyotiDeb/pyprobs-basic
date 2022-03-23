#%%
#idea is to store the last digit inside a 
def revInt(num):
    digit = 0
    while num!= 0:
        rem = num%10 # % gives the last value and hence last number comes up
        digit = digit*10 + rem
        num = num // 10 #
    return digit
def revStr(str):
    return str[::-1]

str = "ert"
num = 423
revInt(num)
revStr(str)
# num = 423 
# digit = 3
# num = 42
# digit = 42 % 10 = 2
# num = 4
# digit = 4%10 = 4