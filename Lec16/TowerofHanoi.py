def toh(n,fr,to,using):
    if n == 0:
        return 0
    else:
        c = 1
        c += toh(n-1,fr,using,to)
        print("Move",n,"from",fr,"to",to)
        c += toh(n-1,using,to,fr)
        return c

c = toh(4,"A","C","B") 
print(c)