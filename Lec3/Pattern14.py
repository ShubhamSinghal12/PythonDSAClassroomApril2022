n = 5
nst = 1
row = 1
nsp = n-1

while row <= 2*n-1:
    #work
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp+=1

    cst = 1
    while cst <= nst:
        print("*",end=" ")
        cst+=1
    
    #Update

    if row < n:
        nst += 1
        nsp-=1
    else:
        nst -= 1
        nsp+=1

    row += 1
    print()
    

