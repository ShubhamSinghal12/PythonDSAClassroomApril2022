def evalPoly(p,x):
    ans = 0
    t = 1
    for i in range(len(p)):
        ans += p[i]*t

        t = t * x
    return ans

poly = [1,10,2,0,3]
x=2
print(evalPoly(poly,x))

