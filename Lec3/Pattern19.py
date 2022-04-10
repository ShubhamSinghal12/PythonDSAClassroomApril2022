n = 7
nsp = -1
nst = n//2 + 1
row = 1

while row <= n:
    cst = 1
    while cst <= nst:
        print("*",end=" ")
        cst+=1
    
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp+=1
   
    cst = 1
    if row == 1 or row == n:
        cst = 2
    while cst <= nst:
        print("*",end=" ")
        cst+=1
    
    if row <= n//2:
        nst -= 1
        nsp += 2
    else:
        nst += 1
        nsp -= 2
    
    print()
    row += 1