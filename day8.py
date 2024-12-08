from aocd import data
from itertools import combinations
from math import gcd


def get_antenna_info(data):
	lines = data.splitlines()
	max_y, max_x = len(lines), len(lines[0])

	antennas = {}
	# loop through all characters and save locations of any antennas
	for r in range(max_y):
		for c, char in enumerate(lines[r]):
			if char != '.':
				antennas.setdefault(char, set()).add((r, c))
				
	return antennas, max_y, max_x

def part_1():
	antennas, max_y, max_x = get_antenna_info(data)

	antinode_locations = set()
	# loop through every antenna type
	for antenna_locations in antennas.values():
		# loop through all pairs of antennas
		for (x0, y0), (x1, y1) in combinations(antenna_locations, 2):
			# get both antinodes
			antinodes = (2*x0 - x1, 2*y0 - y1), (2*x1 - x0, 2*y1 - y0)
			
			for antinode in antinodes:
				if 0 <= antinode[0] < max_x and 0 <= antinode[1] < max_y:
					antinode_locations.add(antinode)

	return len(antinode_locations)

def part_2():
	antennas, max_y, max_x = get_antenna_info(data)
	
	antinode_locations = set()
	# loop through every antenna type
	for antenna_locations in antennas.values():
		# loop through all pairs of antennas
		for (x0, y0), (x1, y1) in combinations(antenna_locations, 2):
			# both directions 
			for direction in (-1, 1):
				# calculate slope to locate antinodes
				slope = (x1-x0, y1-y0)
				slope = slope[0] / gcd(*slope), slope[1] / gcd(*slope)
				
				# get antinodes
				x, y = x0, y0
				while 0 <= x < max_x and 0 <= y < max_y:
					antinode_locations.add((x,y))
					x += slope[0] * direction
					y += slope[1] * direction

	return len(antinode_locations)

print('Part 1:', part_1())
print('Part 2:', part_2())