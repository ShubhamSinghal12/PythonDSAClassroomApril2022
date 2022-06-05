# st = "nitin"
# for i in range(len(st)):
#     print(st[:i+1],st[i+1:])

def pp(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ques)):
            part = ques[:i+1]
            if part == part[::-1]:
                pp(ques[i+1:],ans+part+" ")
pp("nitin","")