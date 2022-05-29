def lexo(n,ans):
    if ans > n:
        return
    else:
        if ans != 0:
            print(ans)
        s = 0
        if ans == 0:
            s = 1
        for i in range(s,10):
            lexo(n,ans*10+i)

lexo(100,0)

def lexo(n,ans,l):
    if ans > n:
        return
    else:
        # if ans != 0:
        l.append(ans)
        # s = 0
        # if ans == 0:
        #     s = 1
        for i in range(10):
            lexo(n,ans*10+i,l)
n = 1000
l = []
for i in range(1,10):
    lexo(n,i,l)
# return l