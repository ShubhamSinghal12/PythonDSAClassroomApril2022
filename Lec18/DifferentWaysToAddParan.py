def isop(i):
    return i == "+" or i == "-" or i == "*"


def opt(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    else:
        return a*b

def diff(st):
    if '+' not in st and '-' not in st and '*' not in st:
        return [int(st)]
    else:
        ans = []
        for i in range(len(st)):
            if st[i] in "+*-":
                l = diff(st[:i])
                r = diff(st[i+1:])
                for j in l:
                    for k in r:
                        ans.append(opt(j,k,st[i]))
        return ans

l = diff("2*3-4*5")
print(l)

