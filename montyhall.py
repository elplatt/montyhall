import random

runs = 10000

keep_wins = 0
switch_wins = 0

for i in range(runs):
	# The doors
	doors = ['goat', 'goat', 'goat']
	
	# Randomly assign a car
	doors[random.randint(0,2)] = 'car'
	
	# Choose a door
	first_door = random.randint(0,2)
	
	# Eliminate a door containing a goat
	eliminated = [
		x
		for x in range(3)
		if x != first_door and doors[x] == 'goat'
		][0]

	# Record win stats
	if doors[first_door] == 'car':
		keep_wins += 1
	else:
		switch_wins += 1

print('{} runs'.format(runs))
print('keep wins: {:00.2f}%'.format(100 * keep_wins / runs))
print('switch wins: {:00.2f}%'.format(100 * switch_wins / runs))
