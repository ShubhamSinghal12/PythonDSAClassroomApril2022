def CountPalindromicSS(st):
    
    ans = 0
    for i in range(len(st)):
        ans += 1
        li = i-1
        ri = i+1
        while li >= 0 and ri < len(st) and st[li] == st[ri]:
            ans += 1
            li -= 1
            ri += 1
    
    for i in range(len(st)-1):
        li = i
        ri = i+1
        while li >= 0 and ri < len(st) and st[li] == st[ri]:
            ans += 1
            li -= 1
            ri += 1
    print(ans)

CountPalindromicSS("aaaaa")