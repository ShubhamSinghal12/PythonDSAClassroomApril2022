l1 = [1,2,2,3,4,6,5,4,2,6,7,2,3,8,3,5,7]
l2 = [2,1,3,4,5,2,3,4,1,2,3,7,8,9,5,2]

cf = {}
for ch in l1:
   cf[ch] =  cf.get(ch,0) + 1
ans = []
for i in l2:
    if i in cf and cf[i] > 0:
        ans.append(i)
        cf[i] = cf[i]-1 
print(ans)