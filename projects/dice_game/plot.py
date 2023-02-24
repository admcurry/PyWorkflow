#Import
import numpy as np
import matplotlib.pyplot as plt

#Runs the simulation
all_walks = []
for i in range(500) : #runs 500 times
    random_walk = [0]
    for x in range(100) : #100 dice rolls
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2: #if the dice roll is less than 2
            step = max(0, step - 1) #you will move down 1 stair (to a maximum of stair 0)
        elif dice <= 5: #if the roll is 2, 3, or 4
            step = step + 1 #you will move up a stair
        else:
            step = step + np.random.randint(1,7) #if the roll is six you'll randomly move 1 to 6 
        if np.random.rand() <= 0.001 : #there is a 0.1% chance you will fall to the bottom
            step = 0
        random_walk.append(step) #adds the steps to a list
    all_walks.append(random_walk) #500 colums of each run (the rows are the steps)

#Arrays
np_aw_t = np.transpose(np.array(all_walks)) #creates an array of the 2d list

ends = np_aw_t[-1,:] #selects the final row (so at which step you end up)

#Plotting
plot1 = plt.figure(1) 
plt.hist(ends)
plt.show()
