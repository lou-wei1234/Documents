import time
import random


def constant_search(array, target):
    if target in array:
        return True
    else:
        return False

    
def linear_search(array, target):
    for i in array:
        if i == target:
            return True
    return False
        

def quadratic_search(array, target):
    for i in array:
        for j in array:
            if j == target:
                return True
    return False

        
array = [random.randint(-2147483648, 2147483647) for i in range(10**5)]
target = random.randint(-2147483648, 2147483647)
print (f"Random target number: {target}\n")

start_time = time.time()
if constant_search(array, target):
    print("Target found. ")
else:
    print("Target not found. ")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"It took {elapsed_time:.7f} seconds to search because of constant time complexity\n")

start_time = time.time()
if linear_search(array, target):
    print("Target found. ")
else:
    print("Target not found. ")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"It took {elapsed_time:.7f} seconds to search because of linear time complexity\n")

start_time = time.time()
if quadratic_search(array, target):
        print("Target found. ")
else:
    print("Target not found. ")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"It took {elapsed_time:.7f} seconds to search because of quadratic time complexity\n")
