from aocd import data
from functools import cache

def split_stone(stone):
	stone_str = str(stone)
	midpoint = len(stone_str) // 2
	return int(stone_str[:midpoint]), int(stone_str[midpoint:])

@cache
def blink(stone, num_blinks):
	if num_blinks != 0:
		new_num_blinks = num_blinks - 1
		if stone == 0:
			return blink(1, new_num_blinks)
		elif len(str(stone)) % 2 == 0:
			split_stones = split_stone(stone)
			return blink(split_stones[0], new_num_blinks) + blink(split_stones[1], new_num_blinks)
		else:
			return blink(stone * 2024, new_num_blinks)
	return 1


stones = [int(x) for x in data.split()]

print('Part 1:', sum(blink(stone, 25) for stone in stones))
print('Part 2:', sum(blink(stone, 75) for stone in stones))