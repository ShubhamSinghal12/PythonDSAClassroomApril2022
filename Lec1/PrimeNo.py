num = 11
flag = 0
i = 2
while i < num/2:
    # print("Hi")
    if num%i == 0:
        flag = 1
        print("Not Prime")
        break
    i += 1
else:
    print("Prime No")
