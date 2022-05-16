def fmn(seq):
    l = [0]*(len(seq)+1)
    val = 1
    for i in range(len(seq)+1):
        if i == len(seq) or seq[i] == "I":
            l[i] = val
            val += 1
            # j = i-1
            for j in range(i-1,-1,-1):
                if seq[j] == "D":
                    l[j] = val
                    val += 1
                else:
                    break
            # while j>= 0 and seq[j] == "D":
            #     l[j] = val
            #     val += 1
            #     j -= 1
    s = ""
    for i in l:
        s += str(i)
    
    return s

n = int(input())
l = input().split()
for i in l:
    print(fmn(i))