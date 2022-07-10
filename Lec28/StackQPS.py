from DynamicStack import DynamicStack

def dispR(st):
    nst  = DynamicStack()
    while not st.isEmpty():
        nst.push(st.pop())
    
    nst.display()
    
    while not nst.isEmpty():
        st.push(nst.pop())

def dispRR(st:"DynamicStack"):
    if st.isEmpty():
        return 
    else:
        n = st.pop()
        dispRR(st)
        print(n,end= " ")
        st.push(n)

def ar(st:"DynamicStack"):
    nst = DynamicStack()
    while not st.isEmpty():
        nst.push(st.pop())
    
    arHelp(nst,st)
    

def arHelp(nst,st):
    if nst.isEmpty():
        return
    else:
        n = nst.pop()
        arHelp(nst,st)
        st.push(n)

def ar2(st:"DynamicStack"):
    if st.isEmpty():
        return
    else:
        n = st.pop()
        ar2(st)
        pushFirst(st,n)

def pushFirst(st,ele):
    if st.isEmpty():
        st.push(ele)
    else:
        n = st.pop()
        pushFirst(st,ele)
        st.push(n)

st = DynamicStack()
for i in range(1,6):
    st.push(i)

st.display()
ar2(st)
st.display()
