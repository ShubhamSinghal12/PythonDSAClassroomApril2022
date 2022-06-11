def cc(l,amount,ans):
    if amount == 0:
        print(ans)
    elif amount < 0:
        return 
    else:
        for i in l:
            cc(l,amount-i,ans+str(i))

def ccc(l,amount,ans,lp):
    if amount == 0:
        print(ans)
    elif amount < 0:
        return 
    else:
        for i in range(lp,len(l)):
            
            ccc(l,amount-l[i],ans+str(l[i]),i)

def ccc2(l,amount,ans):
    if amount == 0:
        print(ans)
    elif amount < 0:
        return 
    else:
        for i in range(len(l)):
            ccc2(l[i+1:],amount-l[i],ans+str(l[i]))



def ccs(l,amount,ans,bigans):
    if amount == 0:
        bigans.append(list(ans))
        # print(ans)
    elif amount < 0:
        return 
    else:
        for i in l:
            ans.append(i)
            ccs(l,amount-i,ans,bigans)
            ans.pop()


def ccr(l,amount,ans,bigans,i):
    if amount == 0:
        bigans.append(list(ans))
    elif i >= len(l) or amount < 0:
        return
    else:
        ans.append(l[i])
        ccr(l,amount-l[i],ans,bigans,i)
        ans.pop()
        ccr(l,amount,ans,bigans,i+1)
        # ans.pop()


l = [1,2,3,5,7]
amt = 6
ans = []
bigans = []
# ccc2(l,amt,"")
ccr(l,amt,ans,bigans,0)
print(bigans)