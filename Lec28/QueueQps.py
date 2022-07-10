from DynamicQueue import DynamicQueue

def ar(qt:"DynamicQueue"):
    if qt.isEmpty():
        return
    else:
        n = qt.dequeue()
        ar(qt)
        qt.enqueue(n)

st = DynamicQueue()
for i in range(1,6):
    st.enqueue(i)

st.display()
ar(st)
st.display()
