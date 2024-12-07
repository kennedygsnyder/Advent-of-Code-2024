from aocd import data
import re

print('Part 1: ', sum([(int(x) * int(y)) for (x,y) in re.findall(r'mul\((\d*),(\d*)\)', data)]))
data = ''.join(line.strip() for line in data.splitlines())

data = data.split("don't")
clean_data = data[0]
for d in data:
  valid = re.findall(r'(?<=do\(\))(.*)', d)
  if len(valid):
    clean_data += valid[0]

print('Part 2: ', sum([(int(x) * int(y)) for (x,y) in re.findall(r'mul\((\d*),(\d*)\)', clean_data)]))

