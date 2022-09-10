def MinCost(cost,i):
    if i >= len(cost):
        return 0
    else:
        return min(MinCost(cost,i+1),MinCost(cost,i+2))+cost[i]

def MinCostTD(cost,i,dp):
    if i >= len(cost):
        return 0
    else:
        if dp[i] != -1:
            return dp[i]
        else:
            dp[i] = min(MinCostTD(cost,i+1,dp),MinCostTD(cost,i+2,dp))+cost[i]
            return dp[i]

def minCostBU(cost):
    dp = [0 for i in range(len(cost))]
    dp[-1] = cost[-1]
    dp[-2] = cost[-2]

    for i in range(len(cost)-3,-1,-1):
        dp[i] = min(dp[i+1],dp[i+2])+cost[i]
    
    return min(dp[0],dp[1])



cost = [10,15,20]
dp = [-1 for i in range(len(cost))]
# print(min(MinCostTD(cost,0,dp),MinCostTD(cost,1,dp)))
print(minCostBU(cost))
