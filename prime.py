#%%
def prime(num):
    flag = False
    if num == 1: flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print("not prime")
    else:
        print("prime")

def primeM(m):
    for i in range(1,m):
        print(i, prime(i))


m = 20
# prime(n)
primeM(m)