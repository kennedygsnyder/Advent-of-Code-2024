from aocd import data
from collections import Counter

list_1, list_2 = [], []
for line in data.split('\n'):
  a, b = line.split()
  list_1.append(int(a))
  list_2.append(int(b))

list_1.sort()
list_2.sort()

diff = 0
for i, _ in enumerate(list_1):
  diff += abs(list_1[i] - list_2[i])

print('Part 1: ', diff)

similarity_score = 0
ct = Counter(list_2)

for item in list_1:
  similarity_score += item * ct[item]

print('Part 2: ', similarity_score)