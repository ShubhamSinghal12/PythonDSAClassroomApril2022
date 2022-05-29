def gp(op,cl,ans):
    if op == 0 and cl == 0:
        print(ans)
    elif op < 0 or cl < op:
        return
    else:
        gp(op-1,cl,ans +"(")
        gp(op,cl-1,ans+")")

gp(3,3,"")
