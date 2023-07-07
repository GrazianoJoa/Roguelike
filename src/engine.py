from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handler import EventHandler
from Gmap import Map

#Responsable for drawing, handling input, ect.
class Engine:
	def __init__(self, entities: Set[Entity], event_handler: EventHandler, gmap: Map, player: Entity):
		self.entities = entities
		self.event_handler = event_handler
		self.gmap = gmap
		self.player = player
       
	def handle_events(self, events: Iterable[Any]) -> None:
		for event in events:
			action = self.event_handler.dispatch(event)
			
			if action is None:
				continue
				
			if isinstance(action, MovementAction):
				if self.gmap.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
					self.player.move(action.dx, action.dy)
			
			elif isinstance(action, EscapeAction):
				raise SystemExit()
	
	def render(self, console: Console, context: Context) -> None:
		self.gmap.render(console)
		for entity in self.entities:
			console.print(entity.x, entity.y, entity.char, entity.color)
		context.present(console, integer_scaling=True)
		console.clear()
