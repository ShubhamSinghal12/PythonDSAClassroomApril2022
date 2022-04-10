import math
a = 24
b = 16

min = min(a,b)
max = max(a,b)
hcf = 0
i = 1
while i <= min:
    if min%i == 0 and max%i == 0:
        hcf = i
    i += 1

print(hcf)
print(math.gcd(a,b))

while max%min != 0:
    rem = max%min

    max = min
    min = rem

print(min)
