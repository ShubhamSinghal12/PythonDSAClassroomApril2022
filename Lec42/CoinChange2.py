def ccc(l,amount,lp):
    if amount == 0:
        return 1
    else:
        c = 0
        for i in range(lp,len(l)):
            if amount >= l[i]:
                c +=  ccc(l,amount-l[i],i)

        return c

def cccTD(l,amount,lp,dp):
    if amount == 0:
        return 1
    else:
        if dp[lp][amount] != 0:
            return dp[lp][amount]
        c = 0
        for i in range(lp,len(l)):
            if amount >= l[i]:
                c +=  cccTD(l,amount-l[i],i,dp)
                

        dp[lp][amount] = c
        return c

def cccBU(l,amt):
    dp = [[0 for j in range(amt+1)] for i in range(len(coins))]
    for i in range(len(l)):
        dp[i][0] = 1
    
    for j in range(1,amt+1):
        for i in range(len(l)):
            c = 0
            for k in range(i,len(l)):
                if j >= l[k]:
                    c +=  dp[k][j-l[k]]
            dp[i][j] = c

    return dp[0][amt]

coins = [1,2,5]
amt = 5
dp = [[0 for j in range(amt+1)] for i in range(len(coins))]
# print(cccTD(coins,amt,0,dp))
print(cccBU(coins,amt))
