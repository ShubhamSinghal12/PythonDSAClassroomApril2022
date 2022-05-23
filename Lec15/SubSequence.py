def ss(st):
    if len(st) == 0:
        return [""]
    else:
        rr = ss(st[1:])
        ans = []
        for i in rr:
            ans.append(i)
            ans.append(st[0]+i)
        return ans

def ss2(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        
        ss2(ques[1:],ans+ques[0])
        ss2(ques[1:],ans)

def Asciiss2(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        Asciiss2(ques[1:],ans)
        Asciiss2(ques[1:],ans+ques[0])
        Asciiss2(ques[1:],ans+str(ord(ques[0])))

# ss2("abc","")
Asciiss2("ab","")

# print(ss("abc"))
