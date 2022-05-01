# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9]

# ll = [l1,l2,l3]

# print(ll)

# for i in ll:
#     for j in i:
#         print(j,end=" ")
#     print()

ll = []
m = 3
n = 3

# for i in range(m):
#     l = []
#     for j in range(n):
#         l.append(int(input()))
#     ll.append(l)

# ll = [[int(input()) for j in range(n)] for i in range(m)]

# ll = []
# for i in range(m):
#     l = []
#     for j in input().split():
#         l.append(int(j))
#     ll.append(l)

# ll = [[int(j) for j in input().split()] for i in range(m)]

ll = [[0]*n]*m

ll[1][0] = 1

for i in range(len(ll)):
    for j in range(len(ll[i])):
        print(ll[i][j],end = " ")
    print()


# l = input().split()
# print(l)

