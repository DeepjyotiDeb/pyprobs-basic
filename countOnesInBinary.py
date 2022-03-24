#%%
# def num_two(n):
# count = 0
digits = []
    # digits.append(num_ones(n))
    # print(digits)
def num_ones(n):
    if n>=1:
        num_ones(n//2)
        print(n)
        digits.append(n%2)
    print(digits)
    count = 0
    for i in digits:
        if i == 1:
            count += 1
    return count
    
n= 60000
# num_ones(n)
num_ones(n)