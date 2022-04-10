
n = 5
nst = 1
nsp = n-1
row = 1
val = 1
while row<=n:
    #Work
    csp = 1
    while csp <= nsp:
        print(" ",end="\t")
        csp += 1
    cst = 1
    cval = val
    while cst <= nst:
        if cst == 1 or cst == nst:
            print(cval,end="\t")
        else:
            print(0,end="\t")
        if cst <= nst//2:
            cval += 1
        else:
            cval -= 1
        cst+=1
    #Update

    print()
    row+=1
    nst += 2
    nsp -= 1
    val += 1