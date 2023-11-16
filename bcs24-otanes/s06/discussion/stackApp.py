class PopStack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size
        
    def is_full(self):
        return self.top == self.max_size -1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if not self.is_full():
            if data not in self.stack:
                self.top += 1
                self.stack.append(data)
                #check if push is successful
                return True
            else:
                #element in stack already
                return False       
        else:
            return "Stack overflow"
    
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            return "Underflow"
        
    def display_elements(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            print("Elements in stack list ")
            for i in range(self.top + 1):
                print(self.stack[i])
    
stack = PopStack(5)

print(stack.push("banana1"))
print(stack.push("banana2"))
print(stack.push("banana3"))
print(stack.push("banana4"))
print(stack.push("banana5"))
print(stack.push("banana6"))
print(stack.push("banana7"))

stack.display_elements()            
            
print("Popping element one by one: ")
while not stack.is_empty():
    popped = stack.pop()
    print("Removed element ", popped)
    
stack.display_elements()
    

