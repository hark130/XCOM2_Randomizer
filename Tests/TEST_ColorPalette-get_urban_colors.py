from random import randint
import math  # calc_standard_deviation
import os, sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Harklepalette import Color
from Harklepalette import MainArmorPalette
from Harklepalette import SecondaryArmorPalette
from Harklepalette import WeaponColorPalette


def get_mean(listOfValues):
    ### INPUT VALIDATION ###
    if not isinstance(listOfValues, list):
        raise TypeError("List of values is not a list")
    elif listOfValues.__len__() == 0:
        raise ValueError("List of values is emtpy")

    ### LOCAL VARIABLES ###
    tmpSum = 0      # Temporary sum of the values
    mean = 0        # Calculated mean

    # Calculate the mean
    for value in listOfValues:
        tmpSum += value
    mean = tmpSum / listOfValues.__len__()

    return mean


def calc_standard_deviation(listOfValues):
    ### INPUT VALIDATION ###
    if not isinstance(listOfValues, list):
        raise TypeError("List of values is not a list")
    elif listOfValues.__len__() == 0:
        raise ValueError("List of values is emtpy")

    ### LOCAL VARIABLES ###
    tmpSum = 0      # Temporary sum of the values
    mean = 0        # Calculated mean
    variance = 0    # Calculated variance
    stanDev = 0     # Calculated standard deviation

    # Calculate the mean
    mean = get_mean(listOfValues)
    # print("Mean:\t{}".format(mean))  # DEBUGGING

    # Calculate the variance
    tmpSum = 0
    for value in listOfValues:
        tmpSum += math.pow((value - mean), 2)
    # print("Sum of mean deviation:\t{}".format(tmpSum))  # DEBUGGING
    variance = tmpSum / listOfValues.__len__()
    # print("Variance:\t{}".format(variance))  # DEBUGGING

    # Calculate the standard deviation
    stanDev = math.sqrt(variance)
    # print("Standard Deviation:\t{}".format(stanDev))  # DEBUGGING

    return stanDev


def compare_float_equivalency(float1, float2):
    ### INPUT VALIDATION ###
    if not isinstance(float1, float) and not isinstance(float1, int):
        raise TypeError("First float is not a valid number")
    elif not isinstance(float2, float) and not isinstance(float2, int):
        raise TypeError("Second float is not a valid number")

    ### LOCAL VARIABLES ###
    retVal = False          # Prove it wrong
    deviation = 0.01     # Degree of specificity
    val1 = 0.0
    val2 = 0.0

    # Ensure floats are actually floats
    if isinstance(float1, float):
        val1 = float1
    else:
        val1 = float(float1)
    if isinstance(float2, float):
        val2 = float2
    else:
        val2 = float(float2)

    # Compare the floats
    if (val1 + deviation > val2) and (val1 - deviation < val2):
        retVal = True
    # else:
    #     print("val1:\t{}val2:\t{}\n".format(val1, val2))

    return retVal


class UrbanColorTest(unittest.TestCase):


    def setUp(self):
        # Main Colors Available
        self.mainColorsImplemented = [ \
            61, 57, 25, 4, 40, 41, \
            69, 80, 83, 35, 93, 75, \
            19, 41, 60, 91, 68, 62, \
            57, 53, 20, 4, 18, 22, \
            59, 68, 96, 64, 19, 80, \
        ]

        # Number of Tests
        self.numTests = 10000

        # List of Implemented Urban Color Combinations
        self.implementedColorCombos = [ \
            # Urban Scheme 01
            ( 61, 44, 82 ), \
            ( 57, 97, 83 ), \
            # Urban Scheme 02
            ( 25, 41, 73 ), \
            ( 4, 87, 73 ), \
            # Urban Scheme 03
            ( 40, 78, 88 ), \
            ( 41, 77, 89 ), \
            # Urban Scheme 04
            ( 69, 71, 13 ), \
            ( 80, 20, 12 ), \
            # Urban Scheme 05
            ( 83, 14, 48 ), \
            ( 35, 73, 85 ), \
            # Urban Scheme 06
            ( 93, 84, 15 ), \
            ( 75, 96, 71 ), \
            # Urban Scheme 07
            ( 19, 18, 72 ), \
            ( 41, 40, 12 ), \
            # Urban Scheme 08
            ( 60, 96, 81 ), \
            ( 91, 64, 28 ), \
            # Urban Scheme 09
            ( 68, 20, 54 ), \
            ( 62, 94, 55 ), \
            # Urban Scheme 10
            ( 57, 9, 41 ), \
            ( 53, 60, 41 ), \
            # Urban Scheme 11
            ( 20, 41, 81 ), \
            ( 4, 11, 29 ), \
            # Urban Scheme 12
            ( 18, 36, 91 ), \
            ( 22, 35, 91 ), \
            # Urban Scheme 13
            ( 59, 56, 90 ), \
            ( 68, 17, 90 ), \
            # Urban Scheme 14
            ( 96, 56, 7 ), \
            ( 64, 50, 7 ), \
            # Urban Scheme 15
            ( 19, 70, 26 ), \
            ( 80, 38, 27 ), \
        ]

        # 3.7. Main Armor Color
        # 3.7.1. Armor Color Scheme
        self.armorColorScheme = "Urban"
        # 3.7.2. Instanstiate Main Armor Colors Object
        self.mainArmorColors = MainArmorPalette(self.armorColorScheme)
        # 3.8. Secondary Armor Color
        # 3.8.1. Instanstiate Secondary Armor Colors Object
        self.secondaryArmorColors = SecondaryArmorPalette(self.armorColorScheme)
        # 3.9. Weapon Color
        # 3.9.1. Instantiate Weapon Color Object
        self.weaponColors = WeaponColorPalette(self.armorColorScheme)


class NormalTests(UrbanColorTest):


    def test_01_Get_Main_Color(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()
        numRuns = self.numTests    # Number of iterations to make in this test

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            try:
                tmpRetVal = self.mainArmorColors.get_color()
            except Exception as err:
                self.fail("Raised an exception")
            else:
                self.assertTrue(tmpRetVal.num in self.mainColorsImplemented)


    def test_02_Get_Secondary_Color(self):
        ### LOCAL VARIABLES ###
        tmpMainColor = None         # Temporarily holds a Color object to pass into secondaryArmorColors.get_color()
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()
        numRuns = 0                 # Number of iterations to make in this test
        numCombos = 0               # Number of combos for a given Main color
        foundIt = False             # Represents whether the match was found
        numRuns = self.implementedColorCombos.__len__()

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            # Find the input Color object
            for swatch in self.mainArmorColors.listOfColors:
                if swatch.num == self.implementedColorCombos[x][0]:
                    tmpMainColor = swatch
                    break

            # Count occurences of the input Color object
            numCombos = 0  # Reset combo counter
            for combo in self.implementedColorCombos:
                if combo[0] == self.implementedColorCombos[x][0]:
                    numCombos += 1
            # print("Main {} from Combo {} has {} copies\n".format(tmpMainColor.num, self.implementedColorCombos[x], numCombos))  # DEBUGGING

            try:
                tmpRetVal = self.secondaryArmorColors.get_color(tmpMainColor)
            except Exception as err:
                self.fail("Raised an exception")
            else:
                foundIt = False  # Reset bool
                self.assertTrue(isinstance(tmpRetVal, Color))
                self.assertTrue(tmpRetVal != None)
                for combo in self.implementedColorCombos:
                    if combo[0] == tmpMainColor.num:
                        numCombos -= 1
                        if combo[1] == tmpRetVal.num:
                            foundIt = True  # Found it
                            break  # Stop looking
                        if numCombos == 0:
                            self.fail("Didn't find an Urban combo match for Main {} and Secondary {}\n".format(tmpMainColor.num, tmpRetVal.num))
                self.assertTrue(foundIt)


    def test_03_Get_Weapon_Color(self):
        ### LOCAL VARIABLES ###
        tmpMainColor = None         # Temporarily holds a Color object to pass into secondaryArmorColors.get_color()
        tmpSecColor = None          # Temporarily holds a Color object to pass into weaponColors.get_color()
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()
        numRuns = 0                 # Number of iterations to make in this test
        # numCombos = 0               # Number of combos for a given Main color
        foundIt = False             # Represents whether the match was found
        numRuns = self.implementedColorCombos.__len__()

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            # Find the input Color object
            for swatch in self.mainArmorColors.listOfColors:
                if swatch.num == self.implementedColorCombos[x][0]:
                    tmpMainColor = swatch
                    break

            # # Count occurences of the input Color object
            # numCombos = 0  # Reset combo counter
            # for combo in self.implementedColorCombos:
            #     if combo[0] == self.implementedColorCombos[x][0]:
            #         numCombos += 1
            # print("Main {} from Combo {} has {} copies\n".format(tmpMainColor.num, self.implementedColorCombos[x], numCombos))  # DEBUGGING

            try:
                tmpSecColor = self.secondaryArmorColors.get_color(tmpMainColor)
            except Exception as err:
                self.fail("Raised an exception")
            else:
                try:
                    tmpRetVal = self.weaponColors.get_color(tmpMainColor, tmpSecColor)
                except Exception as err:
                    self.fail("Raised an exception")
                else:
                    foundIt = False  # Reset bool
                    self.assertTrue(isinstance(tmpRetVal, Color))
                    self.assertTrue(tmpRetVal != None)
                    for combo in self.implementedColorCombos:
                        if combo[0] == tmpMainColor.num:
                            if combo[1] == tmpSecColor.num:
                                if combo[2] == tmpRetVal.num:
                                    foundIt = True  # Found it
                                    break  # Stop looking
                    self.assertTrue(foundIt)


    def test_04_Calc_Stan_Dev(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = 0
        testInputList = [ \
            ([ 1, 2, 3, 4, 5 ], math.sqrt(2)), \
            ([ 4, 5, 6, 5, 3, 2, 8, 0, 4, 6, 7, 8, 4, 5, 7, 9, 8, 6, 7, 5, 5, 4, 2, 1, 9, 3, 3, 4, 6, 4 ], 2.2509257355), \
            ([ 60, 56, 61, 68, 51, 53, 69, 54 ], 6.32), \
            ([ 1, 2, 3, 4, 5, 6 ], 1.7078251277), \
            ([ 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80 ], 0), \
            ([ 0, 0, 1, 15, 20 ], 8.56504524214554), \
            ([ 321, 267, 232, 304, 289, 342, 380, 403, 207, 294 ], 57.9628), \
            ([ 1, 5, 50, 98, 99, 100 ], 43.1331916536), \
        ]

        ### RUN THE TESTS ###
        for testInput, expectedOutput in testInputList:
            try:
                tmpRetVal = calc_standard_deviation(testInput)
            except Exception as err:
                print(repr(err))  # DEBUGGING
                self.fail("Raised an exception")
            else:
                # print("\nReturned:\t{}\nExpected:\t{}\n".format(tmpRetVal, expectedOutput))  # DEBUGGING
                self.assertTrue(compare_float_equivalency(tmpRetVal, expectedOutput))


class ErrorTests(UrbanColorTest):


    def test_01_Color_Palettes_Invalid_Parameter(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()
        # Various invalid values/types to pass into mainArmorColors.get_color()
        testInputList = [ \
            1, "two", 3.0, [ 4, "things", ("in", "a", "list") ], \
            { 5.1 : "things", 5.2 : "that", 5.3 : "don't", 5.4 : "belong" }, \
            self.mainArmorColors, self.secondaryArmorColors, self.weaponColors, \
        ]

        ### RUN THE TESTS ###
        for testInput in testInputList:
            try:
                tmpRetVal = self.mainArmorColors.get_color(testInput)
            except TypeError as err:
                self.assertTrue(err.args[0] == "Color to match is not of type Color or NoneType")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")

            try:
                tmpRetVal = self.secondaryArmorColors.get_color(testInput)
            except TypeError as err:
                self.assertTrue(err.args[0] == "Color to match is not of type Color or NoneType")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")

            try:
                tmpRetVal = self.weaponColors.get_color(testInput)
            except TypeError as err:
                self.assertTrue(err.args[0] == "Color to match is not of type Color or NoneType")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")


    def test_02_Color_Palettes_Invalid_2nd_Param(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()
        # Various invalid values/types to pass into mainArmorColors.get_color()
        testInputList = [ \
            1, "two", 3.0, [ 4, "things", ("in", "a", "list") ], \
            { 5.1 : "things", 5.2 : "that", 5.3 : "don't", 5.4 : "belong" }, \
            self.mainArmorColors, self.secondaryArmorColors, self.weaponColors, \
        ]

        ### RUN THE TESTS ###
        for testInput in testInputList:
            for swatch in self.mainArmorColors.listOfColors:
                try:
                    tmpRetVal = self.mainArmorColors.get_color(swatch, testInput)
                except TypeError as err:
                    self.assertTrue(err.args[0] == "Second color to match is not of type Color or NoneType")
                except Exception as err:
                    self.fail("Raised the wrong exception")
                else:
                    self.fail("Did not raise an exception")

            for swatch in self.secondaryArmorColors.listOfColors:
                try:
                    tmpRetVal = self.secondaryArmorColors.get_color(swatch, testInput)
                except TypeError as err:
                    self.assertTrue(err.args[0] == "Second color to match is not of type Color or NoneType")
                except Exception as err:
                    self.fail("Raised the wrong exception")
                else:
                    self.fail("Did not raise an exception")

            for swatch in self.weaponColors.listOfColors:
                try:
                    tmpRetVal = self.weaponColors.get_color(swatch, testInput)
                except TypeError as err:
                    self.assertTrue(err.args[0] == "Second color to match is not of type Color or NoneType")
                except Exception as err:
                    self.fail("Raised the wrong exception")
                else:
                    self.fail("Did not raise an exception")


    def test_03_Color_Palettes_None_1st_Param(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = None            # Temporarily holds Color object returned from get_color()

        ### RUN THE TESTS ###
        for swatch in self.mainArmorColors.listOfColors:
            try:
                tmpRetVal = self.mainArmorColors.get_color(None, swatch)
            except RuntimeError as err:
                self.assertTrue(err.args[0] == "Main color is blank but Secondary color is not")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")

        for swatch in self.secondaryArmorColors.listOfColors:
            try:
                tmpRetVal = self.secondaryArmorColors.get_color(None, swatch)
            except RuntimeError as err:
                self.assertTrue(err.args[0] == "Main color is blank but Secondary color is not")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")

        for swatch in self.weaponColors.listOfColors:
            try:
                tmpRetVal = self.weaponColors.get_color(None, swatch)
            except RuntimeError as err:
                self.assertTrue(err.args[0] == "Main color is blank but Secondary color is not")
            except Exception as err:
                self.fail("Raised the wrong exception")
            else:
                self.fail("Did not raise an exception")


class BoundaryTests(UrbanColorTest):
    pass


class SpecialTests(UrbanColorTest):


    def test_01_Standard_Deviation_of_Combos(self):
        ### LOCAL VARIABLES ###
        tmpMainColor = None             # Temporarily holds Color object returned from get_color()
        tmpSecondaryColor = None        # Temporarily holds Color object returned from get_color()
        tmpWeaponColor = None           # Temporarily holds Color object returned from get_color()
        numRuns = self.numTests * 10    # Number of iterations to make in this test
        randoComboCount = { }           # Dictionary of implementedColorCombos and their counts
        randoComboList = []             # List of all the counts
        standardDeviation = 0.0         # Calculated standard deviation
        mean = 0                        # Calcualted mean
        tmpCount = 0                    # Temporary counter

        # Initialize randoComboCount with keys and 0 values
        for combo in self.implementedColorCombos:
            randoComboCount[self.implementedColorCombos.index(combo)] = 0

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            try:
                tmpMainColor = self.mainArmorColors.get_color()
            except Exception as err:
                self.fail("Raised an exception")
            else:
                try:
                    tmpSecondaryColor = self.secondaryArmorColors.get_color(tmpMainColor)
                except Exception as err:
                    self.fail("Raised an exception")
                else:
                    try:
                        tmpWeaponColor = self.weaponColors.get_color(tmpMainColor, tmpSecondaryColor)
                    except Exception as err:
                        self.fail("Raised an exception")
                    else:
                        for combo in self.implementedColorCombos:
                            if combo[0] == tmpMainColor.num:
                                if combo[1] == tmpSecondaryColor.num:
                                    if combo[2] == tmpWeaponColor.num:
                                        randoComboCount[self.implementedColorCombos.index(combo)] += 1
                                        break  # Stop looking

        ### CALCULATE STANDARD DEVIATION ###
        # Prepare list of results
        for x in range(0, self.implementedColorCombos.__len__() - 1):
            randoComboList.append(randoComboCount[x])

        standardDeviation = calc_standard_deviation(randoComboList)
        mean = get_mean(randoComboList)

        # print("\nRandomized Combinations:\t{}\n".format(randoComboList))  # DEBUGGING
        # print("The standard deviation was {}".format(standardDeviation))
        # print("The mean was {}".format(mean))
        # print("1SD is between {} and {}".format(mean + standardDeviation, mean - standardDeviation))
        # print("Number of tests:\t{}".format(numRuns))
        # for key in randoComboCount.keys():
        #     print("Combo #{}:\t{}%".format(key, 100 * randoComboCount[key] / numRuns))

        # print("Standard deviation is {}% of the mean".format((standardDeviation / mean) * 100))
        # print("Standard deviation is {}% of the total number of runs".format(standardDeviation / (numRuns / randoComboList.__len__()) * 100))
        self.assertTrue(standardDeviation / (numRuns / randoComboList.__len__()) * 100 < 2.0)
        self.assertTrue(standardDeviation / mean * 100 < 2.0)

        # # Check 1SD
        # tmpCount = 0
        # x = 1
        # for entry in randoComboList:
        #     if (entry >= (mean - (x * standardDeviation))) and (entry <= (mean + (x * standardDeviation))):
        #         tmpCount += 1
        # print("1SD {}%".format((tmpCount / randoComboList.__len__()) * 100))
        # self.assertTrue((tmpCount / randoComboList.__len__()) >= .6826)

        # # Check 2SD
        # tmpCount = 0
        # x = 2
        # for entry in randoComboList:
        #     if (entry >= (mean - (x * standardDeviation))) and (entry <= (mean + (x * standardDeviation))):
        #         tmpCount += 1
        # print("2SD {}%".format((tmpCount / randoComboList.__len__()) * 100))
        # self.assertTrue((tmpCount / randoComboList.__len__()) >= .9544)

        # # Check 3SD
        # tmpCount = 0
        # x = 3
        # for entry in randoComboList:
        #     if (entry >= (mean - (x * standardDeviation))) and (entry <= (mean + (x * standardDeviation))):
        #         tmpCount += 1
        # print("3SD {}%".format((tmpCount / randoComboList.__len__()) * 100))
        # self.assertTrue((tmpCount / randoComboList.__len__()) >= .9972)



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