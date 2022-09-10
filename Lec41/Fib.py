def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibTD(n,dp):
    if n == 0 or n == 1:
        return n
    else:
        if dp[n] != 0:
            return dp[n] #Retrieval

        t = fibTD(n-1,dp) + fibTD(n-2,dp)
        dp[n] = t # Storing
        return t

def fibBU(n):
    l = [0 for i in range(n+1)]

    l[0] = 0
    l[1] = 1
    for i in range(2,n+1):
        l[i] =  l[i-1] + l[i-2]
    
    return l[n]

def fibBUSE(n):
    a,b = 0,1

    for i in range(2,n+1):
        c = a+b

        a = b
        b = c
    
    return b

n = 300
l = [0 for i in range(n+1)]
print(fibBUSE(n))