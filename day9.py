from collections import namedtuple, deque
from aocd import data
from copy import copy

Chunk = namedtuple("chunk", ["start_id", "length", "value"])

class Diskmap(list):
	def __init__(self, data):
		self.file_chunks = []
		self.empty_chunks = []
		curr_block_id = 0
		data_mode = True
		disk_map = []

		for i in range(len(data)):
			num_entries = int(data[i])
			if data_mode:
				self.file_chunks.append(Chunk(len(disk_map), num_entries, curr_block_id))
				for j in range(num_entries):
					disk_map.append(curr_block_id)
				curr_block_id += 1
			else:
				self.empty_chunks.append(Chunk(len(disk_map), num_entries, None))
				for j in range(num_entries):
					disk_map.append(None)

			data_mode = not data_mode

		self.file_chunks = self.file_chunks[::-1]

		super().__init__(disk_map)
	
	def __repr__(self):
		return ''.join(x if x is not None else '.' for x in self)
	
	def reorder_blocks(self):
		num_empty = self.count(None)
		to_move = deque([x for x in self[-num_empty:] if x is not None][::-1])
		
		new_disk_map = []
		i = 0
		while i < len(self) - num_empty:
			if self[i] is None:
				new_disk_map.append(to_move.popleft())
			else:
				new_disk_map.append(self[i])
			i += 1

		self[:] = new_disk_map + [None] * num_empty

	def reorder_files(self):

		for file_chunk in self.file_chunks:
			empty_chunk, empty_chunk_index = next(((chunk, i) for i, chunk in enumerate(self.empty_chunks) if chunk.length >= file_chunk.length and chunk.start_id < file_chunk.start_id), (None, None))

			if empty_chunk is not None:
				self[file_chunk.start_id:file_chunk.start_id + file_chunk.length] = [None] * file_chunk.length
				self[empty_chunk.start_id:empty_chunk.start_id + file_chunk.length] = [file_chunk.value] * file_chunk.length
				
				if file_chunk.length == empty_chunk.length:
					self.empty_chunks.remove(empty_chunk)
				else:
					self.empty_chunks[empty_chunk_index] = Chunk(empty_chunk.start_id + file_chunk.length, empty_chunk.length - file_chunk.length, None)

	def get_checksum(self):
		checksum = 0
		for i, val in enumerate(self):
			if val is not None:
				checksum += i * int(val)
		return checksum


pt1 = Diskmap(data)
pt2 = copy(pt1)

pt1.reorder_blocks()
print('Part 1:', pt1.get_checksum())

pt2.reorder_files()
print('Part 2:', pt2.get_checksum())