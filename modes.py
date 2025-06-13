
class Mode:
	modes = [
		"Steady",
		"Shadow_disappear",
		"Breathing",
		"Gaming Special Key",
		"Retro_snake",
		"Diagonal transformation",
		"Marquee effect",
		"Flowing light and color",
		"Dazzling"
	]
	def __init__(self, name):
		self.name = name
		self.id = Mode.modes.index(name)+1


class Steady(Mode):
	def __init__(self, brightness=5):
		super().__init__("Steady")
		self.brightness = brightness


class ShadowDisappear(Mode):
	def __init__(self, speed=4):
		super().__init__("Shadow_disappear")
		self.speed = speed


class Breathing(Mode):
	def __init__(self, speed=4):
		super().__init__("Breathing")
		self.speed = speed


class GamingSpecialKey(Mode):
	color_group = [
		"Custom2",
		"FPS",
		"CF",
		"COD",
		"RTS",
		"LOL - ALL",
		"Car Race",
		"NBA",
		"LOL",
		"Custom1",
	]
	def __init__(self, brightness=5, color_group=color_group.index("FPS")):
		super().__init__("Gaming Special Key")
		self.brightness = brightness
		self.color_group = color_group


class RetroSnake(Mode):
	def __init__(self, brightness=5, speed=4):
		super().__init__("Retro_snake")
		self.brightness = brightness
		self.speed = speed


class DiagonalTransformation(Mode):
	def __init__(self, brightness=5, speed=4):
		super().__init__("Diagonal transformation")
		self.brightness = brightness
		self.speed = speed


class MarqueeEffect(Mode):
	def __init__(self, brightness=5, speed=4):
		super().__init__("Marquee effect")
		self.brightness = brightness
		self.speed = speed


class FlowingLightAndColor(Mode):
	def __init__(self, speed=4):
		super().__init__("Flowing light and color")
		self.speed = speed


class Dazzling(Mode):
	def __init__(self, brightness=5, speed=4):
		super().__init__("Dazzling")
		self.brightness = brightness
		self.speed = speed


