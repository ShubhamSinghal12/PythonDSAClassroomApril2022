from tkinter import N


n = 10
l = [0]*n 
print(l,len(l))

# l = [int(input()) for i in range(5)]
# print(l,len(l))

# a = input().split()
# print(a,type(a))
l = []

# for i in input().split():
#     l.append(int(i))

l = [int(i) for i in input().split()]

print(l)