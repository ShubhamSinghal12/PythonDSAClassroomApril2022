nums = [0,3,7,2,5,8,4,6,0,1]
s = set(nums)
mct = 0
for i in s:
    if i-1 not in s:
        ct = 1
        c = i+1
        while c in s:
            ct += 1
            c += 1
        if ct > mct:
            mct = ct
print(mct)