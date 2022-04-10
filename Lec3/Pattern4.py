n = 5
row = 1
nst = n
nsp = 0
while row <= n:
    #Work to be done
    
    csp = 1
    while csp <= nsp:
        print(" ",end=" ")
        csp += 1
    
    cst = 1
    while cst <= nst:
        print("*",end=" ")
        cst += 1
    
    # Updation
    print()
    row += 1
    nst -= 1
    nsp += 2

print()