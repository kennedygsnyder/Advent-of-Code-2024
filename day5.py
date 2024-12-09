import re

from aocd import data

matches, page_lists = [x.split('\n') for x in data.split('\n\n')]

rules = [(a,b) for line in matches for a,b in line.split('|')]

incorrect_orders = []
count = 0
for line in page_lists:
	match = True
	for rule in rules:
		a, b = rule[0], rule[1]
		if a in line and b in line:
			rule = r".*" + a + r"(?=.*" + b + r").*"
			if not re.fullmatch(rule, line):
				match = False
	if match:
		nums = [int(x) for x in line.split(',')]
		count += nums[len(nums)//2]
	else:
		incorrect_orders.append(line)
print(count)


'''
PART TWO
'''

iters = len(incorrect_orders)
i = 1
incorrect_orders = [[int(x) for x in order.split(',')] for order in incorrect_orders]
rules = [[int(x) for x in rule] for rule in rules]

count = 0
for order in incorrect_orders:
	subrules = [rule for rule in rules if rule[0] in order and rule[1] in order]
	
	while not all([order.index(rule[0]) < order.index(rule[1]) for rule in subrules]):
		for rule in subrules:
			a, b = order.index(rule[0]), order.index(rule[1])
			if a > b:
				order[a], order[b] = order[b], order[a]
	count += order[len(order)//2]

print(count)