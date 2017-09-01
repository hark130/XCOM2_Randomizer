from random import randint
import os, sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from xrando import rando_nation


class RandoNationTest(unittest.TestCase):


    def setUp(self):
        # Implemented Nations
        self.dictOfNations = { \
            "Argentina" : 0.95, "Australia" : 0.53, "Belgium" : 0.24, \
            "Brazil" : 4.52, "Canada" : 0.78, "China" : 29.71, \
            "Egypt" : 2.04, "France" : 1.39, "Germany" : 1.73, \
            "Greece" : 0.23, "India" : 28.73, "Ireland" : 0.10, \
            "Israel" : 0.18, "Italy" : 1.28, "Japan" : 2.70, \
            "Mexico" : 2.79, "Netherlands" : 0.36, "Nigeria" : 4.11, \
            "Norway" : 0.11, "Poland" : 0.83, "Russia" : 3.07, \
            "Saudi Arabia" : 0.70, "Scotland" : 0.11, \
            "South Africa" : 1.19, "South Korea" : 1.09, "Spain" : 0.99, \
            "Sweden" : 0.21, "Ukraine" : 0.95, "United Kingdom" : 1.40, \
            "USA" : 6.99, \
        }

        # Number of Tests
        self.numTests = 10000


class NormalTests(RandoNationTest):


    def test_01_Get_Rando_Nation(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = ""              # Temporarily holds Color object returned from get_color()
        numRuns = self.numTests     # Number of iterations to make in this test

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            try:
                tmpRetVal = rando_nation()
            except Exception as err:
                print(repr(err))  # DEBUGGING
                self.fail("Raised an exception")
            else:
                self.assertTrue(tmpRetVal in self.dictOfNations.keys())


class ErrorTests(RandoNationTest):
    pass


class BoundaryTests(RandoNationTest):
    pass


class SpecialTests(RandoNationTest):


    def test_01_Standard_Deviation_of_Combos(self):
        ### LOCAL VARIABLES ###
        tmpRetVal = ""                          # Holds the return value from rando_nation()
        testFactor = 100                        # Multiplied to numTests
        numRuns = self.numTests * testFactor    # Number of iterations to make in this test
        randoComboCount = { }                   # Dictionary of nations and their counts
        tmpDiff = 0                             # Temporary difference
        allowedDev = 0                          # Allowed deviation between Real and Rando

        # Initialize randoComboCount with keys and 0 values
        for nation in self.dictOfNations.keys():
            randoComboCount[nation] = 0

        ### RUN THE TESTS ###
        for x in range(0, numRuns - 1):
            try:
                tmpRetVal = rando_nation()
            except Exception as err:
                print(repr(err))  # DEBUGGING
                self.fail("Raised an exception")
            else:
                self.assertTrue(tmpRetVal in self.dictOfNations.keys())
                randoComboCount[tmpRetVal] += 1

        ### COMPARE RESULTS ###
        for nation in self.dictOfNations.keys():
            randoResults = randoComboCount[nation] / (testFactor * 100)
            tmpDiff = self.dictOfNations[nation] - randoResults
            allowedDev = self.dictOfNations[nation] * .1
            if tmpDiff > allowedDev or tmpDiff < -allowedDev:
                print("\nNation:\t{}".format(nation))
                print("\tReal World:\t{}".format(self.dictOfNations[nation])) 
                print("\tRando Nation:\t{}".format(randoResults))
                print("\tReal Diff:\t{}".format(tmpDiff))
                if tmpDiff < 0:
                    print("\tAllowed Diff:\t{}".format(-allowedDev))
                else:
                    print("\tAllowed Diff:\t{}".format(allowedDev))
            self.assertTrue(tmpDiff < allowedDev and tmpDiff > -allowedDev)

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