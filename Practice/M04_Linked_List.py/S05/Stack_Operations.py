class stack:
    def __init__(self):
        self.s = []
    def push(self,val):
        self.s.append(val)
    def is_empty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.s.pop()
    def size(self):
        return len(self.s)
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.s[-1]
st = stack()
print(st.is_empty())
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.size())
print(st.peek())

#Stack implementation using Linked List
class Node:
    def __init__(self,data):
        self.next = None
class Stack_LL:
