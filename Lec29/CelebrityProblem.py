

l = [[0,1,1,1],[1,0,1,0],[1,0,0,0],[1,0,1,0]]

def cele(l):
    st = [i for i in range(len(l))]
    while len(st) > 1:
        a = st.pop()
        b = st.pop()

        if l[a][b] == 1:
            st.append(b)
        else:
            st.append(a)

    c = st.pop()
    flag = True

    for i in range(len(l)):
        if i != c and (l[i][c] == 0 or l[c][i] == 1):
            flag = False
            break
    if flag:
        print("Celeb: "+str(c))
    else:
        print("No Celeb")

cele(l)