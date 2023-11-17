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

