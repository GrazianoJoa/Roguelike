from typing import Tuple
import numpy
"""
	ch: Character (int format)
	fg: Foreground-color (3 Bytes)
	bg: Background-color (3 Bytes)
"""
graphic_dt = numpy.dtype(
	[
		("ch", numpy.int32),
		("fg", "3B"),
		("bg", "3B"),
	]
)

tile_dt = numpy.dtype(
	[
		("walkable", bool),
		("transparent", bool),
		("dark", graphic_dt),
	]
)

#Basic tiles generator
def new_tile(walkable: int, transparent: int, dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]]) -> numpy.ndarray:
	return numpy.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(walkable=True, transparent=True, dark=(ord(" "), (255,255,255), (50, 50, 150)))
wall = new_tile(walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)))
