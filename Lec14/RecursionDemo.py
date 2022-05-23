def PD(n):
    if n == 0:
        return
    else:   
        print(n)
        PD(n-1)

def PI(n):
    if n == 1:
        print(1)
    else:
        PI(n-1)
        print(n)

def PDI(n):
    if n == 0:
        # print(1)
        pass
        # return 
    else:
        print(n)
        PDI(n-1)
        print(n)

def sumN(n):
    if n == 1:
        return 1
    else:
        s = sumN(n-1)
        return s+n

def sumTail(n,ans):
    if n == 0:
        return ans
    else:
        return sumTail(n-1,ans+n)

def power(a,b):
    if b == 0:
        return 1
    else:
        return power(a,b-1)*a

def powTail(a,b,ans):
    if b == 0:
        return ans
    else:
        return powTail(a,b-1,ans*a)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def fibtail(n,a,b):
    if n == 0:
        return a
    else:
        return fibtail(n-1,b,a+b)
# print(power(2,10))
# print(sumTail(5,0))
# print(powTail(2,10,1))
print(fibtail(6,0,1))
