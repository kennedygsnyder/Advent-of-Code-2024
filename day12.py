from aocd import data
from utils.grid import MapGrid, C, get_neighbors, Grid
from collections import deque


class Garden(MapGrid):
	def get_region(self, start_pos):
		region = set([start_pos])
		plant = self[start_pos]
		q = deque([start_pos])

		while q:
			curr_pos = q.popleft()
			neighbors = [n for n in get_neighbors(curr_pos) if ((n in self) and (n not in region) and (self[n] == plant))]
			for n in neighbors:
				region.add(n)
				q.append(n)

		return region
	
	def get_regions(self):
		regions = []
		visited = set()
		for region_start in self.keys():
			if region_start not in visited:
				region = self.get_region(region_start)
				regions.append(region)
				visited.update(region)
		return regions

def get_perimeter(region):
	perimeter = 0
	for pt in region:
		neighbors = get_neighbors(pt)
		for n in neighbors:
			if n not in region:
				perimeter += 1
	return perimeter

def get_discounted_perimeter(region):
	num_corners = 0
	corners = [C(-.5, -.5), C(-.5,.5), C(.5,.5), C(.5,-.5)]
	# get test points
	perimeter_points = set()
	for pt in region:
		perimeter_points.update(pt + c for c in corners)
	
	for peri_pt in perimeter_points:
		peri_pt_neighbors = [(peri_pt + c in region) for c in corners]

		if sum(peri_pt_neighbors) in (1,3):
			num_corners += 1
		elif peri_pt_neighbors == [0,1,0,1] or peri_pt_neighbors == [1,0,1,0]:
			num_corners += 2
	return(num_corners)

g = Garden(data)

regions = g.get_regions()
print('Part 1:', sum(len(region) * get_perimeter(region) for region in regions))
print('Part 2:', sum(len(region) * get_discounted_perimeter(region) for region in regions))