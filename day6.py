from aocd import data
import sys

from utils.grid import Grid, C

def get_grid():

	lines = data.split('\n')

	for i in range(len(lines)):
		if '^' in lines[i]:
			guard_location = i, lines[i].index('^')


	g = Grid('\n'.join(lines))
	return g, C(*guard_location)

g, guard_location = get_grid()
current_dir = 0
next_pos = {0: C(-1,0), 1:C(0,1), 2:C(1,0), 3:C(0,-1)}
visited = set([guard_location])
while guard_location + next_pos[current_dir] in g:
	if g[guard_location + next_pos[current_dir]] == '#':
		current_dir = (current_dir+1)%4

	guard_location = guard_location + next_pos[current_dir]
	visited.add(guard_location)

print('Part 1:', len(visited))
neighbors = [C(-1,0), C(0,1), C(1,0), C(0,-1)]
potential_obstacle_locations = visited


width, height = g.size()
infinite_count = 0
num = height * width
i = 0
for loc in potential_obstacle_locations:
	print(f'Part 2: Loading ... {i // 53.2 + 1:.0f}%', end="\r")
	sys.stdout.flush()
	cached_turns, current_dir = set([]), 0
	g, guard_location = get_grid()
	g[loc] = '#'

	while guard_location + next_pos[current_dir] in g:
		if g[guard_location + next_pos[current_dir]] == '#':
			if (guard_location + next_pos[current_dir], current_dir) in cached_turns:
				infinite_count += 1
				break
			cached_turns.add((guard_location + next_pos[current_dir], current_dir))
			current_dir = (current_dir+1)%4
		
		else:
			guard_location += next_pos[current_dir]
	i += 1


print('\r                                          ', end='\r')	
print('Part 2:', infinite_count)
