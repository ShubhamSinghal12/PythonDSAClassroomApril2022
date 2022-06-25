def power(a,b):
    if b == 0:
        return 1
    else:
        x = power(a,b//2)
        if b%2 == 0:
            return x*x
        else:
            return x*x*a

print(power(2,5))