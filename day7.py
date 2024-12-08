from aocd import data
import re
from itertools import product

def is_valid(nums, operators):
	ans, start_value, line_nums = nums[0], nums[1], nums[2:]
	curr_value = start_value
	for i in range(len(operators)):
		if operators[i] == 1:
			curr_value += line_nums[i]
		elif operators[i] == 0:
			curr_value *= line_nums[i]
		else:
			curr_value = int(str(curr_value) + str(line_nums[i]))
	return curr_value == ans

valid_p1 = 0
def count_valid_lines():
	valid_p1 = 0
	valid_p2 = 0

	lines = data.splitlines()

	for i, line in enumerate(lines):
		print(f'{i}/{len(lines)}', end='\r')
		line_nums = [int(x) for x in re.findall(r'\d+', line)]
		num_operators = len(line_nums) - 2

		#all * and + combos
		options = list(product([1,0], repeat=num_operators))

		if any(is_valid(line_nums, o) for o in options):
			valid_p1 += line_nums[0]
			valid_p2 += line_nums[0]
			
		else:
			options = [o for o in product([1, 0, -1], repeat=num_operators) if -1 in o]
			if any(is_valid(line_nums, o) for o in options):
				valid_p2 += line_nums[0]

	return valid_p1, valid_p2
			
valid_p1, valid_p2 = count_valid_lines()
print('Part 1:', valid_p1)
print('Part 2:', valid_p2)
