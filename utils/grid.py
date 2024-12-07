from typing import Union, Tuple
from collections import namedtuple

C = complex

GridBounds = namedtuple('GridBounds', ['start_y', 'start_x', 'height', 'width'])

class Grid(dict):
    
    def __init__(self, data=None, start_y=0, start_x=0, end_y=0, end_x=0, filler='.'):
        self.start_y, self.start_x = start_y, start_x
        self.end_y, self.end_x = end_y, end_x
        self.filler = filler

        if isinstance(data, dict):
           self.start_y, self.start_x = min([int(x.real) for x in list(data.keys())]), min([int(x.imag) for x in list(data.keys())])
           self.end_y, self.end_x = max([int(x.real) for x in list(data.keys())]) + 1, max([int(x.imag) for x in list(data.keys())]) + 1
           
           super().__init__(data)
        
        elif isinstance(data, str):
           self.from_string(data.split('\n'))
        
        else:
           raise ValueError("Unsupported data type. Must be a dictionary, string, or list.")
    
    @classmethod
    def blank(cls, start_x=0, start_y=0, width=0, height=0, filler='.'):
        d = {}
        for r in range(start_y, start_y + height):
            for c in range(start_x, start_x + width):
                d[C(r,c)] = filler
        return cls(d, filler=filler)

    def from_string(self, data):
        self.end_y, self.end_x = len(data) + self.start_y, max(len(line) for line in data) + self.start_x
        
        for r in range(self.start_y, self.end_y):
            for c in range(self.start_x, self.end_x):
                try:
                    self[C(r,c)] = data[r][c]
                except IndexError:
                    pass
                except: 
                    raise

    def __repr__(self):
        try:
            repr = []
            for r in range(self.start_y, self.end_y):
                row = ""
                for c in range(self.start_x, self.end_x):
                    row += self[C(r,c)] if C(r,c) in self else self.filler
                repr.append(row)
            return '\n'.join(repr)
        except:
            raise
    
    def size(self):
        """_summary_

        Returns:
            _tuple_: _(width, height)_
        """
        return (self.end_y - self.start_y, self.end_x - self.start_y)
    
    def mask(self, mask:set[C], mask_symbol:str="X", invert_mask:bool=False):
        if invert_mask:
            inverted_mask = set()
            for key in self.keys():
                if key not in mask:
                    inverted_mask.add(key)
            mask = inverted_mask

        masked_grid = Grid(self)

        for k in mask:
           masked_grid[k] = mask_symbol 
        
        return masked_grid
        
    def get_neighbors(self, pos:C, include_diagonals: bool=False) -> list:
        neighbors = [C(-1,0), C(0,1), C(1,0), C(0,-1)]
        if include_diagonals:
            neighbors += [C(-1,-1), C(-1,1), C(1,-1), C(1,1)]
  
        neighbors = [pos + n for n in neighbors if pos + n in self]
        return neighbors

def get_neighbors(point: Union[tuple, list, complex], bounds: Tuple[int, int, int, int] = None, flip_axes: bool=False, include_diagonals: bool=False) -> list:
  neighbors = [(-1,0), (0,1), (1,0), (0,-1)]
  if include_diagonals:
    neighbors += [(-1,-1), (-1,1), (1,-1), (1,1)]
  
  #import complex points & change neighbors
  if type(point) is C:
    y, x = point.real, point.imag

  #otherwise handle them normally  
  else:
    y, x = point

  if flip_axes:
    y, x = x, y
    bounds = bounds[2:4] + bounds[0:2]

  neighbors = [(y + dy, x+dx) for dy, dx in neighbors]
  if bounds:
    neighbors = [n for n in neighbors if n[0] in range(bounds[0], bounds[1]+1)]
    neighbors = [n for n in neighbors if n[1] in range(bounds[2], bounds[3]+1)]

  if type(point) is complex:
    neighbors = [complex(*x) for x in neighbors]

  return neighbors



if __name__ == '__main__':
    
    g = Grid({C(0,0):'X', C(0,1):'O', C(1,0):'V', C(1,1):'E'})
    assert(str(g) == "XO\nVE")
    g = Grid(data={C(0,0):'X', C(0,1):'O', C(1,0):'V', C(1,1):'E'}, start_x=2, start_y=2)
    assert(str(g) == "XO\nVE")
    g = Grid.blank(width=5, height=5)
    assert(str(g) == ".....\n.....\n.....\n.....\n.....")

    g = Grid('XOO\nOOX\nOXO')
    mask = set([C(0,0),C(1,1),C(2,2)])
    assert(str(g.mask(mask)) == "XOO\nOXX\nOXX")
    assert(str(g.mask(mask, invert_mask=True, mask_symbol='V')) == "XVV\nVOV\nVVO")

    g = Grid('OOO\nOOO\nOOO')
    mask = set([C(1,1)])

    hello = Grid("hello\nthere\n:)")
    assert(hello[C(2,0)] == ':')
    assert(C(2,3) not in hello)
    assert(str(hello) == "hello\nthere\n:)...")
    assert(hello.get_neighbors(C(2,0)) == [(1+0j), (2+1j)])
