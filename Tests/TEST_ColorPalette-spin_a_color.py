# from Harklepalette import Color
# from Harklepalette import ColorPalette
# from .. import Harklepalette
# import ..Harklepalette

from random import randint
import os, sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Harklepalette import ColorPalette


class SpinTest(unittest.TestCase):


	def setUp(self):
		self.palette = ColorPalette("Monochromatic - Primary")
		self.colorDict = {}
		self.colorDict[0] = self.palette.validColors[0]		# "Red"
		self.colorDict[1] = self.palette.validColors[1]		# "Red Orange"
		self.colorDict[2] = self.palette.validColors[2]		# "Orange"
		self.colorDict[3] = self.palette.validColors[3]		# "Orange Yellow"
		self.colorDict[4] = self.palette.validColors[4]		# "Yellow"
		self.colorDict[5] = self.palette.validColors[5]		# "Yellow Green"
		self.colorDict[6] = self.palette.validColors[6]		# "Green"
		self.colorDict[7] = self.palette.validColors[7]		# "Green Blue"
		self.colorDict[8] = self.palette.validColors[8]		# "Blue"
		self.colorDict[9] = self.palette.validColors[9]		# "Blue Indigo"
		self.colorDict[10] = self.palette.validColors[10]	# "Indigo"
		self.colorDict[11] = self.palette.validColors[11]	# "Indigo Violet"
		self.colorDict[12] = self.palette.validColors[12]	# "Violet"
		self.colorDict[13] = self.palette.validColors[13]	# "Violet Red"


class NormalTests(SpinTest):


	def test_01_Spin_One(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 1	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_02_Spin_Neg_One(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -1	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_03_Spin_Seven(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 7	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_04_Spin_Neg_Seven(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -7	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


class ErrorTests(SpinTest):


	def test_01_Starting_Color_Non_String(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		# startingColor parameter for this test
		inputColors = [ \
			None, {1:"One"}, [2, "Two"], \
			(3, "Three"), int(4), float(5.00001), \
			self.palette, True, False, \
		]
		staticOffset = 0	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for inputColor in inputColors:
			try:
				tmpRetVal = self.palette.spin_a_color(inputColor, staticOffset, skipGrey)
			except TypeError as err:
				self.assertTrue(err.args[0] == "Starting color is not a string")
			except Exception as err:
				self.fail("Raised the wrong exception")
			else:
				self.fail("Did not raise an exception")


	def test_02_Starting_Color_Invalid(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		# startingColor parameter for this test
		inputColors = [ \
			"No", "Bad", "Invalid", \
			"Colors are nice", "Some color", "color scheme", \
			"ColorPalette", "Color", "Invalid starting color", \
		]
		for validColor in self.palette.validColors:
			# UPPER CASE
			inputColors.append(validColor.upper())
			# lower case
			inputColors.append(validColor.lower())
			# Slice off index[0]
			inputColors.append(validColor[1:])
			# Slice off index[n]
			inputColors.append(validColor[:validColor.__len__() - 2])

		staticOffset = 0	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for inputColor in inputColors:
			try:
				tmpRetVal = self.palette.spin_a_color(inputColor, staticOffset, skipGrey)
			except ValueError as err:
				self.assertTrue(err.args[0] == "Invalid starting color")
			except Exception as err:
				self.fail("Raised the wrong exception")
			else:
				self.fail("Did not raise an exception")


	def test_03_Offset_Non_Integer(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		# startingColor parameter for this test
		inputColor = self.palette.validColors[randint(0, self.palette.validColors.__len__() - 1)]
		staticOffsets = [ \
			None, {1:"One"}, [2, "Two"], \
			(3, "Three"), "Four", float(5.00001), \
			self.palette, \
		]
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for staticOffset in staticOffsets:
			try:
				tmpRetVal = self.palette.spin_a_color(inputColor, staticOffset, skipGrey)
			except TypeError as err:
				self.assertTrue(err.args[0] == "Offset is not an integer")
			except Exception as err:
				self.fail("Raised the wrong exception")
			else:
				self.fail("Did not raise an exception")


	def test_04_Skip_Greyscale_Non_Bool(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		# startingColor parameter for this test
		inputColor = self.palette.validColors[randint(0, self.palette.validColors.__len__() - 1)]
		staticOffset = 0	# Offset parameter for this test
		# skipGreyscale parameter for this test
		skipGreyInputs = [ \
			None, {1:"One"}, [2, "Two"], \
			(3, "Three"), int(4), float(5.00001), \
			"Six", self.palette, \
		]

		### RUN THE TESTS ###
		for skipGrey in skipGreyInputs:
			try:
				tmpRetVal = self.palette.spin_a_color(inputColor, staticOffset, skipGrey)
			except TypeError as err:
				self.assertTrue(err.args[0] == "Skip Greyscale is not a bool")
			except Exception as err:
				self.fail("Raised the wrong exception")
			else:
				self.fail("Did not raise an exception")


class BoundaryTests(SpinTest):


	def test_01_Spin_Thirteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 13	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_02_Spin_Neg_Thirteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -13	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_03_Spin_Fourteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 14	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_04_Spin_Neg_Fourteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -14	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_05_Spin_Fifteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 15	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_06_Spin_Neg_Fifteen(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -15	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_07_Spin_A_Lot(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 455	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


	def test_08_Spin_Neg_A_Lot(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = -455	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nExpected Result:\t{}".format(self.colorDict[((key + staticOffset) % 14)]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal == self.colorDict[((key + staticOffset) % 14)])


class SpecialTests(SpinTest):


	def test_01_Spin_Zero(self):
		### LOCAL VARIABLES ###
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 0	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test

		### RUN THE TESTS ###
		for key in self.colorDict.keys():
			try:
				tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
			except Exception as err:
				self.fail("Raised an exception")
			else:
				# print("\nInput:\t\t\t{}".format(self.colorDict[key]))
				# print("Actual Result:\t\t{}".format(tmpRetVal))
				self.assertTrue(tmpRetVal in self.palette.validColors)


	def test_02_Offset_Zero(self):
		### LOCAL VARIABLES ###
		numIterations = 10	# Number of times to loop through valid colors
		tmpRetVal = None  	# Temporarily holds return value from spin_a_color
		expectedKey = 0 	# Holds the calculated key of the expected return value
		staticOffset = 0	# Offset parameter for this test
		skipGrey = True 	# skipGreyscale parameter for this test
		testCounter = 0		# Counts the number of function calls that have been made
		randFailCount = 0	# Counts the number of times tmpRetVal == self.colorDict[key]

		### RUN THE TESTS ###
		for num in range(1, numIterations):
			for key in self.colorDict.keys():
				try:
					tmpRetVal = self.palette.spin_a_color(self.colorDict[key], staticOffset, skipGrey)
				except Exception as err:
					self.fail("Raised an exception")
				else:
					# Increment test counter
					testCounter += 1
					# Verify return value is valid
					self.assertTrue(tmpRetVal in self.palette.validColors)
					# Check tmpRetVal against the startingColor parameter
					if tmpRetVal == self.colorDict[key]:
						randFailCount += 1

		### CHECK THE NUMBER OF FAILURES TO RANDOMIZE A COLOR ###
		if (randFailCount / testCounter) > .25:
			self.fail("spin_a_color does not appear to be randomizing return values on offset 0")


if __name__ == "__main__":

	# Run all the tests!
    unittest.main(verbosity=2, exit=False)

	# # NormalTests
	# linkerSuite = unittest.TestLoader().loadTestsFromTestCase(NormalTests)
	# unittest.TextTestRunner(verbosity=2).run(linkerSuite)

	# # ErrorTests
	# linkerSuite = unittest.TestLoader().loadTestsFromTestCase(ErrorTests)
	# unittest.TextTestRunner(verbosity=2).run(linkerSuite)

	# # BoundaryTests
	# linkerSuite = unittest.TestLoader().loadTestsFromTestCase(BoundaryTests)
	# unittest.TextTestRunner(verbosity=2).run(linkerSuite)

	# # SpecialTests
	# linkerSuite = unittest.TestLoader().loadTestsFromTestCase(SpecialTests)
	# unittest.TextTestRunner(verbosity=2).run(linkerSuite)