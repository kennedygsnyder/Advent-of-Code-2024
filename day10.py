from aocd import data
from utils.grid import Grid
from collections import deque

class Trailmap(Grid):
	def __init__(self, data):
		super().__init__(data)
		for k in self.keys():
			self[k] = int(self[k])

	def get_trailheads(self):
		trailheads = set()
		for k, v in self.items():
			if v == 0:
				trailheads.add(k)
		return trailheads
	
	def get_num_trails(self, pt_2=False):
		trailhead_total = 0
		for trailhead in self.get_trailheads():

			trailhead_sum = 0
			visited, queue = set([trailhead]), deque([trailhead])

			while queue:
				curr_pos = queue.popleft()

				if self[curr_pos] == 9:
					trailhead_sum += 1
				neighbors = [n for n in self.get_neighbors(curr_pos) if (pt_2 or (n not in visited)) and self[n] - self[curr_pos] == 1]
				for n in neighbors: 
					queue.append(n)
					visited.add(n)

			trailhead_total += trailhead_sum
		return trailhead_total

trailmap = Trailmap(data)

print('Part 1:', trailmap.get_num_trails())
print('Part 2:', trailmap.get_num_trails(pt_2=True))
