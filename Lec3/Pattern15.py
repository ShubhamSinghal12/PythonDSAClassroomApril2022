n = 5
nst = n
row = 1
nsp = 0

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
        nst -= 1
        nsp += 2
    else:
        nst += 1
        nsp -= 2

    row += 1
    print()
    

