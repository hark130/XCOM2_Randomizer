from random import randint
# from xrando import print_color_object


def print_color_object(colorToPrint):
    ### INPUT VALIDATION ###
    if not isinstance(colorToPrint, Color):
        raise TypeError("Color to print is not a Color object")

    print("Color Num:\t{}".format(colorToPrint.num))
    print("Color Hue:\t{}".format(colorToPrint.hue))
    print("Color Sat:\t{}".format(colorToPrint.sat))
    print("Color Val:\t{}".format(colorToPrint.val))
    print("Color Type:\t{}".format(colorToPrint.colorType))
    print("Brightness:\t{}".format(colorToPrint.brightness))
    print("Wheel Color:\t{}\n".format(colorToPrint.wheelColor))

    return


class Color:
	'This class defines the attributes of one color'
	
	wheelColor = ""
	colorType = ""
	brightness = ""
	validColors = [ \
		"Greyscale", "Red", "Red Orange", \
		"Orange", "Orange Yellow", "Yellow", \
		"Yellow Green", "Green", "Green Blue", \
		"Blue", "Blue Indigo", "Indigo", \
		"Indigo Violet", "Violet", "Violet Red", \
	]
	validTypes = [ \
		"Primary", "Secondary", "Tertiary", \
	]

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
		greyscaleSatThresh = 20  # Saturation threshold for a hue to be considered Greyscale
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

		### DETERMINE WHEEL COLOR ###
		if self.sat <= greyscaleSatThresh:
			retVal = "Greyscale"
		elif self.hue >= redHue and self.hue < ((redHue + redOrangeHue) / 2):
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
		### LOCAL VARIABLES ###
		retVal = "UNDEFINED"

		### INPUT VALIDATION ###
		if self.wheelColor == "" or self.wheelColor == "UNDEFINED":
			pass  # Return "UNDEFINED"
		elif self.wheelColor not in self.validColors:
			raise ValueError("Invalid wheel color")
		else:
			### DETERMINE COLOR TYPE ###
			if self.wheelColor == "Red" or self.wheelColor == "Yellow" or self.wheelColor == "Blue":
				retVal = "Primary"
			elif self.wheelColor == "Orange" or self.wheelColor == "Green" or self.wheelColor == "Violet":
				retVal = "Secondary"
			else:
				retVal = "Tertiary"

		return retVal


	def determine_brightness(self):
		### LOCAL VARIABLES ###
		retVal = "UNDEFINED"
		brightVal = 0  # Used to hold the computed sum of saturation and value
		lightThresh = (100 + 100) / 3
		mediumThresh = lightThresh * 2
		satWeight = .5
		valWeight = 2 - satWeight

		### INPUT VALIDATION ###
		if self.wheelColor == "" or self.wheelColor == "UNDEFINED":
			pass  # Return "UNDEFINED"
		elif self.wheelColor not in self.validColors:
			raise ValueError("Invalid wheel color")
		else:
			### DETERMINE BRIGHTNESS ###
			brightVal = (self.sat * satWeight) + ((100 - self.val) * valWeight)
			if brightVal <= lightThresh:
				retVal = "Light"
			elif brightVal <= mediumThresh:
				retVal = "Medium"
			else:
				retVal = "Dark"

		return retVal


class ColorPalette:
	'This class can randomly choose complimentary colors from a collection based on established color schemes'

	listOfColors = []  # This will hold all the colors available in this specific palette
	validColors = [ \
		"Greyscale", "Red", "Red Orange", \
		"Orange", "Orange Yellow", "Yellow", \
		"Yellow Green", "Green", "Green Blue", \
		"Blue", "Blue Indigo", "Indigo", \
		"Indigo Violet", "Violet", "Violet Red", \
	]
	validTypes = [ \
		"Primary", "Secondary", "Tertiary", \
	]
	validSchemes = [ \
		"Monochromatic - Primary", "Monochromatic - Secondary", "Monochromatic - Tertiary", \
		"2 Colors - Analogous", "2 Colors - Complementary", "3 Colors - Triad", \
		"3 Colors - Split Complementary", "3 Colors - Secondary", "Random Chaos", \
		"Earthy", "Urban", "Emo", \
	]
	implementedSchemes = [ \
		"Monochromatic - Primary", "Monochromatic - Secondary", "Monochromatic - Tertiary", \
	]
	listOfPrimaryColors = [ \
		"Red", "Yellow", "Blue", \
	]
	listOfSecondaryColors = [ \
		"Orange", "Green", "Violet", \
	]
	listOfTertiaryColors = [ \
		"Red Orange", "Orange Yellow", "Yellow Green", \
		"Green Blue", "Blue Indigo", "Indigo", \
		"Indigo Violet", "Violet Red", \
	]
	scheme = ""

	def __init__(self, scheme):
		### INPUT VALIDATION ###
		if not isinstance(scheme, str):
			raise TypeError("Color scheme is not an string")
		elif scheme not in self.validSchemes:
			raise ValueError("Invalid color scheme")
		elif scheme not in self.implementedSchemes:
			raise RuntimeError("This valid color scheme has not yet been implemented")

		### INITIALIZAITON ###
		self.scheme = scheme
		# print("This is the ColorPalette __init__()")  # DEBUGGING


	def count_colors(self, wheelColorToCount):
		'''
			PURPOSE:	Count the frequency of a given color in this palette's list of Colors
			INPUT:  	wheelColorToCount - A valid color to count in this color palette
			OUTPUT:  	The number of matching colors in this palette
		'''
		### INPUT VALIDATION ###
		if not isinstance(wheelColorToCount, str):
			raise TypeError("Wheel color is not a string")
		elif wheelColorToCount not in self.validColors:
			raise ValueError("Invalid wheel color")

		### LOCAL VARIABLES ###
		retVal = 0

		### COUNT THE COLORS ###
		for swatch in self.listOfColors:
			if swatch.wheelColor == wheelColorToCount:
				retVal += 1
		# print("Found {} objects of color '{}'".format(retVal, wheelColorToCount))  # DEBUGGING
		return retVal


	def get_color(self, colorToMatch = None):
		### INPUT VALIDATION ###
		if not isinstance(colorToMatch, Color) and colorToMatch is not None:
			print("get_color():\tcolorToMatch is of type {}\n".format(colorToMatch))  # DEBUGGING
			raise TypeError("Color to match is not of type Color or NoneType")
		########### WHY WAS THIS HERE? ###########
		# elif colorToMatch is not None:
		# 	if colorToMatch.colorType != "Primary":
		# 		raise ValueError("This function does not match non-Primary colors")
		elif self.scheme not in self.implementedSchemes:
			# print("get_color():\tcolorToMatch is of type {}\n".format(colorToMatch))  # DEBUGGING
			print("get_color():\tself.scheme is {}\n".format(self.scheme))  # DEBUGGING
			raise RuntimeError("This perfectly valid color scheme has not yet been implemented")

		### LOCAL VARIABLES ###
		retVal = None
		randColor = None
		primaryColorNum = 0
		secondaryColorNum = 0
		weaponColorNum = 0

		### CALL CORRESPONDING METHOD ###
		if self.scheme == "Monochromatic - Primary":
			# Get Primary Armor Color
			retVal = self.get_mono_primary(colorToMatch)
		elif self.scheme == "Monochromatic - Secondary":
			retVal = self.get_mono_secondary(colorToMatch)
		elif self.scheme == "Monochromatic - Tertiary":
			retVal = self.get_mono_tertiary(colorToMatch)
		############# IMPLEMENT MORE COLOR SCHEMES HERE #############
		else:
			raise RuntimeError("How did we get here?!")

		### EXTRACT THE COLOR NUMBER ###
		# retVal = randColor.num
		# retVal = randColor

		return retVal


	def get_mono_primary(self, colorToMatch = None):
		'''
			PURPOSE:	Get a primary color from the list of Colors in this palette
			INPUT:		colorToMatch - Color class to match against
			OUTPUT:		Color class of Type "Primary" that matches colorToMatch
			NOTE:
						If colorToMatch is None, will randomly select a primary wheelColor and then
							randomly select a Color from the palette's list to match that wheelColor
						If colorToMatch is a Color, will determine the Color's wheelColor and randomly
							select a Color from the palette's list to match that wheelColor
		'''
		### LOCAL VARIABLES ###
		retVal = None  			# Function's return value of type Color
		matchThisColor = None  	# Primary color to match
		numColors = 0  			# Holds of the number of given primary color in the list
		randNum = 0				# Holds a randomized value

		### GET PRIMARY COLOR ###
		# print("Color To Match is of type:\t{}\n".format(colorToMatch))  # DEBUGGING
		# 1. Determine primary color
		if colorToMatch is None:  # This is the starting color
			matchThisColor = self.listOfPrimaryColors[randint(0, self.listOfPrimaryColors.__len__() - 1)]
		else:
			matchThisColor = colorToMatch.wheelColor  # This is the color to match
			# print("get_mono_primary() colorToMatch:\n")  # DEBUGGING
			# print_color_object(colorToMatch)  # DEBUGGING
		# 2. Count the colors in the list
		numColors = self.count_colors(matchThisColor)
		if numColors <= 0:
			# raise ValueError("Could not find any {} colors".format(matchThisColor))
			# print("Could not find any {} colors".format(matchThisColor))  # DEBUGGING
			matchThisColor = "Greyscale"
			numColors = self.count_colors(matchThisColor)
		# 3. Randomly choose a color
		randNum = randint(1, numColors)
		# 4. Find the randNum'th Color in this palette's list
		for swatch in self.listOfColors:
			if swatch.wheelColor == matchThisColor:
				randNum -= 1
				if randNum == 0:
					retVal = swatch
					break

		# print("get_mono_primary() Randomized Color:\n")  # DEBUGGING
		# print_color_object(retVal)  # DEBUGGING
		return retVal


	def get_mono_secondary(self, colorToMatch = None):
		'''
			PURPOSE:	Get a secondary color from the list of Colors in this palette
			INPUT:		colorToMatch - Color class to match against
			OUTPUT:		Color class of Type "Secondary" that matches colorToMatch
			NOTE:
						If colorToMatch is None, will randomly select a secondary wheelColor and then
							randomly select a Color from the palette's list to match that wheelColor
						If colorToMatch is a Color, will determine the Color's wheelColor and randomly
							select a Color from the palette's list to match that wheelColor
		'''
		### LOCAL VARIABLES ###
		retVal = None  			# Function's return value of type Color
		matchThisColor = None  	# Secondary color to match
		numColors = 0  			# Holds of the number of given secondary color in the list
		randNum = 0				# Holds a randomized value

		### GET SECONDARY COLOR ###
		# 1. Determine secondary color
		if colorToMatch is None:  # This is the starting color
			matchThisColor = self.listOfSecondaryColors[randint(0, self.listOfSecondaryColors.__len__() - 1)]
		else:
			matchThisColor = colorToMatch.wheelColor  # This is the color to match
		# 2. Count the colors in the list
		numColors = self.count_colors(matchThisColor)
		if numColors <= 0:
			# raise ValueError("Could not find any {} colors".format(matchThisColor))
			# print("Could not find any {} colors".format(matchThisColor))  # DEBUGGING
			matchThisColor = "Greyscale"
			numColors = self.count_colors(matchThisColor)
		# 3. Randomly choose a color
		randNum = randint(1, numColors)
		# 4. Find the randNum'th Color in this palette's list
		for swatch in self.listOfColors:
			if swatch.wheelColor == matchThisColor:
				randNum -= 1
				if randNum == 0:
					retVal = swatch
					break

		return retVal


	def get_mono_tertiary(self, colorToMatch = None):
		'''
			PURPOSE:	Get a tertiary color from the list of Colors in this palette
			INPUT:		colorToMatch - Color class to match against
			OUTPUT:		Color class of Type "Tertiary" that matches colorToMatch
			NOTE:
						If colorToMatch is None, will randomly select a tertiary wheelColor and then
							randomly select a Color from the palette's list to match that wheelColor
						If colorToMatch is a Color, will determine the Color's wheelColor and randomly
							select a Color from the palette's list to match that wheelColor
		'''
		### LOCAL VARIABLES ###
		retVal = None  			# Function's return value of type Color
		matchThisColor = None  	# Tertiary color to match
		numColors = 0  			# Holds of the number of given tertiary color in the list
		randNum = 0				# Holds a randomized value

		### GET TERTIARY COLOR ###
		# 1. Determine tertiary color
		if colorToMatch is None:  # This is the starting color
			matchThisColor = self.listOfTertiaryColors[randint(0, self.listOfTertiaryColors.__len__() - 1)]
		else:
			matchThisColor = colorToMatch.wheelColor  # This is the color to match
		# 2. Count the colors in the list
		numColors = self.count_colors(matchThisColor)
		if numColors <= 0:
			# raise ValueError("Could not find any {} colors".format(matchThisColor))
			# print("Could not find any {} colors".format(matchThisColor))  # DEBUGGING
			matchThisColor = "Greyscale"
			numColors = self.count_colors(matchThisColor)
		# 3. Randomly choose a color
		randNum = randint(1, numColors)
		# 4. Find the randNum'th Color in this palette's list
		for swatch in self.listOfColors:
			if swatch.wheelColor == matchThisColor:
				randNum -= 1
				if randNum == 0:
					retVal = swatch
					break

		return retVal


class MainArmorPalette(ColorPalette):
	'This class can randomly choose main armor colors from a collection based on established color schemes'

	def __init__(self, scheme):
		### INPUT VALIDATION ###
		if not isinstance(scheme, str):
			raise TypeError("Color scheme is not an string")
		elif scheme not in self.validSchemes:
			raise ValueError("Invalid color scheme")
		elif scheme not in self.implementedSchemes:
			raise RuntimeError("This valid color scheme has not yet been implemented")
		# print("This is the MainArmorPalette __init__()")  # DEBUGGING
		### INITIALIZAITON ###
		# super().__init__(scheme)
		self.scheme = scheme
		self.listOfColors = []
		self.listOfColors.append(Color(0, 72, 59, 20))
		self.listOfColors.append(Color(1, 118, 41, 24))
		self.listOfColors.append(Color(2, 32, 45, 26))
		self.listOfColors.append(Color(3, 33, 57, 58))
		self.listOfColors.append(Color(4, 31, 47, 84))
		self.listOfColors.append(Color(5, 206, 20, 14))
		self.listOfColors.append(Color(6, 194, 22, 31))
		self.listOfColors.append(Color(7, 0, 100, 40))
		self.listOfColors.append(Color(8, 0, 100, 23))
		self.listOfColors.append(Color(9, 357, 90, 24))

		self.listOfColors.append(Color(10, 359, 83, 27))
		self.listOfColors.append(Color(11, 358, 77, 29))
		self.listOfColors.append(Color(12, 357, 70, 30))
		self.listOfColors.append(Color(13, 356, 60, 31))
		self.listOfColors.append(Color(14, 21, 93, 90))
		self.listOfColors.append(Color(15, 17, 94, 58))
		self.listOfColors.append(Color(16, 19, 89, 59))
		self.listOfColors.append(Color(17, 23, 84, 60))
		self.listOfColors.append(Color(18, 25, 75, 62))
		self.listOfColors.append(Color(19, 26, 62, 62))

		self.listOfColors.append(Color(20, 28, 46, 63))
		self.listOfColors.append(Color(21, 43, 96, 100))
		self.listOfColors.append(Color(22, 35, 97, 73))
		self.listOfColors.append(Color(23, 37, 91, 71))
		self.listOfColors.append(Color(24, 39, 87, 71))
		self.listOfColors.append(Color(25, 42, 79, 68))
		self.listOfColors.append(Color(26, 45, 67, 67))
		self.listOfColors.append(Color(27, 44, 52, 68))
		self.listOfColors.append(Color(28, 78, 62, 22))
		self.listOfColors.append(Color(29, 68, 55, 11))

		self.listOfColors.append(Color(30, 70, 50, 14))
		self.listOfColors.append(Color(31, 69, 43, 17))
		self.listOfColors.append(Color(32, 72, 36, 22))
		self.listOfColors.append(Color(33, 79, 24, 26))
		self.listOfColors.append(Color(34, 82, 14, 31))
		self.listOfColors.append(Color(35, 222, 90, 34))
		self.listOfColors.append(Color(36, 223, 71, 16))
		self.listOfColors.append(Color(37, 223, 71, 20))
		self.listOfColors.append(Color(38, 220, 74, 24))
		self.listOfColors.append(Color(39, 217, 75, 28))

		self.listOfColors.append(Color(40, 213, 72, 31))
		self.listOfColors.append(Color(41, 211, 67, 33))
		self.listOfColors.append(Color(42, 256, 75, 31))
		self.listOfColors.append(Color(43, 268, 67, 15))
		self.listOfColors.append(Color(44, 262, 61, 19))
		self.listOfColors.append(Color(45, 259, 60, 24))
		self.listOfColors.append(Color(46, 257, 53, 29))
		self.listOfColors.append(Color(47, 256, 46, 36))
		self.listOfColors.append(Color(48, 250, 39, 43))
		self.listOfColors.append(Color(49, 25, 68, 22))

		self.listOfColors.append(Color(50, 24, 63, 13))
		self.listOfColors.append(Color(51, 26, 57, 16))
		self.listOfColors.append(Color(52, 24, 53, 18))
		self.listOfColors.append(Color(53, 22, 42, 22))
		self.listOfColors.append(Color(54, 20, 31, 26))
		self.listOfColors.append(Color(55, 19, 21, 31))
		self.listOfColors.append(Color(56, 200, 18, 13))
		self.listOfColors.append(Color(57, 195, 18, 17))
		self.listOfColors.append(Color(58, 206, 13, 22))
		self.listOfColors.append(Color(59, 210, 12, 27))

		self.listOfColors.append(Color(60, 206, 9, 32))
		self.listOfColors.append(Color(61, 192, 5, 37))
		self.listOfColors.append(Color(62, 204, 4, 44))
		self.listOfColors.append(Color(63, 240, 3, 45))
		self.listOfColors.append(Color(64, 240, 3, 54))
		self.listOfColors.append(Color(65, 240, 1, 60))
		self.listOfColors.append(Color(66, 0, 0, 68))
		self.listOfColors.append(Color(67, 240, 2, 75))
		self.listOfColors.append(Color(68, 0, 0, 81))
		self.listOfColors.append(Color(69, 0, 0, 88))

		self.listOfColors.append(Color(70, 356, 100, 63))
		self.listOfColors.append(Color(71, 9, 100, 35))
		self.listOfColors.append(Color(72, 6, 100, 25))
		self.listOfColors.append(Color(73, 15, 100, 100))
		self.listOfColors.append(Color(74, 15, 100, 84))
		self.listOfColors.append(Color(75, 19, 100, 48))
		self.listOfColors.append(Color(76, 60, 100, 100))
		self.listOfColors.append(Color(77, 51, 100, 100))
		self.listOfColors.append(Color(78, 43, 100, 85))
		self.listOfColors.append(Color(79, 114, 86, 72))

		self.listOfColors.append(Color(80, 91, 100, 37))
		self.listOfColors.append(Color(81, 100, 100, 20))
		self.listOfColors.append(Color(82, 235, 100, 100))
		self.listOfColors.append(Color(83, 237, 100, 100))
		self.listOfColors.append(Color(84, 237, 100, 71))
		self.listOfColors.append(Color(85, 261, 87, 100))
		self.listOfColors.append(Color(86, 256, 100, 65))
		self.listOfColors.append(Color(87, 259, 100, 35))
		self.listOfColors.append(Color(88, 300, 66, 100))
		self.listOfColors.append(Color(89, 321, 100, 100))

		self.listOfColors.append(Color(90, 333, 100, 88))
		self.listOfColors.append(Color(91, 0, 0, 100))
		self.listOfColors.append(Color(92, 0, 0, 100))
		self.listOfColors.append(Color(93, 0, 0, 86))
		self.listOfColors.append(Color(94, 207, 100, 4))
		self.listOfColors.append(Color(95, 204, 24, 8))
		self.listOfColors.append(Color(96, 210, 17, 9))
		self.listOfColors.append(Color(97, 177, 43, 21))

		# super().__init__(scheme)
		# count = 0
		# for swatch in self.listOfColors:
		# 	count += 1
		# print("Found {} Color objects in Main Armor Palette".format(count))  # DEBUGGING 


class SecondaryArmorPalette(ColorPalette):
	'This class can randomly choose secondary armor colors from a collection based on established color schemes'

	def __init__(self, scheme):
		### INPUT VALIDATION ###
		if not isinstance(scheme, str):
			raise TypeError("Color scheme is not an string")
		elif scheme not in self.validSchemes:
			raise ValueError("Invalid color scheme")
		elif scheme not in self.implementedSchemes:
			raise RuntimeError("This valid color scheme has not yet been implemented")
		# print("This is the SecondaryArmorPalette __init__()")  # DEBUGGING
		### INITIALIZAITON ###
		# super().__init__(scheme)
		self.scheme = scheme
		self.listOfColors = []
		self.listOfColors.append(Color(0, 39, 49, 14))
		self.listOfColors.append(Color(1, 48, 20, 20))
		self.listOfColors.append(Color(2, 38, 28, 34))
		self.listOfColors.append(Color(3, 48, 31, 13))
		self.listOfColors.append(Color(4, 43, 49, 17))
		self.listOfColors.append(Color(5, 53, 11, 29))
		self.listOfColors.append(Color(6, 33, 56, 31))
		self.listOfColors.append(Color(7, 34, 57, 37))
		self.listOfColors.append(Color(8, 34, 61, 22))
		self.listOfColors.append(Color(9, 32, 52, 26))

		self.listOfColors.append(Color(10, 31, 43, 30))
		self.listOfColors.append(Color(11, 29, 32, 35))
		self.listOfColors.append(Color(12, 26, 20, 41))
		self.listOfColors.append(Color(13, 25, 10, 45))
		self.listOfColors.append(Color(14, 203, 32, 29))
		self.listOfColors.append(Color(15, 204, 13, 15))
		self.listOfColors.append(Color(16, 210, 16, 20))
		self.listOfColors.append(Color(17, 208, 23, 26))
		self.listOfColors.append(Color(18, 213, 24, 33))
		self.listOfColors.append(Color(19, 218, 25, 40))

		self.listOfColors.append(Color(20, 218, 22, 48))
		self.listOfColors.append(Color(21, 24, 56, 20))
		self.listOfColors.append(Color(22, 21, 48, 11))
		self.listOfColors.append(Color(23, 26, 46, 14))
		self.listOfColors.append(Color(24, 21, 40, 17))
		self.listOfColors.append(Color(25, 19, 30, 21))
		self.listOfColors.append(Color(26, 9, 20, 25))
		self.listOfColors.append(Color(27, 0, 12, 30))
		self.listOfColors.append(Color(28, 40, 60, 20))
		self.listOfColors.append(Color(29, 34, 55, 11))

		self.listOfColors.append(Color(30, 39, 49, 14))
		self.listOfColors.append(Color(31, 38, 44, 17))
		self.listOfColors.append(Color(32, 40, 35, 20))
		self.listOfColors.append(Color(33, 39, 23, 24))
		self.listOfColors.append(Color(34, 36, 14, 29))
		self.listOfColors.append(Color(35, 30, 66, 39))
		self.listOfColors.append(Color(36, 27, 66, 23))
		self.listOfColors.append(Color(37, 27, 59, 27))
		self.listOfColors.append(Color(38, 27, 50, 31))
		self.listOfColors.append(Color(39, 26, 38, 35))

		self.listOfColors.append(Color(40, 25, 28, 41))
		self.listOfColors.append(Color(41, 18, 15, 45))
		self.listOfColors.append(Color(42, 53, 16, 22))
		self.listOfColors.append(Color(43, 42, 29, 14))
		self.listOfColors.append(Color(44, 38, 19, 16))
		self.listOfColors.append(Color(45, 36, 10, 20))
		self.listOfColors.append(Color(46, 30, 3, 25))
		self.listOfColors.append(Color(47, 240, 5, 32))
		self.listOfColors.append(Color(48, 240, 8, 40))
		self.listOfColors.append(Color(49, 209, 42, 20))

		self.listOfColors.append(Color(50, 216, 19, 10))
		self.listOfColors.append(Color(51, 213, 26, 13))
		self.listOfColors.append(Color(52, 210, 27, 17))
		self.listOfColors.append(Color(53, 215, 29, 23))
		self.listOfColors.append(Color(54, 216, 28, 28))
		self.listOfColors.append(Color(55, 221, 25, 35))
		self.listOfColors.append(Color(56, 220, 8, 45))
		self.listOfColors.append(Color(57, 230, 12, 40))
		self.listOfColors.append(Color(58, 222, 15, 34))
		self.listOfColors.append(Color(59, 224, 20, 29))

		self.listOfColors.append(Color(60, 219, 23, 24))
		self.listOfColors.append(Color(61, 224, 30, 20))
		self.listOfColors.append(Color(62, 225, 31, 15))
		self.listOfColors.append(Color(63, 200, 3, 39))
		self.listOfColors.append(Color(64, 210, 7, 34))
		self.listOfColors.append(Color(65, 200, 8, 28))
		self.listOfColors.append(Color(66, 204, 9, 23))
		self.listOfColors.append(Color(67, 216, 11, 18))
		self.listOfColors.append(Color(68, 195, 11, 14))
		self.listOfColors.append(Color(69, 200, 11, 11))
		
		self.listOfColors.append(Color(70, 114, 86, 72))
		self.listOfColors.append(Color(71, 91, 100, 37))
		self.listOfColors.append(Color(72, 100, 100, 20))
		self.listOfColors.append(Color(73, 235, 100, 100))
		self.listOfColors.append(Color(74, 237, 100, 100))
		self.listOfColors.append(Color(75, 237, 100, 71))
		self.listOfColors.append(Color(76, 261, 87, 100))
		self.listOfColors.append(Color(77, 256, 100, 65))
		self.listOfColors.append(Color(78, 259, 100, 35))
		self.listOfColors.append(Color(79, 356, 100, 63))

		self.listOfColors.append(Color(80, 9, 100, 35))
		self.listOfColors.append(Color(81, 6, 100, 25))
		self.listOfColors.append(Color(82, 15, 100, 100))
		self.listOfColors.append(Color(83, 15, 100, 84))
		self.listOfColors.append(Color(84, 19, 100, 48))
		self.listOfColors.append(Color(85, 60, 100, 100))
		self.listOfColors.append(Color(86, 51, 100, 100))
		self.listOfColors.append(Color(87, 43, 100, 85))
		self.listOfColors.append(Color(88, 333, 100, 88))
		self.listOfColors.append(Color(89, 321, 100, 100))

		self.listOfColors.append(Color(90, 300, 66, 100))
		self.listOfColors.append(Color(91, 207, 100, 4))
		self.listOfColors.append(Color(92, 204, 24, 8))
		self.listOfColors.append(Color(93, 210, 17, 9))
		self.listOfColors.append(Color(94, 0, 0, 100))
		self.listOfColors.append(Color(95, 0, 0, 100))
		self.listOfColors.append(Color(96, 0, 0, 86))
		self.listOfColors.append(Color(97, 177, 43, 20))

		# super().__init__(scheme)

		# for swatch in self.listOfColors:
		# 	print_color_object(swatch)
		# count = 0
		# for swatch in self.listOfColors:
		# 	count += 1
		# print("Found {} Color objects in Secondary Armor Palette".format(count))  # DEBUGGING 


# class WeaponColorPalette(ColorPalette):
class WeaponColorPalette(MainArmorPalette):
	'This class can randomly choose weapon colors from a collection based on established color schemes'
	# pass

	def __init__(self, scheme):
		super().__init__(scheme)

	# def __init__(self, scheme):
	# 	### INPUT VALIDATION ###
	# 	if not isinstance(scheme, str):
	# 		raise TypeError("Color scheme is not an string")
	# 	elif scheme not in self.validSchemes:
	# 		raise ValueError("Invalid color scheme")
	# 	elif scheme not in self.implementedSchemes:
	# 		raise RuntimeError("This valid color scheme has not yet been implemented")
	# 	print("This is the WeaponColorPalette __init__()")  # DEBUGGING
	# 	### INITIALIZAITON ###
	# 	# super().__init__(scheme)
	# 	self.scheme = scheme
	# 	self.listOfColors = []
	# 	self.listOfColors.append(Color(0, 72, 59, 20))
	# 	self.listOfColors.append(Color(1, 118, 41, 24))
	# 	self.listOfColors.append(Color(2, 32, 45, 26))
	# 	self.listOfColors.append(Color(3, 33, 57, 58))
	# 	self.listOfColors.append(Color(4, 31, 47, 84))
	# 	self.listOfColors.append(Color(5, 206, 20, 14))
	# 	self.listOfColors.append(Color(6, 194, 22, 31))
	# 	self.listOfColors.append(Color(7, 0, 100, 40))
	# 	self.listOfColors.append(Color(8, 0, 100, 23))
	# 	self.listOfColors.append(Color(9, 357, 90, 24))

	# 	self.listOfColors.append(Color(10, 359, 83, 27))
	# 	self.listOfColors.append(Color(11, 358, 77, 29))
	# 	self.listOfColors.append(Color(12, 357, 70, 30))
	# 	self.listOfColors.append(Color(13, 356, 60, 31))
	# 	self.listOfColors.append(Color(14, 21, 93, 90))
	# 	self.listOfColors.append(Color(15, 17, 94, 58))
	# 	self.listOfColors.append(Color(16, 19, 89, 59))
	# 	self.listOfColors.append(Color(17, 23, 84, 60))
	# 	self.listOfColors.append(Color(18, 25, 75, 62))
	# 	self.listOfColors.append(Color(19, 26, 62, 62))

	# 	self.listOfColors.append(Color(20, 28, 46, 63))
	# 	self.listOfColors.append(Color(21, 43, 96, 100))
	# 	self.listOfColors.append(Color(22, 35, 97, 73))
	# 	self.listOfColors.append(Color(23, 37, 91, 71))
	# 	self.listOfColors.append(Color(24, 39, 87, 71))
	# 	self.listOfColors.append(Color(25, 42, 79, 68))
	# 	self.listOfColors.append(Color(26, 45, 67, 67))
	# 	self.listOfColors.append(Color(27, 44, 52, 68))
	# 	self.listOfColors.append(Color(28, 78, 62, 22))
	# 	self.listOfColors.append(Color(29, 68, 55, 11))

	# 	self.listOfColors.append(Color(30, 70, 50, 14))
	# 	self.listOfColors.append(Color(31, 69, 43, 17))
	# 	self.listOfColors.append(Color(32, 72, 36, 22))
	# 	self.listOfColors.append(Color(33, 79, 24, 26))
	# 	self.listOfColors.append(Color(34, 82, 14, 31))
	# 	self.listOfColors.append(Color(35, 222, 90, 34))
	# 	self.listOfColors.append(Color(36, 223, 71, 16))
	# 	self.listOfColors.append(Color(37, 223, 71, 20))
	# 	self.listOfColors.append(Color(38, 220, 74, 24))
	# 	self.listOfColors.append(Color(39, 217, 75, 28))

	# 	self.listOfColors.append(Color(40, 213, 72, 31))
	# 	self.listOfColors.append(Color(41, 211, 67, 33))
	# 	self.listOfColors.append(Color(42, 256, 75, 31))
	# 	self.listOfColors.append(Color(43, 268, 67, 15))
	# 	self.listOfColors.append(Color(44, 262, 61, 19))
	# 	self.listOfColors.append(Color(45, 259, 60, 24))
	# 	self.listOfColors.append(Color(46, 257, 53, 29))
	# 	self.listOfColors.append(Color(47, 256, 46, 36))
	# 	self.listOfColors.append(Color(48, 250, 39, 43))
	# 	self.listOfColors.append(Color(49, 25, 68, 22))

	# 	self.listOfColors.append(Color(50, 24, 63, 13))
	# 	self.listOfColors.append(Color(51, 26, 57, 16))
	# 	self.listOfColors.append(Color(52, 24, 53, 18))
	# 	self.listOfColors.append(Color(53, 22, 42, 22))
	# 	self.listOfColors.append(Color(54, 20, 31, 26))
	# 	self.listOfColors.append(Color(55, 19, 21, 31))
	# 	self.listOfColors.append(Color(56, 200, 18, 13))
	# 	self.listOfColors.append(Color(57, 195, 18, 17))
	# 	self.listOfColors.append(Color(58, 206, 13, 22))
	# 	self.listOfColors.append(Color(59, 210, 12, 27))

	# 	self.listOfColors.append(Color(60, 206, 9, 32))
	# 	self.listOfColors.append(Color(61, 192, 5, 37))
	# 	self.listOfColors.append(Color(62, 204, 4, 44))
	# 	self.listOfColors.append(Color(63, 240, 3, 45))
	# 	self.listOfColors.append(Color(64, 240, 3, 54))
	# 	self.listOfColors.append(Color(65, 240, 1, 60))
	# 	self.listOfColors.append(Color(66, 0, 0, 68))
	# 	self.listOfColors.append(Color(67, 240, 2, 75))
	# 	self.listOfColors.append(Color(68, 0, 0, 81))
	# 	self.listOfColors.append(Color(69, 0, 0, 88))

	# 	self.listOfColors.append(Color(70, 356, 100, 63))
	# 	self.listOfColors.append(Color(71, 9, 100, 35))
	# 	self.listOfColors.append(Color(72, 6, 100, 25))
	# 	self.listOfColors.append(Color(73, 15, 100, 100))
	# 	self.listOfColors.append(Color(74, 15, 100, 84))
	# 	self.listOfColors.append(Color(75, 19, 100, 48))
	# 	self.listOfColors.append(Color(76, 60, 100, 100))
	# 	self.listOfColors.append(Color(77, 51, 100, 100))
	# 	self.listOfColors.append(Color(78, 43, 100, 85))
	# 	self.listOfColors.append(Color(79, 114, 86, 72))

	# 	self.listOfColors.append(Color(80, 91, 100, 37))
	# 	self.listOfColors.append(Color(81, 100, 100, 20))
	# 	self.listOfColors.append(Color(82, 235, 100, 100))
	# 	self.listOfColors.append(Color(83, 237, 100, 100))
	# 	self.listOfColors.append(Color(84, 237, 100, 71))
	# 	self.listOfColors.append(Color(85, 261, 87, 100))
	# 	self.listOfColors.append(Color(86, 256, 100, 65))
	# 	self.listOfColors.append(Color(87, 259, 100, 35))
	# 	self.listOfColors.append(Color(88, 300, 66, 100))
	# 	self.listOfColors.append(Color(89, 321, 100, 100))

	# 	self.listOfColors.append(Color(90, 333, 100, 88))
	# 	self.listOfColors.append(Color(91, 0, 0, 100))
	# 	self.listOfColors.append(Color(92, 0, 0, 100))
	# 	self.listOfColors.append(Color(93, 0, 0, 86))
	# 	self.listOfColors.append(Color(94, 207, 100, 4))
	# 	self.listOfColors.append(Color(95, 204, 24, 8))
	# 	self.listOfColors.append(Color(96, 210, 17, 9))
	# 	self.listOfColors.append(Color(97, 177, 43, 21))

	# 	# super().__init__(scheme)
	# 	count = 0
	# 	for swatch in self.listOfColors:
	# 		count += 1
	# 	print("Found {} Color objects in Weapon Color Palette".format(count))  # DEBUGGING 

