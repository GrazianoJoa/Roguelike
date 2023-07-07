import tcod
from input_handler import EventHandler
from entity import Entity
from engine import Engine
from Gmap import Map

def main():
	screen_width = 720
	screen_height = 480
	#Setting Tileset
	tileset = tcod.tileset.load_tilesheet("tiles.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
	
	map_width = 72
	map_height = 45
	
	#Setting up engine
	event_handler = EventHandler()
	player = Entity(int(screen_width / 18), int(screen_height / 16), "@", (255, 255, 255))
	npc = Entity(int(screen_width / 30), int(screen_height / 16), "@", (0, 0, 255))
	entities = {player, npc}
	
	gmap = Map(width=map_width, height=map_height)
	engine = Engine(entities=entities, event_handler=event_handler, gmap=gmap, player=player)
	
	#Window Manager
	with tcod.context.new(
		width=screen_width,
		height=screen_height,
		tileset=tileset,
		vsync=True,
		title="Roguelike!",
	) as context:
		while True:
			#The order determines NumPy array axes attributes. F, so arrays are indexing following [X,Y] 
			console = context.new_console(order="F")
			engine.render(console=console, context=context)
			
			#Waits to events
			events = tcod.event.wait()
			engine.handle_events(events)
if __name__ == "__main__":
	main()
