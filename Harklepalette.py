class Color:
	'This class defines the attributes of one color'
	
	wheelColor = ""
	colorType = ""
	brightness = ""


	def __init__(self, number, hue, saturation, value):
		### INPUT VALIDATION ###
		if not isinstance(number, int):
			raise TypeError("number is not an int")
		elif not isinstance(hue, int):
			raise TypeError("hue is not an int")
		elif not isinstance(saturation, int):
			raise TypeError("saturation is not an int")
		elif not isinstance(value, int):
			raise TypeError("value is not an int")
		elif hue > 360 or hue < 0:
			raise ValueError("Invalid hue")
		elif saturation > 100 or saturation < 0:
			raise ValueError("Invalid saturation")
		elif value > 100 or value < 0:
			raise ValueError("Invalid value")

		### INITIALIZAITON ###
		self.num = number  		# Palette selection number
		self.hue = hue  		# Hue of the this color
		self.sat = saturation  	# Saturation of this color
		self.val = value  		# Value of this color
		self.wheelColor = self.determine_wheel_color()	
		self.colorType = self.determine_color_type()
		self.brightness = self.determine_brightness()


	def determine_wheel_color(self):
		### LOCAL VARIABLES ###
		retVal = "UNDEFINED"
		redHue = 0
		redOrangeHue = 19
		orangeHue = 38
		orangeYellowHue = 49
		yellowHue = 60
		yellowGreenHue = 90
		greenHue = 120
		greenBlueHue = 180
		blueHue = 240
		blueIndigoHue = 255
		indigoHue = 270
		indigoVioletHue = 285
		violetHue = 300
		violetRedHue = 330
		upperLimitHue = 360

		if self.hue >= redHue and self.hue < ((redHue + redOrangeHue) / 2):
			retVal = "Red"
		elif self.hue >= ((redHue + redOrangeHue) / 2) and self.hue < ((redOrangeHue + orangeHue) / 2):
			retVal = "Red Orange"
		elif self.hue >= ((redOrangeHue + orangeHue) / 2) and self.hue < ((orangeHue + orangeYellowHue) / 2):
			retVal = "Orange"
		elif self.hue >= ((orangeHue + orangeYellowHue) / 2) and self.hue < ((orangeYellowHue + yellowHue) / 2):
			retVal = "Orange Yellow"
		elif self.hue >= ((orangeYellowHue + yellowHue) / 2) and self.hue < ((yellowHue + yellowGreenHue) / 2):
			retVal = "Yellow"
		elif self.hue >= ((yellowHue + yellowGreenHue) / 2) and self.hue < ((yellowGreenHue + greenHue) / 2):
			retVal = "Yellow Green"
		elif self.hue >= ((yellowGreenHue + greenHue) / 2) and self.hue < ((greenHue + greenBlueHue) / 2):
			retVal = "Green"
		elif self.hue >= ((greenHue + greenBlueHue) / 2) and self.hue < ((greenBlueHue + blueHue) / 2):
			retVal = "Green Blue"
		elif self.hue >= ((greenBlueHue + blueHue) / 2) and self.hue < ((blueHue + blueIndigoHue) / 2):
			retVal = "Blue"
		elif self.hue >= ((blueHue + blueIndigoHue) / 2) and self.hue < ((blueIndigoHue + indigoHue) / 2):
			retVal = "Blue Indigo"
		elif self.hue >= ((blueIndigoHue + indigoHue) / 2) and self.hue < ((indigoHue + indigoVioletHue) / 2):
			retVal = "Indigo"
		elif self.hue >= ((indigoHue + indigoVioletHue) / 2) and self.hue < ((indigoVioletHue + violetHue) / 2):
			retVal = "Indigo Violet"
		elif self.hue >= ((indigoVioletHue + violetHue) / 2) and self.hue < ((violetHue + violetRedHue) / 2):
			retVal = "Violet"
		elif self.hue >= ((violetHue + violetRedHue) / 2) and self.hue < ((violetRedHue + upperLimitHue) / 2):
			retVal = "Violet Red"
		elif self.hue >= ((violetRedHue + upperLimitHue) / 2) and self.hue <= upperLimitHue:
			retVal = "Red"
		else:
			raise ValueError("Translation of hue fell out of bounds")

		return retVal


	def determine_color_type(self):
		retVal = "UNDEFINED"


		return retVal

	def determine_brightness(self):

		return "b"




