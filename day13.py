from aocd import data
import re
from sympy import symbols
from sympy.core.numbers import Integer
from sympy.solvers.solveset import linsolve

def solve(button_a, button_b, prize):
	x, y = symbols('x, y')
	result = list(linsolve([button_a[0]*x + button_b[0]*y - prize[0], button_a[1]*x + button_b[1]*y -prize[1] ], (x, y)))[0]
	if len(result) > 0:
		if type(result[0]) is Integer and type(result[1]) is Integer:
			return result[0]*3 + result[1]
	
	return 0 

def run_all_machines(data, prize_offset=0):
	sum = 0
	for machine in data:
		button_a, button_b, prize = zip(*[iter(map(int, re.findall(r'\d+', machine)))] * 2)
		prize = [p + prize_offset for p in prize]
		sum += solve(button_a, button_b, prize)
	return sum

data = data.split('\n\n')
print('Part 1:', run_all_machines(data))
print('Part 2:', run_all_machines(data, prize_offset=10000000000000))