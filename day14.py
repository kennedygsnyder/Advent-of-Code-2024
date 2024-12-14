from aocd import data
import re
C = complex

class Robot():
	def __init__(self, pos, velocity):
		self.pos = C(pos[0], pos[1])
		self.velocity = C(velocity[0], velocity[1])
	
	def __repr__(self):
		return str(self.pos)
	
	def step(self, bounds):
		self.pos = self.pos + self.velocity 
		self.pos = C(self.pos.real % bounds[0], self.pos.imag % bounds[1])

class Bathroom():
	def __init__(self, robots, bounds):
		self.robots = robots
		self.bounds = bounds

	def step(self):
		for robot in self.robots:
			robot.step(self.bounds)

	def __repr__(self):

		repr = []
		for r in range(self.bounds[0]):
			row = ""
			for c in range(self.bounds[1]):
				num_robots = len([robot for robot in self.robots if robot.pos == C(r,c)])
				row += str(num_robots) if num_robots else "."
			repr.append(row)
		return '\n'.join(repr)
	
	def count_quadrants(self):
		safety_score = 1
		
		for yrng in (range(self.bounds[0]//2), range(self.bounds[0]//2+1, self.bounds[0])):
			for xrng in (range(self.bounds[1]//2), range(self.bounds[1]//2+1, self.bounds[1])):
				safety_score *= len([robot for robot in robots if robot.pos.real in yrng and robot.pos.imag in xrng])

		return safety_score

data = data.splitlines()

robots = []

for line in data:
	result = [int(d) for d in re.findall(r'-?\d+', line)]
	position = result[:2][::-1]
	velocity = result[2:][::-1]
	robots.append(Robot(position, velocity))

bathroom = Bathroom(robots, (103,101))
for i in range(100):
	bathroom.step()

p1 = bathroom.count_quadrants()

i = 100
new_len = 0
while new_len != len(bathroom.robots):
	bathroom.step()
	new_len = len(set([robot.pos for robot in bathroom.robots]))
	i += 1

pattern_lines = str(bathroom).splitlines()[44:77]
print('\n'.join([p[35:66] for p in pattern_lines]), '\n')
print('Part 1:', p1)
print('Part 2:', i)