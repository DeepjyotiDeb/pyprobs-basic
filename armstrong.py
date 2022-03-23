def arm(n):
    digit = 0
    while n != 0:
        rem = n%10
        digit = digit+rem**3
        n = n//10
    return digit
def armCheck(n):
    digit = arm(n)
    if digit == n:
        print("arm")
    else:
        print("not arm")

n = 123
armCheck(n)