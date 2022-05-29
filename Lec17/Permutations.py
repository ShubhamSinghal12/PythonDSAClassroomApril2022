def pm(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ques)):
            nq = ques[:i]+ques[i+1:]
            pm(nq,ans+ques[i])

def pm2(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ans)+1):
            na = ans[:i]+ques[0]+ans[i:]
            pm2(ques[1:],na)


def tpm(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ques)):
            # flag = True
            # for j in range(0,i):
            #     if ques[i] == ques[j]:
            #         flag = False
            #         break
            if ques[i] not in ques[0:i]:
                nq = ques[:i]+ques[i+1:]
                tpm(nq,ans+ques[i])

tpm("aba","")
