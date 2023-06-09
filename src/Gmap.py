import numpy
from tcod.console import Console
import tiles_types

class Map:
	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height
		self.tiles = numpy.full((width, height), fill_value=tiles_types.floor, order="F")
		self.tiles[30:33, 22] = tiles_types.wall
	
	def in_bounds(self, x: int, y: int) -> bool:
		return 0 < x < self.width and 0 < y < self.height
	
	def render(self, console: Console) -> None:
		console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
