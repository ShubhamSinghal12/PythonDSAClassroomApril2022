def mazeP(cr,cc,m,n,ans):
    if cr == m and cc == n:
        print(ans)
        return 1
    elif cr > m or cc > n:
        return 0
    else:
        c = 0
        c += mazeP(cr+1,cc,m,n,ans+"V")
        c += mazeP(cr,cc+1,m,n,ans+"H")
        c += mazeP(cr+1,cc+1,m,n,ans+"D")
        return c

c = mazeP(0,0,2,2,"")
print(c)
