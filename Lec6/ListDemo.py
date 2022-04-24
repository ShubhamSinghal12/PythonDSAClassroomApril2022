l = []
l = [1,2,3]
l = [1,"Hello",3.0,4]

l[0] = 100
# print(l,type(l))
# print(l[0])

# print(len(l))

# i = -1
# while i >= -len(l):
#     print(l[i])
#     i -= 1

# for i in l:
#     print(i)

# for i in range(-len(l),0):
#     print(l[i])

l = [1,2,3,4]
# for i in range(5):
#     l.append(int(input()))

l.insert(1,20)
print(l)

# a = l.pop(1)
# print(l,a)

# l.remove(20)
# print(l)

# l.clear()
# print(l)

l = [1,2,3,4,5]

a = l[::-1]
print(a,type(a))







a = [1,2,3]
b = [4,5,6]

c = a+b
a.extend(b)
print(a)
