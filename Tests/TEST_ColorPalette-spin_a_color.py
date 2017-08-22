# from Harklepalette import Color
# from Harklepalette import ColorPalette
# from .. import Harklepalette
# import ..Harklepalette

import unittest
import os, sys
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
		return


	def test_02_Starting_Color_Invalid(self):
		return


	def test_03_Offset_Non_Integer(self):
		return


	def test_04_Skip_Greyscale_Non_Bool(self):
		return


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