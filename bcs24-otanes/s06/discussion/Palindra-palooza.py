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

    def reverse(self): #create a reversed version of the original stack. this version will be called in the method check in class Palindrome
        reversed_stack = Stack()
        temp = self.top
        while temp:
            reversed_stack.push(temp.data)
            temp = temp.next
        return reversed_stack

class Palindrome:
    def __init__(self, input):
        self.input = input

    def check(self): #create an instance and push each character of the input
        stack = Stack()
        for i in self.input:
            stack.push(i)

        reversed_stack = stack.reverse()

        temp = stack.top
        while temp:
            self.compare(temp.data, reversed_stack.pop())
            temp = temp.next
        
    def compare(self, first, second):
        print(first, second)    #it now works as intended. temp.data contains the data of the latest node in the original stack
                                #reversed_stack.pop() now contains the data of the latest node in the reversed stack
                                #all i need is to put a conditional statement that checks the equality of the two nodes
palindrome = Palindrome("banana")
palindrome.check()

"""
CURRENT OUTPUT
a b
n a
a n
n a
a n
b a

DESIRED OUTPUT
a b
n a
a n
n a
a n
b a
"""
