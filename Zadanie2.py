class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            nowywez = Node(data)
            nowywez.next = self.head
            self.head = nowywez

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        internode = self.head
        if self.isempty():
            print("Stos pusty")
        else:
            while(internode != None):
                print(internode.data,"->",end = " ")
                internode = internode.next
            return

MyStack = Stack()

MyStack.push(1)
MyStack.push(2)
MyStack.push(3)
MyStack.push(4)
MyStack.push(5)
MyStack.push(6)
MyStack.push(7)
MyStack.push(8)

MyStack.display()

print("\nElement znajdujący się na górze ",MyStack.peek())

MyStack.pop()
MyStack.pop()

MyStack.display()

print("\nElement znajdujący się na górze ", MyStack.peek())

MyStack.pop()

MyStack.display()

print("\nElement znajdujący się na górze ", MyStack.peek())