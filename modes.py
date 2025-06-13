
class Mode:
	modes = [
		"Steady", "Shadow_disappear",
		"Breathing", "Gaming Special Key",
		"Retro_snake", "Diagonal transformation",
		"Marquee effect",	"Flowing light and color",
		"Dazzling"
	]
	def __init__(self, id):
		self.name = Mode.modes[id]
		self.id = id
	
	def hex_data(self):
		# Values when mode does not support the property.
		# These values get ignored by keyboard, so theoretically
		# you can put any hex value and not get any errors.
		brt = "00" # brightness
		spd = "00" # speed
		cgp = "00" # color group

		if hasattr(self, 'brightness'):
			brt = "0" + str(self.brightness)
		if hasattr(self, 'speed'):
			spd = "0" + str(self.speed)
		if hasattr(self, 'color_group'):
			cgp = "0" + str(self.color_group)
			
		data = "0a" + f"{self.id+1:02d}" + cgp + spd + brt
		return f"{data:084}"


class Steady(Mode):
	def __init__(self, brightness=5):
		super().__init__(0)
		self.brightness = brightness

class ShadowDisappear(Mode):
	def __init__(self, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(1)
		self.speed = speed

class Breathing(Mode):
	def __init__(self, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(2)
		self.speed = speed

class GamingSpecialKey(Mode):
	color_group = [
		"FPS", "CF", "COD", "RTS",
		"LOL - ALL", "Car Race", "NBA", "LOL",
		"Custom1", "Custom2",
	]
	def __init__(self, brightness=5, color_group=0):
		super().__init__(3)
		self.brightness = brightness
		self.color_group = color_group

class RetroSnake(Mode):
	def __init__(self, brightness=5, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(4)
		self.brightness = brightness
		self.speed = speed

class DiagonalTransformation(Mode):
	def __init__(self, brightness=5, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(5)
		self.brightness = brightness
		self.speed = speed

class MarqueeEffect(Mode):
	def __init__(self, brightness=5, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(6)
		self.brightness = brightness
		self.speed = speed

class FlowingLightAndColor(Mode):
	def __init__(self, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(7)
		self.speed = speed

class Dazzling(Mode):
	def __init__(self, brightness=5, speed=3):
		""" speed[0-4]=3 (less is faster) """
		super().__init__(8)
		self.brightness = brightness
		self.speed = speed
