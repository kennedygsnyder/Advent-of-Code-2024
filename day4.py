from aocd import data
from utils.grid import Grid, C

neighbors = [C(0,-1), C(-1,-1), C(-1,0), C(-1,1), C(0,1), C(1,1), C(1,0), C(1,-1)]

def find_word(start_pos, neighbor_direction, grid, word):
	checkword = ""
	positions = set()
	while start_pos in grid and len(checkword) < len(word):
		checkword += grid[start_pos]
		positions.add(start_pos)
		start_pos += neighbor_direction
	
	if checkword == word:
		return positions

def part_1(g, word):
	
	height, width = g.end_y - g.start_y, g.end_x - g.start_x
	correct = set()
	count = 0
	for r in range(height):
		for c in range(width):
			for n in neighbors: 
				p = find_word(C(r,c), n, g, word)
				if p: 
					correct.update(p)
					count += 1
	return count

def part_2(grid, word):
	height, width = g.end_y - g.start_y, g.end_x - g.start_x
	count = 0
	# for every possible center
	for r in range(1, height - 1):
		for c in range(1, width - 1):
			pos = C(r,c)
			diagonals = ''.join([grid[pos + diff] for diff in [C(-1,-1), 0, C(1,1)]]), ''.join([grid[pos + diff] for diff in [C(-1,1), 0, C(1,-1)]])
			if all([d in [word, word[::-1]] for d in diagonals]):
				count += 1
			

	return count

g = Grid(data)

print('Part 1:', part_1(g, 'XMAS'))
print('Part 2:', part_2(g, "MAS"))