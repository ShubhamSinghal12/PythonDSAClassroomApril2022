n = 3
lans = []
def CoinToss(n,ans,lans):
    if n == 0:
        lans.append(ans)
        return 1
    else:
        c = 0
        c += CoinToss(n-1,ans+"H",lans)
        c += CoinToss(n-1,ans+"T",lans)
        return c

c = CoinToss(n,"",lans)
print(lans,len(lans),c)