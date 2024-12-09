from aocd import data
from utils.grid import Grid, C

def get_grid():

	lines = data.split('\n')

	for i, line in enumerate(lines):
		if '^' in line:
			guard_position = i, line.index('^')
			break

	g = Grid('\n'.join(lines))
	return g, C(*guard_position)

# get grid and guard location
g, guard_pos = get_grid()

# guard movement tracking
next_step = {0: C(-1,0), 1:C(0,1), 2:C(1,0), 3:C(0,-1)}
visited = set([guard_pos])
current_dir = 0

# patrol until guard exits grid
while guard_pos + next_step[current_dir] in g:
	if g[guard_pos + next_step[current_dir]] == '#':
		current_dir = (current_dir+1)%4

	guard_pos = guard_pos + next_step[current_dir]
	visited.add(guard_pos)

print('Part 1:', len(visited))


# part 2
neighbors = [C(-1,0), C(0,1), C(1,0), C(0,-1)]
potential_obstacle_locations = visited
width, height = g.size()
infinite_count = 0
num = height * width
i = 0

for i, loc in enumerate(potential_obstacle_locations):
	print(f'Part 2: Loading ... {i / num * 100:.0f}%', end="\r")

	# reset grid and locations
	g, guard_pos = get_grid()
	g[loc] = '#'

	# set up cache to detect loops
	cached_turns, current_dir = set([]), 0

	# keep moving until a turn repeats
	while guard_pos + next_step[current_dir] in g:
		new_guard_pos = guard_pos + next_step[current_dir]
		if g[new_guard_pos] == '#':
			if (new_guard_pos, current_dir) in cached_turns:
				infinite_count += 1
				break
			cached_turns.add((new_guard_pos, current_dir))
			current_dir = (current_dir+1)%4
		
		else:
			guard_pos = new_guard_pos

print('\r' + ' ' * 40, end='\r')	
print('Part 2:', infinite_count)
