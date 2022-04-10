


n = 5
nst = 1
nsp = n-1
row = 1

while row<=n:
    #Work
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1
    cst = 1
    while cst <= nst:
        print("*",end=" ")
        cst+=1
    #Update

    print()
    row+=1
    nst += 2
    nsp -= 1