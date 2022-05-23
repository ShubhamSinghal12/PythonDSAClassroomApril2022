kmap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def keyPad(st):
    if len(st) == 0:
        return [""]
    else:
        ch = st[0]
        seq = kmap[int(ch)]
        rr = keyPad(st[1:])
        ans = []
        for i in rr:
            for j in seq:
                ans.append(j+i)
        return ans

def kp(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        seq = kmap[int(ques[0])]
        for i in seq:
            kp(ques[1:],ans+i)
    
# print(keyPad("23"))
kp("23","")