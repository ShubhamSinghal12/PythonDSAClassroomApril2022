import math

def countDigits(n):
    return int(math.log10(n))+1

# print(countDigits(153))

def isArmstrong(n):
    d = countDigits(n)
    temp = n

    ans = 0
    while n != 0:
        ans += (n%10)**d
        n //= 10
    
    return ans == temp

# print(isArmstrong(13))

def printAllArmStrong(n):
    i = 1
    while i <= n:
        if isArmstrong(i):
            print(i)
        i += 1

n = 1000
printAllArmStrong(n)
