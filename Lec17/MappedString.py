def mps(ques,ans):
    if len(ques) == 0:
        print(ans)
        return 1
    else:
        c = 0
        c += mps(ques[1:],ans + chr(int(ques[0])+64))
        if len(ques) >= 2:
            i = int(ques[0:2])
            if i <= 26:
                c+= mps(ques[2:],ans + chr(i+64))
        return c

c = mps("123","")
print(c)