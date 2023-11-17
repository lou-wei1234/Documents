class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            self.top.next = None
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack empty")
        else:
            if self.top.next is None:
                popped_data = self.top.data
                self.top = None
                return popped_data
            else:
                temp = self.top
                popped_data = temp.data
                self.top = temp.next
                temp = None
                return popped_data

    def display(self):
        if self.is_empty():
            print("Stack Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

class Palindrome:
    def __init__(self, input):
        self.input = input

    def check(self): #create an instance of Stack and push each character of the input to the object
        stack = Stack()
        for i in self.input:
            stack.push(i)

        temp = stack.top 
        while temp: #show every value of all nodes and the popped values to prepare for comparison
            self.compare(temp.data, stack.pop())
            temp = temp.next
        
    def compare(self, first, second):
        print(first, second)    #i am trying to attempt to compare the data in first node, thinking it was the at the stack.top
                                #but the stack.top actually contains the last node created and not the first node that was created (LIFO)
                                #so when i print the stack.top and stack.pop, they are just the same
palindrome = Palindrome("banana")
palindrome.check()

"""
DESIRED OUTPUT
a b
n a
a n
n a
a n
b a

CURRENT OUTPUT
a a
n n
a a
n n
a a
b b
"""
