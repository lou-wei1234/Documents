import os
import time

num_floors = 10
target_floor = 5

# initialize the array to contain "|____|" in all indices
floors = ["|____|"] * num_floors

for floor in range(num_floors):
    # clear console
    os.system('cls')

    # update the position of the symbol
    if floor > 0:
        floors[floor - 1] = "|____|"
        
    floors[floor] = "|_🙂_|"
    
    # print floors
    for i in range(num_floors, 0, -1):
        print(floors[i - 1], i)
    
    # When destination is reached
    if floor == target_floor - 1:
        print("Destination reached!")
        break
    
    time.sleep(0.5)
