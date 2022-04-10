import math
num = 123456

digits = int(math.log10(num)) +1
print(digits)
ans = 0

# while num != 0:
#     rem = num%10
#     ans += rem*(10**(digits-1))

#     num = num//10
#     digits -= 1

while num != 0:
    rem = num%10
    ans = ans+rem*10

    num = num//10

print(ans)
