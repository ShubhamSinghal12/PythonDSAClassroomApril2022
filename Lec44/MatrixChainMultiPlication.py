def mcm(matrix,si,ei):
    if si+1 == ei:
        return 0
    else:
        opt = 10**10
        for k in range(si+1,ei):
            cur = matrix[si]*matrix[k]*matrix[ei]
            first = mcm(matrix,si,k)
            second = mcm(matrix,k,ei)
            opt = min(opt,cur+first+second)
        return opt

matrix = [40,20,30,10,30]
print(mcm(matrix,0,len(matrix)-1))