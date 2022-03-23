#%%
def prime(num):
    flag = False
    if num == 1: flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag == True:
        return True
    else:
        return False

def primeM(m):
    for i in range(1,m):
        if prime(i) == True:
            print(i,"not prime")
        else:
            print(i,"prime")

m = 17
prime(m)
primeM(m)
