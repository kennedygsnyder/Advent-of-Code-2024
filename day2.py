from aocd import data

def is_safe(line):
  diffs = [x-y for x, y in zip(line[1:], line)]
  all_same_sign = False
  if diffs[0] >= 0:
    all_same_sign = not any(i < 0 for i in diffs)
  else:
    all_same_sign =  not any(i >= 0 for i in diffs)
  if all_same_sign:
    abs_list = [abs(x) for x in diffs]
    if any((x < 1 or x > 3) for x in abs_list):
      return False
    else: 
      return True
  else:
    return False
    
data = [[int(x) for x in y.split()] for y in data.split('\n')]

safe_count = 0
print(sum([is_safe(line) for line in data]))

safe_count = 0
for line in data:
  if is_safe(line):
    safe_count += 1
  else:
    test_lines = []
    for i in range(len(line)):
      test_lines.append(line[:i] + line[i+1:])
    if any(is_safe(x) for x in test_lines):
      safe_count += 1

print(safe_count)
