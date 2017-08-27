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
        "Red", "Red Orange", \
        "Orange", "Orange Yellow", "Yellow", \
        "Yellow Green", "Green", "Green Blue", \
        "Blue", \
        # "Blue", "Blue Indigo", "Indigo", \
        "Blue Violet", "Violet", "Violet Red", \
        # "Indigo Violet", "Violet", "Violet Red", \
        "Greyscale", \
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
        self.num = number          # Palette selection number
        self.hue = hue          # Hue of the this color
        self.sat = saturation      # Saturation of this color
        self.val = value          # Value of this color
        self.wheelColor = self.determine_wheel_color()    # see: validColors[]
        self.colorType = self.determine_color_type()    # Primary, Secondary, Tertiary
        self.brightness = self.determine_brightness()    # Light, Medium, Dark


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
        # blueIndigoHue = 255
        # indigoHue = 270
        blueVioletHue = 270
        # indigoVioletHue = 285
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
        ############## OLD VISIBLE LIGHT SPECTRUM COLORS ##############
        # elif self.hue >= ((greenBlueHue + blueHue) / 2) and self.hue < ((blueHue + blueIndigoHue) / 2):
        #     retVal = "Blue"
        # elif self.hue >= ((blueHue + blueIndigoHue) / 2) and self.hue < ((blueIndigoHue + indigoHue) / 2):
        #     retVal = "Blue Indigo"
        # elif self.hue >= ((blueIndigoHue + indigoHue) / 2) and self.hue < ((indigoHue + indigoVioletHue) / 2):
        #     retVal = "Indigo"
        # elif self.hue >= ((indigoHue + indigoVioletHue) / 2) and self.hue < ((indigoVioletHue + violetHue) / 2):
        #     retVal = "Indigo Violet"
        # elif self.hue >= ((indigoVioletHue + violetHue) / 2) and self.hue < ((violetHue + violetRedHue) / 2):
        #     retVal = "Violet"
        ############## NEW COLOR WHEEL COLORS ##############
        elif self.hue >= ((greenBlueHue + blueHue) / 2) and self.hue < ((blueHue + blueVioletHue) / 2):
            retVal = "Blue"
        elif self.hue >= ((blueHue + blueVioletHue) / 2) and self.hue < ((blueVioletHue + violetHue) / 2):
            retVal = "Blue Violet"
        elif self.hue >= ((blueVioletHue + violetHue) / 2) and self.hue < ((violetHue + violetRedHue) / 2):
            retVal = "Violet"
        ############## OLD COLOR WHEEL COLORS ##############
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
        "Red", "Red Orange", \
        "Orange", "Orange Yellow", "Yellow", \
        "Yellow Green", "Green", "Green Blue", \
        "Blue", \
        # "Blue", "Blue Indigo", "Indigo", \
        "Blue Violet", "Violet", "Violet Red", \
        # "Indigo Violet", "Violet", "Violet Red", \
        "Greyscale", \
    ]
    validTypes = [ \
        "Primary", "Secondary", "Tertiary", \
    ]
    validSchemes = [ \
        "Monochromatic - Primary", "Monochromatic - Secondary", "Monochromatic - Tertiary", \
        "2 Colors - Analogous", "2 Colors - Complementary", "3 Colors - Triad", \
        "3 Colors - Split Complementary", "3 Colors - Secondary", "Random", \
        "2 Colors - Earthy", "3 Colors - Earthy", "Random Earthy", \
        "Urban", "Goth", "Parallel", \
    ]
    implementedSchemes = [ \
        "Monochromatic - Primary", "Monochromatic - Secondary", "Monochromatic - Tertiary", \
        "2 Colors - Analogous", "2 Colors - Complementary", "3 Colors - Triad", \
        "3 Colors - Split Complementary", "3 Colors - Secondary", "Random", \
        # This line is missing "3 Colors - Earthy"
        "2 Colors - Earthy", "Random Earthy", \
        "Urban", "Goth", \

    ]
    listOfPrimaryColors = [ \
        "Red", "Yellow", "Blue", \
    ]
    listOfSecondaryColors = [ \
        "Orange", "Green", "Violet", \
    ]
    listOfTertiaryColors = [ \
        "Red Orange", "Orange Yellow", "Yellow Green", \
        # "Green Blue", "Blue Indigo", "Indigo", \
        "Green Blue", "Blue Violet", \
        # "Indigo Violet", "Violet Red", \
        "Violet Red", \
    ]
    # Assign colors to this list programtically during __init__()
    listOfBrownColors = []
    # Assign browns and other select colors to this during __init__()
    listOfEarthyColors = []
    # Assign goth colors to this during __init__()
    listOfGothColors = []
    scheme = ""
    # # Store the colors selected under this palette
    # mainColor = Color(0, 0, 0, 0)
    # secondaryColor = Color(0, 0, 0, 0)
    # weaponColor = Color(0, 0, 0, 0)


    def __init__(self, scheme):
        ### INPUT VALIDATION ###
        if not isinstance(scheme, str):
            raise TypeError("Color scheme is not an string")
        elif scheme not in self.validSchemes:
            raise ValueError("Invalid color scheme")
        elif scheme not in self.implementedSchemes:
            raise RuntimeError("The '{}' color scheme has not yet been implemented".format(scheme))

        ### INITIALIZAITON ###
        self.scheme = scheme
        # print("This is the ColorPalette __init__()")  # DEBUGGING


    def count_colors(self, wheelColorToCount):
        '''
            PURPOSE:    Count the frequency of a given color in this palette's list of Colors
            INPUT:      wheelColorToCount - A valid color to count in this color palette
            OUTPUT:      The number of matching colors in this palette
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


    def spin_a_color(self, startingColor, offset, skipGreyscale):
        '''
            PURPOSE:    Spin the wheel of color to find an offset
            INPUT:      
                        startingColor - A valid color as the starting location
                        offset - Positive or negative number to spin the wheel
                        skipGreyscale - type(bool) True, ignore "Greyscale"
            OUTPUT:      A "valid color" from validColors
            NOTE:         If offset is 0, will return a randomized "valid color"
        '''
        ### INPUT VALIDATION ###
        if not isinstance(startingColor, str):
            raise TypeError("Starting color is not a string")
        elif not isinstance(offset, int):
            raise TypeError("Offset is not an integer")
        elif not isinstance(skipGreyscale, bool):
            raise TypeError("Skip Greyscale is not a bool")
        elif startingColor not in self.validColors:
            raise ValueError("Invalid starting color")

        ### LOCAL VARIABLES ###
        retVal = None  # validColor name to return
        numColors = 0  # Number of colors to spin through
        # newOffset = 0  # Modified offset
        currIndex = 0  # Current index of the starting color
        newIndex = 0   # Index of the color that got spun

        ### CALCULATIONS ###
        if skipGreyscale is True:
            numColors = self.validColors.__len__() - 2  # 15 --> 13
        else:
            numColors = self.validColors.__len__() - 1 # 15 --> 14

        if offset != 0:
            currIndex = self.validColors.index(startingColor)  # Get the index of the starting color
            newIndex = (currIndex + offset) % (numColors + 1)
            retVal = self.validColors[newIndex]
        else:
            retVal = self.validColors[randint(0, self.validColors.__len__() - 1)]

        return retVal

    
    # Color(#HSV)
    # Main
    # self.listOfColors.append(Color(2, 32, 45, 26))
    # self.listOfColors.append(Color(49, 25, 68, 22))
    # self.listOfColors.append(Color(50, 24, 63, 13))
    # self.listOfColors.append(Color(51, 26, 57, 16))
    # self.listOfColors.append(Color(52, 24, 53, 18))
    # self.listOfColors.append(Color(53, 22, 42, 22))
    # self.listOfColors.append(Color(54, 20, 31, 26))
    # self.listOfColors.append(Color(55, 19, 21, 31))
    # Secondary
    # self.listOfColors.append(Color(0, 39, 49, 14))
    # self.listOfColors.append(Color(4, 43, 49, 17))
    # self.listOfColors.append(Color(6, 33, 56, 31))
    # self.listOfColors.append(Color(8, 34, 61, 22))
    # self.listOfColors.append(Color(21, 24, 56, 20))
    # self.listOfColors.append(Color(28, 40, 60, 20))
    # self.listOfColors.append(Color(36, 27, 66, 23))
    # self.listOfColors.append(Color(84, 19, 100, 48))
    def is_it_brown(self, someColor):
        ### INPUT VALIDATION ###
        if not isinstance(someColor, Color):
            raise TypeError("Some color is not a Color at all")
            
        ### LOCAL VARIABLES ###
        retVal = False  # Default return value... prove it wrong
        
        ### CHECK COLOR ###
        # 1.1. Brown == Dark Orange
        # https://en.wikipedia.org/wiki/Hue
        if someColor.wheelColor == "Orange" and someColor.wheelColor == "Dark":
            print("Dark Orange")  # DEBUGGING
            print_color_object(someColor)  # DEBUGGING
            retVal = True
        # 1.2. Wingin' It
        elif someColor.wheelColor == "Red Orange" and someColor.wheelColor == "Dark":
            print("Dark Red Orange")  # DEBUGGING
            print_color_object(someColor)  # DEBUGGING
            retVal = True
        # 1.3. Wingin' It
        elif someColor.wheelColor == "Orange Yellow" and someColor.wheelColor == "Dark":
            print("Dark Orange Yellow")  # DEBUGGING
            print_color_object(someColor)  # DEBUGGING
            retVal = True
        # 2. Low saturation in Yellow-Red region
        # http://www.greatreality.com/color/ColorHVC.htm
        ## 2.1. Check Wheel Color against Saturation
        # if someColor.wheelColor in [ "Red", "Red Orange", "Orange", "Orange Yellow", "Yellow" ]:
        #     if someColor.sat > 50:
        #         retVal = True
        ## 2.2. Check Hue against Saturation
        # if someColor.hue >= 0 and someColor.hue <= 40:
        #     if someColor.sat > 33:
        #         retVal = True
        # 3. ???
        # http://www.december.com/html/spec/colorhsl.html        
        # 4. Wingin' It
        if (someColor.hue >= 0 and someColor.hue <= 40) or someColor.hue >= 330:
            if (someColor.sat - (someColor.val * 1)) >= 40:
                retVal = True
                # print_color_object(someColor)  # DEBUGGING
        # 5. Wingin' It
        if (someColor.hue >= 0 and someColor.hue <= 40) or someColor.hue >= 330:
            if someColor.val <= 35:
                retVal = True
        # 6. Wingin' It
        if (someColor.hue >= 0 and someColor.hue <= 55) or someColor.hue >= 330:
            if someColor.val <= 25:
                retVal = True

        # 7. Remove Greyscale colors
        if (someColor.wheelColor == "Greyscale"):
            retVal = False

        return retVal
    

    def get_color(self, colorToMatch = None, secondColorToMatch = None):
        ### INPUT VALIDATION ###
        if not isinstance(colorToMatch, Color) and colorToMatch is not None:
            # print("get_color():\tcolorToMatch is of type {}\n".format(colorToMatch))  # DEBUGGING
            raise TypeError("Color to match is not of type Color or NoneType")
        elif not isinstance(secondColorToMatch, Color) and secondColorToMatch is not None:
            # print("get_color():\tsecondColorToMatch is of type {}\n".format(secondColorToMatch))  # DEBUGGING
            raise TypeError("Second color to match is not of type Color or NoneType")
        elif not colorToMatch and secondColorToMatch:
            raise RuntimeError("Main color is blank but Secondary color is not")
        elif self.scheme not in self.implementedSchemes:
            # print("get_color():\tcolorToMatch is of type {}\n".format(colorToMatch))  # DEBUGGING
            # print("get_color():\tself.scheme is {}\n".format(self.scheme))  # DEBUGGING
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
            retVal = self.get_mono_primary(colorToMatch, secondColorToMatch)
        elif self.scheme == "Monochromatic - Secondary":
            retVal = self.get_mono_secondary(colorToMatch, secondColorToMatch)
        elif self.scheme == "Monochromatic - Tertiary":
            retVal = self.get_mono_tertiary(colorToMatch, secondColorToMatch)
        elif self.scheme == "2 Colors - Analogous":
            retVal = self.get_two_analogous(colorToMatch, secondColorToMatch)
        elif self.scheme == "2 Colors - Complementary":
            retVal = self.get_two_complementary(colorToMatch, secondColorToMatch)
        elif self.scheme == "3 Colors - Triad":
            retVal = self.get_triad_color(colorToMatch, secondColorToMatch)
        elif self.scheme == "3 Colors - Split Complementary":
            retVal = self.get_three_split_complementary(colorToMatch, secondColorToMatch)
        elif self.scheme == "3 Colors - Secondary":
            retVal = self.get_three_secondary(colorToMatch, secondColorToMatch)
        elif self.scheme == "Random":
            retVal = self.get_random_colors(colorToMatch, secondColorToMatch)
        elif self.scheme == "2 Colors - Earthy":
            retVal = self.get_two_earthy_colors(colorToMatch, secondColorToMatch)
        elif self.scheme == "Random Earthy":
            retVal = self.get_random_earthy_colors(colorToMatch, secondColorToMatch)
        elif self.scheme == "Urban":
            retVal = self.get_urban_colors(colorToMatch, secondColorToMatch)
        elif self.scheme == "Goth":
            retVal = self.get_goth_colors(colorToMatch, secondColorToMatch)
        ############# IMPLEMENT MORE COLOR SCHEMES HERE #############
        else:
            raise RuntimeError("get_color:\tHow did we get here?!")

        return retVal


    def get_mono_primary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a primary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class of Type "Primary" that matches colorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a primary wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list to match that wheelColor
        '''
        ### LOCAL VARIABLES ###
        retVal = None              # Function's return value of type Color
        matchThisColor = None      # Primary color to match
        numColors = 0              # Holds of the number of given primary color in the list
        randNum = 0                # Holds a randomized value

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


    def get_mono_secondary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a secondary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class of Type "Secondary" that matches colorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a secondary wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list to match that wheelColor
        '''
        ### LOCAL VARIABLES ###
        retVal = None              # Function's return value of type Color
        matchThisColor = None      # Secondary color to match
        numColors = 0              # Holds of the number of given secondary color in the list
        randNum = 0                # Holds a randomized value

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


    def get_mono_tertiary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a tertiary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class of Type "Tertiary" that matches colorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a tertiary wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list to match that wheelColor
        '''
        ### LOCAL VARIABLES ###
        retVal = None              # Function's return value of type Color
        matchThisColor = None      # Tertiary color to match
        numColors = 0              # Holds of the number of given tertiary color in the list
        randNum = 0                # Holds a randomized value

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


    def get_two_analogous(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get an analogous color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is analogous to colorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list analogous to that wheelColor
        '''
        ### LOCAL VARIABLES ###
        retVal = None              # Function's return value of type Color
        matchThisColor = None      # Color to match
        analogousColor = None    # wheelColor string used to randomize the return value
        numColors = 0              # Holds of the number of given tertiary color in the list
        randNum = 0                # Holds a randomized value
        mainIndex = 0            # validColor index of the mainColor
        secondIndex = 0            # validColor index of the secondaryColor

        # Verify Main and Secondary are analogous to each other
        if colorToMatch is not None and secondColorToMatch is not None:
            mainIndex = self.validColors.index(colorToMatch.wheelColor)
            secondIndex = self.validColors.index(secondColorToMatch.wheelColor)
            if ((mainIndex + 1) != secondIndex and (mainIndex - 1) != secondIndex) and \
            ((mainIndex + secondIndex) != (self.validColors.__len__() - 2)):
                # print("Main Color:\tIndex {}".format(mainIndex))  # DEBUGGING
                # print_color_object(colorToMatch)  # DEBUGGING
                # print("Secondary Color:\tIndex {}".format(secondIndex))  # DEBUGGING
                # print_color_object(secondColorToMatch)  # DEBUGGING
                raise ValueError("Main and Secondary colors are not analogous to each other")

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:  
            matchThisColor = self.validColors[randint(0, self.validColors.__len__() - 1)]
        ## 1.2. Select Weapon
        elif secondColorToMatch is not None:
            randNum = randint(0, 1)
            if randNum == 0:
                matchThisColor = colorToMatch.wheelColor
            else:
                matchThisColor = secondColorToMatch.wheelColor
        ## 1.3. Select Secondary
        else:
            matchThisColor = colorToMatch.wheelColor

        # 2. Determine the color to randomize from
        ## 2.1. Pick a color
        if colorToMatch and secondColorToMatch:
            ### 2.1.a. If this is a Weapon Color, select from existing colors
            analogousColor = matchThisColor
        else:
            ### 2.2.b. If this is not a Weapon Color, find an offset
            #### 2.2.b.i Randomize offset of -1 or 1
            randNum = randint(0, 1)
            if randNum == 0:
                randNum = -1
            #### 2.2.b.ii Determine the color at that offset
            analogousColor = self.spin_a_color(matchThisColor, randNum, True)
            
        # 3. Count the colors in the list
        numColors = self.count_colors(analogousColor)
        if numColors <= 0:
            analogousColor = "Greyscale"
            numColors = self.count_colors(analogousColor)

        # 4. Randomly choose a color
        randNum = randint(1, numColors)

        # 5. Find the randNum'th Color in this palette's list
        for swatch in self.listOfColors:
            if swatch.wheelColor == analogousColor:
                randNum -= 1
                if randNum == 0:
                    retVal = swatch
                    break

        return retVal

    
    def get_two_complementary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a complementary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is complementary to colorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list complementary to that wheelColor
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        matchThisColor = None          # Color to match
        complementaryColor = None    # wheelColor string used to randomize the return value
        numColors = 0                  # Holds of the number of given tertiary color in the list
        randNum = 0                    # Holds a randomized value
        offset = 0                    # Holds the calculated offset for the inevitable spin_a_color() function call

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:  
            matchThisColor = self.validColors[randint(0, self.validColors.__len__() - 1)]
        ## 1.2. Select Weapon
        elif secondColorToMatch is not None:
            randNum = randint(0, 1)
            if randNum == 0:
                matchThisColor = colorToMatch.wheelColor
            else:
                matchThisColor = secondColorToMatch.wheelColor
        ## 1.3. Select Secondary
        else:
            matchThisColor = colorToMatch.wheelColor

        # 2. Determine the color to randomize from
        ## 2.1. Pick a color
        if colorToMatch and secondColorToMatch:
            ### 2.1.a. If this is a Weapon Color, select from existing colors
            complementaryColor = matchThisColor
        else:
            ### 2.2.b. If this is not a Weapon Color, find an offset
            #### 2.2.b.i Randomize offset for complementary color (NOTE: Should be 6)
            if (self.validColors.__len__() - 1) % 2 == 0:  # Even (NOTE: Minus 1 for Greyscale)
                offset = (self.validColors.__len__() - 1) / 2
                # print("Wheel is even at {} colors and offset is {}".format(self.validColors.__len__() - 1, offset))  # DEBUGGING
            else:  # Odd
                randNum = randint(0, 1)
                if randNum == 0:
                    randNum = -1
                offset = (self.validColors.__len__() - 1 + randNum) / 2
                # print("Wheel is odd at {} colors and offset is {}".format(self.validColors.__len__() - 1, offset))  # DEBUGGING
            #### 2.2.b.ii Determine the color at that offset
            complementaryColor = self.spin_a_color(matchThisColor, int(offset), True)

        # 3. Count the colors in the list
        numColors = self.count_colors(complementaryColor)
        if numColors <= 0:
            complementaryColor = "Greyscale"
            numColors = self.count_colors(complementaryColor)

        # 4. Randomly choose a color
        randNum = randint(1, numColors)

        # 5. Find the randNum'th Color in this palette's list
        for swatch in self.listOfColors:
            if swatch.wheelColor == complementaryColor:
                randNum -= 1
                if randNum == 0:
                    retVal = swatch
                    break

        return retVal
    
    
    def get_triad_color(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a complementary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is in a triad color scheme with colorToMatch and secondColorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list complementary to that wheelColor
                        If colorToMatch and secondColorToMatch are both Color objects, will determine
                            the last remaining color in the triad and randomize a color to match
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        matchThisColor = None          # Color to match
        triadColor = None            # wheelColor string used to randomize the return value
        numColors = 0                  # Holds of the number of given tertiary color in the list
        randNum = 0                    # Holds a randomized value
        offset = 0                    # Holds the calculated offset for the inevitable spin_a_color() function call

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:  
            matchThisColor = self.validColors[randint(0, self.validColors.__len__() - 1)]
        ## 1.2. Select Weapon
        elif secondColorToMatch is not None:
            # print("Main Type:\t{}".format(type(colorToMatch)))  # DEBUGGING
            # print("2nd Type:\t{}".format(type(secondColorToMatch)))  # DEBUGGING
            # print("Main Dir:\t{}".format(dir(colorToMatch)))  # DEBUGGING
            # print("2nd Dir:\t{}".format(dir(secondColorToMatch)))  # DEBUGGING
            if self.spin_a_color(colorToMatch.wheelColor, 4, True) != secondColorToMatch.wheelColor and \
            self.spin_a_color(colorToMatch.wheelColor, -4, True) != secondColorToMatch.wheelColor:
                raise ValueError("Main and Secondary colors do not appear to be in a triad")
            elif self.spin_a_color(colorToMatch.wheelColor, 4, True) != secondColorToMatch.wheelColor:
                matchThisColor = self.spin_a_color(colorToMatch.wheelColor, 4, True)
            else:
                matchThisColor = self.spin_a_color(colorToMatch.wheelColor, -4, True)        
        ## 1.3. Select Secondary
        else:
            matchThisColor = colorToMatch.wheelColor

        # 2. Determine the color to randomize from
        ## 2.1. Pick a color
        if colorToMatch and secondColorToMatch:
            ### 2.1.a. If this is a Weapon Color, select from existing colors
            triadColor = matchThisColor
        else:
            ### 2.2.b. If this is not a Weapon Color, find an offset
            #### 2.2.b.i Randomize offset for complementary color (NOTE: Should be 4 or -4)
            if (self.validColors.__len__() - 1) % 3 == 0:  # NOTE: Minus 1 for Greyscale
                offset = (self.validColors.__len__() - 1) / 3
                # print("Wheel is even at {} colors and offset is {}".format(self.validColors.__len__() - 1, offset))  # DEBUGGING
            else:  # Not a multiple of three (?)
                randNum = randint(0, 1)
                if randNum == 0:
                    randNum = -1
                while ((self.validColors.__len__() - 1 + randNum) % 3 != 0):
                    randNum = randNum + randNum
                offset = (self.validColors.__len__() - 1 + randNum) / 3
                # print("Wheel is odd at {} colors and offset is {}".format(self.validColors.__len__() - 1, offset))  # DEBUGGING
            #### 2.2.b.ii Determine the color at that offset
            triadColor = self.spin_a_color(matchThisColor, int(offset), True)

        # 3. Count the colors in the list
        numColors = self.count_colors(triadColor)
        if numColors <= 0:
            triadColor = "Greyscale"
            numColors = self.count_colors(triadColor)

        # 4. Randomly choose a color
        randNum = randint(1, numColors)

        # 5. Find the randNum'th Color in this palette's list
        for swatch in self.listOfColors:
            if swatch.wheelColor == triadColor:
                randNum -= 1
                if randNum == 0:
                    retVal = swatch
                    break

        return retVal
    

    def get_three_split_complementary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a split complementary color from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is split complementary to colorToMatch and secondColorToMatch
            NOTE:
                        If colorToMatch is None, will randomly select a wheelColor and then
                            randomly select a Color from the palette's list to match that wheelColor
                        If colorToMatch is a Color, will determine the Color's wheelColor and randomly
                            select a Color from the palette's list complementary to that wheelColor
                        If colorToMatch and secondColorToMatch are both Color objects, will determine
                            the last remaining color in the triad and randomize a color to match
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        matchThisColor = None          # Color to match
        splitColor = None            # wheelColor string used to randomize the return value
        numColors = 0                  # Holds of the number of given tertiary color in the list
        randNum = 0                    # Holds a randomized value

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:  
            matchThisColor = self.validColors[randint(0, self.validColors.__len__() - 1)]
        ## 1.2. Select Weapon
        elif secondColorToMatch is not None:
            # print("Main Type:\t{}".format(type(colorToMatch)))  # DEBUGGING
            # print("2nd Type:\t{}".format(type(secondColorToMatch)))  # DEBUGGING
            # print("Main Dir:\t{}".format(dir(colorToMatch)))  # DEBUGGING
            # print("2nd Dir:\t{}".format(dir(secondColorToMatch)))  # DEBUGGING
            if self.spin_a_color(colorToMatch.wheelColor, 5, True) != secondColorToMatch.wheelColor and \
            self.spin_a_color(colorToMatch.wheelColor, -5, True) != secondColorToMatch.wheelColor:
                # print_color_object(colorToMatch)  # DEBUGGING
                # print_color_object(secondColorToMatch)  # DEBUGGING
                # print("Main:\t{}".format(self.validColors.index(colorToMatch.wheelColor)))  # DEBUGGING
                # print("2nd:\t{}".format(self.validColors.index(secondColorToMatch.wheelColor)))  # DEBUGGING
                raise ValueError("Main and Secondary colors do not appear to be split complementary")
            elif self.spin_a_color(colorToMatch.wheelColor, 5, True) != secondColorToMatch.wheelColor:
                matchThisColor = self.spin_a_color(colorToMatch.wheelColor, 5, True)
            else:
                matchThisColor = self.spin_a_color(colorToMatch.wheelColor, -5, True)    
        ## 1.3. Select Secondary
        else:
            matchThisColor = colorToMatch.wheelColor

        # 2. Determine the color to randomize from
        ## 2.1. Pick a color
        if colorToMatch and secondColorToMatch:
            ### 2.1.a. If this is a Weapon Color, select from existing colors
            splitColor = matchThisColor
        else:
            ### 2.2.b. Randomize an offset
            randNum = randint(0, 1)
            if randNum == 0:
                randNum = -1
            randNum *= 5
            #### 2.2.c Determine the color at that offset
            splitColor = self.spin_a_color(matchThisColor, int(randNum), True)

        # 3. Count the colors in the list
        numColors = self.count_colors(splitColor)
        if numColors <= 0:
            splitColor = "Greyscale"
            numColors = self.count_colors(splitColor)

        # 4. Randomly choose a color
        randNum = randint(1, numColors)

        # 5. Find the randNum'th Color in this palette's list
        for swatch in self.listOfColors:
            if swatch.wheelColor == splitColor:
                randNum -= 1
                if randNum == 0:
                    retVal = swatch
                    break

        return retVal
    
    
    def get_three_secondary(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get a triad color from the list of Colors in this palette that is also Secondary
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is in a secondary triad color scheme with colorToMatch and secondColorToMatch
            NOTE:
                        This function is actually a wrapper for get_triad_color.
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        matchThisColor = None          # Color to match
        numColors = 0                  # Holds of the number of given tertiary color in the list
        randNum = 0                    # Holds a randomized value
        
        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:
            # 1.1.1. Pick a color
            matchThisColor = self.listOfSecondaryColors[randint(0, self.listOfSecondaryColors.__len__() - 1)]
            # 1.1.2. Count the colors in the list
            numColors = self.count_colors(matchThisColor)
            if numColors <= 0:
                matchThisColor = "Greyscale"
                numColors = self.count_colors(matchThisColor)

            # 1.1.3. Randomly choose a color
            randNum = randint(1, numColors)

            # 1.1.4. Find the randNum'th Color in this palette's list
            for swatch in self.listOfColors:
                if swatch.wheelColor == matchThisColor:
                    randNum -= 1
                    if randNum == 0:
                        retVal = swatch
                        break
        ## 1.2. Select Weapon
        elif secondColorToMatch is not None:
            if colorToMatch.colorType != "Secondary":
                raise ValueError("Main armor color is not a Secondary wheel color")
            elif secondColorToMatch.colorType != "Secondary":
                raise ValueError("Secondary armor color is not a Secondary wheel color")
            else:
                retVal = self.get_triad_color(colorToMatch, secondColorToMatch)
        ## 1.3. Select Secondary
        else:
            if colorToMatch.colorType != "Secondary":
                raise ValueError("Main color is not a Secondary color")
            else:
                retVal = self.get_triad_color(colorToMatch, secondColorToMatch)
            
        return retVal
    
    
    def get_random_colors(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get random colors from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" (ignored)
                        secondColorToMatch - Secondary Armor Color (ignored)
            OUTPUT:        Color class that has been completely randomized regardless of Main and Secondary
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        
        ### GET COLOR ###
        # 1. Randomize color
        retVal = self.listOfColors[randint(0, self.listOfColors.__len__() - 1)]

        return retVal


    def get_two_earthy_colors(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get earthy colors from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is in an earthy color along with colorToMatch and secondColorToMatch
            NOTE:
                        This function is unique, as of yet, because it builds from a sub-list of earthy colors.
                        http://www.creativecolorschemes.com/resources/free-color-schemes/earth-tone-color-scheme.shtml
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        tmpColor = None             # Temporary Color object
        matchThisColor = None          # Color to match
        numColors = 0                  # Holds of the number of given tertiary color in the list
        randNum = 0                    # Holds a randomized value
        maxIterations = 1000        # Maximum number of while loops            

        ### GET COLOR ###
        # Two Color Schemes
        # 1. Brown(dark) → Brown(light)
        # 2. Brown(medium) → Brown(dark)
        # 3. Green(dark) → Yellow
        # 4. Brown(light) → Greyscale(light)... Orange(light) == Brown(light) for this scheme
        # 5. Green(light) → Greyscale(dark)... NOT IMPLEMENTED
        # 6. Brown(light) or Greyscale(light) → Brown(reddish)
        # 7. Green(medium) → Brown(medium)
        # 8. Orange → Green(dark)

        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:
            while randNum not in [ 1, 2, 3, 4, 6, 7, 8 ]:  # List of implemented schemes
                randNum = randint(1,8)  # Random Two Color Earthy scheme
            randNum = 8  # DEBUGGING
            # print("Two Color Earthy Scheme:\t{}".format(randNum))  # DEBUGGING
            while retVal is None:
                # 1.1.1. Randomize an earthy color
                tmpColor = self.listOfEarthyColors[randint(0, self.listOfEarthyColors.__len__() - 1)]
                # 1.1.1.1. Brown(dark) → Brown(light)
                if randNum == 1:
                    if self.is_it_brown(tmpColor):
                        if tmpColor.brightness == "Dark":
                            retVal = tmpColor
                # 1.1.1.2. Brown(medium) → Brown(dark)
                elif randNum == 2:
                    if self.is_it_brown(tmpColor):
                        if tmpColor.brightness == "Medium":
                            retVal = tmpColor
                # 1.1.1.3. Green(dark) → Yellow
                elif randNum == 3:
                    if tmpColor.wheelColor == "Green":
                        if tmpColor.brightness == "Dark":
                            retVal = tmpColor
                # 1.1.1.4. Brown(light) → Greyscale(light)... Orange(light) == Brown(light) for this scheme
                elif randNum == 4:
                    if self.is_it_brown(tmpColor):
                        if tmpColor.brightness == "Light":
                            retVal = tmpColor
                    elif tmpColor.wheelColor.find("Orange") >= 0:
                        if tmpColor.brightness == "Light":
                            retVal = tmpColor
                # 1.1.1.5. Green(light) → Greyscale(dark)
                # NOTE: Not implemented since there are no Light Green colors in 
                #     the Main Armor Color Palette
                # elif randNum == 5:
                #     if tmpColor.wheelColor.find("Green") >= 0:
                #         if tmpColor.brightness == "Light":
                #             retVal = tmpColor
                # 1.1.1.6. Brown(light) or Greyscale(light) → Brown(reddish)
                elif randNum == 6:
                    if self.is_it_brown(tmpColor):
                        if tmpColor.brightness == "Light":
                            retVal = tmpColor
                    elif tmpColor.wheelColor == "Greyscale":
                        if tmpColor.brightness == "Light":
                            retVal = tmpColor
                # 1.1.1.7. Green(medium) → Brown(medium)
                elif randNum == 7:
                    if tmpColor.wheelColor == "Green":
                        if tmpColor.brightness == "Medium":
                            retVal = tmpColor
                # 1.1.1.8. Orange → Green(dark)
                elif randNum == 8:
                    if tmpColor.wheelColor == "Orange" and tmpColor.brightness != "Light" and not self.is_it_brown(tmpColor):
                        retVal = tmpColor
                else:
                    raise RuntimeError("get_two_earthy_colors:\tHow did we get here?")
                # Limit while loop iterations
                if retVal is None:
                    maxIterations -= 1
                    if maxIterations <= 0:
                        raise RuntimeError("get_two_earthy_colors:\tCouldn't find a Main color match for scheme {}".format(randNum))
        ## 1.2. Select Secondary
        elif secondColorToMatch is None:
            while retVal is None:
                # 1.1.1. Randomize an earthy color
                tmpColor = self.listOfEarthyColors[randint(0, self.listOfEarthyColors.__len__() - 1)]
                # 1.1.1.1. Brown(dark) → Brown(light)
                if self.is_it_brown(colorToMatch) and colorToMatch.brightness == "Dark":
                    # print("Two Color Earthy Scheme:\t1")  # DEBUGGING
                    if self.is_it_brown(tmpColor) and tmpColor.brightness != "Dark":
                        retVal = tmpColor
                # 1.1.1.2. Brown(medium) → Brown(dark)
                elif self.is_it_brown(colorToMatch) and colorToMatch.brightness == "Medium":
                    # print("Two Color Earthy Scheme:\t2")  # DEBUGGING
                    if self.is_it_brown(tmpColor) and tmpColor.brightness == "Dark":
                        retVal = tmpColor
                # 1.1.1.3. Green(dark) → Yellow
                elif colorToMatch.wheelColor == "Green" and colorToMatch.brightness == "Dark":
                    # print("Two Color Earthy Scheme:\t3")  # DEBUGGING
                    if tmpColor.wheelColor.find("Yellow") >= 0:
                        retVal = tmpColor
                # 1.1.1.4. Brown(light) → Greyscale(light)... Orange(light) == Brown(light) for this scheme
                elif colorToMatch.wheelColor == "Orange" and colorToMatch.brightness == "Light":
                    # print("Two Color Earthy Scheme:\t4")  # DEBUGGING
                    if tmpColor.wheelColor == "Greyscale" and tmpColor.brightness == "Light":
                        retVal = tmpColor
                # 1.1.1.5. Green(light) → Greyscale(dark)
                # NOTE: Not implemented since there are no Light Green colors in 
                #     the Main Armor Color Palette
                # elif colorToMatch.wheelColor.find("Green") >= 0 and colorToMatch.brightness == "Light":
                #     print("Two Color Earthy Scheme:\t5")  # DEBUGGING
                #     if tmpColor.wheelColor == "Greyscale" and tmpColor.brightness == "Dark":
                #         retVal = tmpColor
                # 1.1.1.6. Brown(light) or Greyscale(light) → Brown(reddish)
                elif (self.is_it_brown(colorToMatch) and colorToMatch.brightness == "Light") or \
                (colorToMatch.wheelColor == "Greyscale" and colorToMatch.brightness == "Light"):
                    # print("Two Color Earthy Scheme:\t6")  # DEBUGGING
                    if self.is_it_brown(tmpColor) and tmpColor.wheelColor.find("Red") >= 0:
                        retVal = tmpColor
                # 1.1.1.7. Green(medium) → Brown(medium)
                elif colorToMatch.wheelColor == "Green" and colorToMatch.brightness == "Medium":
                    # print("Two Color Earthy Scheme:\t7")  # DEBUGGING
                    if self.is_it_brown(tmpColor) and tmpColor.brightness == "Medium":
                        retVal = tmpColor
                # 1.1.1.8. Orange → Green(dark)
                elif colorToMatch.wheelColor == "Orange" and colorToMatch.brightness != "Light" and not self.is_it_brown(colorToMatch):
                    # print("Two Color Earthy Scheme:\t8")  # DEBUGGING
                    if tmpColor.wheelColor.find("Green") >= 0 and tmpColor.brightness != "Light":
                        retVal = tmpColor
                else:
                    raise RuntimeError("get_two_earthy_colors:\tHow did we get here?")
                # Limit while loop iterations
                if retVal is None:
                    maxIterations -= 1
                    if maxIterations <= 0:
                        raise RuntimeError("get_two_earthy_colors:\tCouldn't find a secondary color match for scheme {}".format(randNum))
        ## 1.3. Select Weapon
        else:
            retVal = colorToMatch

        # print("Earthy color randomization took {} iterations\n".format(1000 - maxIterations))  # DEBUGGING
        return retVal


    def get_random_earthy_colors(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get random earthy colors from the list of earthy colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" (ignored)
                        secondColorToMatch - Secondary Armor Color (ignored)
            OUTPUT:        Earthy Color class that has been completely randomized regardless of Main and Secondary
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        
        ### GET COLOR ###
        # 1. Randomize color
        retVal = self.listOfEarthyColors[randint(0, self.listOfEarthyColors.__len__() - 1)]

        return retVal

        
    def get_urban_colors(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get urban colors from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is in an urban color along with colorToMatch and secondColorToMatch
            NOTE:
                        This function is unique, as of yet, because it builds from a pred-defined list of tuple Color.num combos.
                        These pre-defined tuples of Color.num combos are taken from XCOM 2 cityscape screenshots
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        randNum = 0                    # Holds a randomized value
        mainCount = 0                # Counts the number of Main duplicates
        listOfColorCombos = [ \
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

        # mainColors = []
        # for combo in listOfColorCombos:
        #     # print("Main Color:\t{}".format(combo[0]))  # DEBUGGING
        #     mainColors.append(combo[0])

        # for combo in listOfColorCombos:
        #     if mainColors.count(combo[0]) is not 1:
        #         print("Too many {}s".format(combo[0]))  # DEBUGGING

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:
            # 1.1.1. Randomize tuple
            randNum = randint(0, listOfColorCombos.__len__() - 1)

            for swatch in self.listOfColors:
                if swatch.num == listOfColorCombos[randNum][0]:
                    retVal = swatch
                if retVal:
                    break
        ## 1.2. Select Secondary
        elif secondColorToMatch is None:
            for combo in listOfColorCombos:
                if colorToMatch.num == combo[0]:
                    mainCount += 1
            randNum = randint(1, mainCount)

            for combo in listOfColorCombos:
                if colorToMatch.num == combo[0]:
                    randNum -= 1

                    if randNum == 0:
                        for swatch in self.listOfColors:
                            if swatch.num == combo[1]:
                                retVal = swatch
                                break
                if retVal:
                    break
        ## 1.3. Select Weapon
        else:
            for combo in listOfColorCombos:
                if colorToMatch.num == combo[0] and secondColorToMatch.num == combo[1]:
                    for swatch in self.listOfColors:
                        if swatch.num == combo[2]:
                            retVal = swatch
                            break
                if retVal:
                    break

        if not retVal:
            # print("Main:\t{}".format(colorToMatch.num))  # DEBUGGING
            # print("2nd:\t{}".format(secondColorToMatch))  # DEBUGGING
            raise RuntimeError("get_urban_colors:\tCould not match color combo tuple to input")

        return retVal


    def get_goth_colors(self, colorToMatch = None, secondColorToMatch = None):
        '''
            PURPOSE:    Get goth colors from the list of Colors in this palette
            INPUT:        
                        colorToMatch - Main Armor Color of type "Color" to match against
                        secondColorToMatch - Secondary Armor Color, of type "Color", if any
            OUTPUT:        Color class that is in an urban color along with colorToMatch and secondColorToMatch
            NOTE:
                        Black will dominate this color scheme.  If any previous color is not Black, the rest will be
        '''
        ### LOCAL VARIABLES ###
        retVal = None                  # Function's return value of type Color
        randNum = 0                    # Holds a randomized value

        ### GET COLOR ###
        # 1. Determine starting color
        ## 1.1. Select Main
        if colorToMatch is None:
            pass
        ## 1.2. Select Secondary
        elif secondColorToMatch is None:
            pass
        ## 1.3. Select Weapon
        else:
            pass

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
            raise RuntimeError("The '{}' color scheme has not yet been implemented".format(scheme))
        # print("This is the MainArmorPalette __init__()")  # DEBUGGING
        ### INITIALIZAITON ###
        # super().__init__(scheme)
        self.scheme = scheme
        self.listOfColors = []
        self.listOfBrownColors = []
        self.listOfEarthyColors = []
        self.listOfGothColors = []
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

        for swatch in self.listOfColors:
            # Build the list of brown colors
            if self.is_it_brown(swatch):
                self.listOfBrownColors.append(swatch)
            # Build the list of earthy colors
                # Browns are earthy colors as well
                self.listOfEarthyColors.append(swatch)
            elif swatch.num in [ 0, 1, 2, 3, 5, 6, 16, 23, 28, 29, \
                                    30, 31, 32, 33, 34, 49, 50, 51, 52, 53, \
                                    54, 55, 56, 57, 58, 59, 60, 61, 62, 63, \
                                    64, 65, 71, 75, 78, 80, 81, 97 ]:
                self.listOfEarthyColors.append(swatch)
            elif swatch.wheelColor == "Orange":
                if swatch.brightness == "Medium" or swatch.brightness == "Dark":
                    self.listOfEarthyColors.append(swatch)
                elif swatch.brightness == "Light":
                    self.listOfEarthyColors.append(swatch)
                    # print("This is being added as 'light brown'")  # DEBUGGING
                    # print_color_object(swatch)
            elif swatch.wheelColor.find("Green") >= 0 and swatch.brightness == "Light":
                self.listOfEarthyColors.append(swatch)
                # print("This is being added as 'light green'")  # DEBUGGING
                # print_color_object(swatch)
            elif swatch.wheelColor == "Green" and swatch.brightness == "Medium":
                self.listOfEarthyColors.append(swatch)
                # print("This is being added as 'medium green'")  # DEBUGGING
                # print_color_object(swatch)
            elif swatch.wheelColor == "Greyscale" and swatch.brightness == "Light":
                self.listOfEarthyColors.append(swatch)
            # Build the list of goth colors
            if swatch.wheelColor == "Greyscale" and swatch.brightness == "Dark":
                self.listOfGothColors.append(swatch)
                # print("This is being added as 'Goth'")  # DEBUGGING
                # print_color_object(swatch)
            elif swatch.num in [ 94, 95 ]:  # These Colors register as Dark Green Blue
                self.listOfGothColors.append(swatch)
                # print("This is being manually added as 'Goth'")  # DEBUGGING
                # print_color_object(swatch)

        # print("Earth Tones:\t\n")
        # for swatch in self.listOfEarthyColors:
        #     print_color_object(swatch)


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
        self.listOfBrownColors = []
        self.listOfEarthyColors = []
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

        for swatch in self.listOfColors:
            if self.is_it_brown(swatch):
                self.listOfBrownColors.append(swatch)
                # Browns are earthy colors as well
                self.listOfEarthyColors.append(swatch)
            # The first 70 Secondary Armor colors count as earth tones
            elif swatch.num in [ x for x in range(0, 70) ]:  # Does not include 70
                self.listOfEarthyColors.append(swatch)
            # There are more than just 70 earth tones in the Secondary Armor color palette
            elif swatch.num in [ 71, 72, 79, 80, 81, 84, 87, 92, 93, 97 ]:
                self.listOfEarthyColors.append(swatch)
            elif swatch.wheelColor == "Greyscale" and swatch.brightness == "Light":
                self.listOfEarthyColors.append(swatch)
            # Build the list of goth colors
            if swatch.wheelColor == "Greyscale" and swatch.brightness == "Dark":
                self.listOfGothColors.append(swatch)
                # print("This is being added as 'Goth'")  # DEBUGGING
                # print_color_object(swatch)
            elif swatch.num in [ 91, 92, 97 ]:  # These Colors register as Dark Green Blue
                self.listOfGothColors.append(swatch)
                # print("This is being manually added as 'Goth'")  # DEBUGGING
                # print_color_object(swatch)

        # print("Earth Tones:\t\n")
        # for swatch in self.listOfEarthyColors:
        #     print_color_object(swatch)


# class WeaponColorPalette(ColorPalette):
class WeaponColorPalette(MainArmorPalette):
    'This class can randomly choose weapon colors from a collection based on established color schemes'
    # pass

    def __init__(self, scheme):
        super().__init__(scheme)

