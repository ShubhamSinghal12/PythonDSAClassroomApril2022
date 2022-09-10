def MinCost(cost,i):
    if i < 0:
        return 0
    else:
        return min(MinCost(cost,i-1),MinCost(cost,i-2))+cost[i]

def MinCostTD(cost,i,dp):
    if i < 0:
        return 0
    else:
        if dp[i] != -1:
            return dp[i]
        else:
            dp[i] = min(MinCostTD(cost,i-1,dp),MinCostTD(cost,i-2,dp))+cost[i]
            return dp[i]

def MinCostBU(cost):
    dp = [0 for i in range(len(cost))]
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(len(cost)):
        dp[i] = min(dp[i-1],dp[i-2])+cost[i]
    
    return min(dp[-1],dp[-2])



cost = [1,100,1,1,1,100,1,1,100,1]
dp = [-1 for i in range(len(cost))]
# print(min(MinCostTD(cost,len(cost)-1,dp),MinCostTD(cost,len(cost)-2,dp)))
print(MinCostBU(cost))
