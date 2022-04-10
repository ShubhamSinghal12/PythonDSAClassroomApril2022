import math
num = 123456
temp = num
count = 0
while num != 0:
    num = num//10
    count += 1

print(count)

digits = int(math.log10(temp)) +1
print(digits)


