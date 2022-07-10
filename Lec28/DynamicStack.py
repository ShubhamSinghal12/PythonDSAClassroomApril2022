from MyStack import MyStack

class DynamicStack(MyStack):

    def push(self,ele):
        if self.isFull():
            nl = [0]*len(self.l)
            self.l.extend(nl)
        
        super().push(ele)

# st = DynamicStack(5)
# for i in range(1,30):
#     st.push(i)
#     st.display()

# print(st.pop())
# print(st.pop())
# print(st.peek())
# st.display()
# st.push(10)
# st.push(20)
# st.display()
