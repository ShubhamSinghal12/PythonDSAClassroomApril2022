def rwt(bars):

    lmax = []
    l = 0
    for i in range(len(bars)):
        if bars[i] > l:
            l = bars[i]
        lmax.append(l)
    r = 0
    rmax = [0 for i in bars]
    for i in range(len(bars)-1,-1,-1):
        if bars[i] > r:
            r = bars[i]
        rmax[i] = r
    
    ans = 0
    for i in range(len(bars)):
        ans += min(lmax[i],rmax[i]) - bars[i]
    
    return ans


bars = [0,  1,  0,  2,  1,  0,  1,  3,  2,  1,  2,  1]
print(rwt(bars))