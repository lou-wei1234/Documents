class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
       self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
               
    def display(self):
        target_value = "LINUS TORVALDS"       
        arr = []
        current_target_char = 0
        current = self.head

        """
        I tried two ways of doing this, one with for loop and the other is while loop.
        nested for loop where each iteration of the outer loop will put the current node to starting node again
        
        for i in target_value:
            current = self.head
            for _ in target_value:
                if i == " ":
                    arr.append(i)
                    break
                if str(current.data) == i: 
                    arr.append(str(current.data))
                    break
                current = current.next

        while loop where when the current node in the iteration reaches the last node, the current node will go back
        to the starting node again
        """
        
        while current_target_char < len(target_value):
            if current is None:
                current = self.head
            if target_value[current_target_char] == " ":
                arr.append(" ")
                current_target_char += 1
            if current.data == target_value[current_target_char]:
                arr.append(str(current.data))
                current_target_char += 1
            current = current.next
            
        for i in arr:
            print(i, end="")

input_values = ['I', 'S', 'L', 'T', 'O', 'R', 'N', 'S', 'U', 'D', 'L', 'A', 'V']

my_linked_list = linked_list()

for value in input_values:
    my_linked_list.insert(value)

my_linked_list.display()
