l = [4,3,1,2,25,11,12]

def NG(l):
    ans = [0 for i in range(len(l))]
    st = []
    for i in range(len(l)):
        while len(st) != 0 and l[st[-1]] < l[i]:
            j = st.pop()
            ans[j] = l[i]

        st.append(i)
    
    for i in st:
        ans[i] = -1

    return ans

print(NG(l))