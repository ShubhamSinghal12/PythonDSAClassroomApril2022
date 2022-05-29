def stairs(n,ans):
    if n == 0:
        print(ans)
        return 1
    elif n < 0:
        return 0
    else:
        c = 0 
        c += stairs(n-1,ans+"1")
        c += stairs(n-2,ans+"2")
        return c

c = stairs(5,"")
print(c)

def stairsComb(n,ans,lp):
    if n == 0:
        print(ans)
        return 1
    elif n < 0:
        return 0
    else:
        c = 0 
        if lp < 2:
            c += stairsComb(n-1,ans+"1",1)
        c += stairsComb(n-2,ans+"2",2)
        return c

print(stairsComb(5,"",1))