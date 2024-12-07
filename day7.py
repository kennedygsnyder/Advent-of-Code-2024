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
valid_p2 = 0

lines = data.splitlines()
i = 1
for line_num in range(len(lines)):
	print(f'{i}/{len(lines)}', end='\r')
	line = [int(x) for x in re.findall(r'\d+', lines[line_num])]

	num_operators = len(line) - 2

	#all * and + combos
	options = list(product([1,0], repeat=num_operators))

	if any(is_valid(line, o) for o in options):
		valid_p1 += line[0]
		valid_p2 += line[0]
		
	else:
		options = [o for o in product([1, 0, -1], repeat=num_operators) if -1 in o]
		if any(is_valid(line, o) for o in options):
			valid_p2 += line[0]
	i += 1
		
print(valid_p1)
print(valid_p2)
