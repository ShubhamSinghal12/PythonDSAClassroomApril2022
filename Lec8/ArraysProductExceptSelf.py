l = [1,2,3,4,5]

lp = [0]*len(l)

lp[0] = 1
for i in range(1,len(l)):
    lp[i] = lp[i-1] * l[i-1]

print(lp)

rp = [0]*len(l)
p = 1
for i in range(len(l)-1,-1,-1):
    lp[i] = lp[i]*p
    p = p*l[i]

ans = [0]*len(l)
for i in range(len(l)):
    ans[i] = lp[i]*rp[i]

print(lp)