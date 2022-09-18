def knap(values,weight,i,W):
    if i == len(values) or W == 0:
        return 0
    else:
        inc = 0
        if weight[i] <= W:
            inc = values[i]+knap(values,weight,i+1,W-weight[i])
        exc = knap(values,weight,i+1,W)

        return max(inc,exc)

def knapBU(values,weight,W):
    dp = [[0 for j in range(W+1)] for i in range(len(values)+1)]
    for i in range(len(values)-1,-1,-1):
        for j in range(1,W+1):
            inc = 0
            if weight[i] <= j:
                inc = values[i]+dp[i+1][j-weight[i]]
            exc = dp[i+1][j]

            dp[i][j] = max(inc,exc)

    return dp[0][W]

values = [60,100,120]
weights = [10,20,30]
print(knapBU(values,weights,50))
