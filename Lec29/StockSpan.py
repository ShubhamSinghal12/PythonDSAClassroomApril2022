l = [100,80,60,70,60,75,85,110]

def SS(l):
    ans = [0 for i in range(len(l))]
    st = []
    for i in range(len(l)):
        while len(st) != 0 and l[st[-1]] < l[i]:
            st.pop()

        if len(st) == 0:
            j = -1
        else:
            j = st[-1]
        
        ans[i] = i-j

        st.append(i)

    return ans

print(SS(l))