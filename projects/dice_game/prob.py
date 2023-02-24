end_60 = ends >= 60
s60 = sum(end_60)

print('Reached stair 60 or above ' + str(s60) + ' times')
s60prob = s60 / 500 * 100
print('This means there is a ' + str(s60prob) +"% chance you'll reach stair 60!")
