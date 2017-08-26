from copy import deepcopy
from Harklepalette import Color
from Harklepalette import MainArmorPalette
from Harklepalette import print_color_object
from Harklepalette import SecondaryArmorPalette
from Harklepalette import WeaponColorPalette
from random import randint
# import Harklepalette
import os

'''
Face:
Hair:
Facial Hair:
Hair Color:
Eye Color:
Race:
    0 - Caucasian
    1 - Afican
    2 - Asian
    3 - Hispanic
Skin Color:
Main Armor Color:
Secondary Armor Color:
Weapon Color:
Voice:
Attitude:
'''


######################################################
######################################################
#################### GLOBAL LISTS ####################
######################################################
######################################################


listOfNations = [ \
    "Argentina", "Australia", "Belgium", "Brazil", "Canada", "China", \
    "Egypt", "France", "Germany", "Greece", "India", "Ireland", "Israel", \
    "Italy", "Japan", "Mexico", "Netherlands", "Nigeria", "Norway", \
    "Poland", "Russia", "Saudi Arabia", "Scotland", "South Africa", \
    "South Korea", "Spain", "Sweden", "Ukraine", "United Kingdom", "USA", \
]

listOfGenders = [ "Male", "Female" ]

listOfColorSchemes = [ \
        "Monochromatic - Primary", "Monochromatic - Secondary", "Monochromatic - Tertiary", \
        "2 Colors - Analogous", "2 Colors - Complementary", "3 Colors - Triad", \
        "3 Colors - Split Complementary", "3 Colors - Secondary", "Random", \
        "2 Colors - Earthy", "3 Colors - Earthy", "Random Earthy", \
        "Urban", "Emo", "Parallel", \
]

listOfHelmetHats = [ \
    "None", "Ballcap", "Backwards Ballcap", \
    "Bandana", "Headband", "Boonie Hat", \
    "Beanie", "Dress Hat", "Recon Hood", \
    "Shemagh Scarf", "Delta 1", "Delta 2", \
    "Delta 3", "Delta 4", "Plated 1", \
    "Plated 2", "Plated 3", "Plated 4", \
    "Hockey Mask", "Powered 1", "Powered 2", \
    "Powered 3", "Powered 4", "Kaiser Helmet", \
    "Gas Mask", "Metal Skull", "Metal Skulls with Horns", \
    "Metal Skulls with Mohawk", "Welder's Mask", "Space Helmet", \
    "Space Helmet with Feather Mohawk", "Space Mask", "Knight Helm A", \
    "Knight Helm B", "Voodoo Top Hat A", "Voodoo Top Hat B", \
    "Tintable Skull Paint Hockey Mask", "Skull Paint Hockey Mask", "Tintable Hockey Mask", \
    "Goggles on Eyes", "Goggles on Forehead", "Spider Mask", \
    "Muzzle with Glowing Visor", "Muzzle with Goggles on Eyes", "Muzzle with Goggles on Forehead", \
    "Muzzle", "Aviator Helmet", "Aviator Helmet with Goggles on Eyes", \
    "Aviator Helmet with Goggles on Forehead", "Android", "ADVENT Captain", \
    "ADVENT StunLancer", "ADVENT ShieldBearer", "ADVENT Trooper", \
    "Avatar", "Andromedon", "Floppy Bonnie", \
    "Long Hood", "Ski Mask", \
]

listOfArmorStyles = [ \
    "Base", "Anarchy", "Chaotic", \
    "ADVENT", "Alien", \
]

listOfArmorArms = [ \
    "Arms 0", "Arms 1", "Arms 2", \
    "Arms 3", "Arms 4", "Arms 5", \
    "Arms 6", "Arms 7", "Arms 8", \
    "Arms 9", "Arms 10", "Arms 11", \
]

listOfArmorLegs = [ \
    "Legs 0", "Legs 1", "Legs 2", \
    "Legs 3", "Legs 4", "Legs 5", \
    "Legs 6", "Legs 7", \
]

listOfArmorTorso = [ \
    "Torso 0", "Torso 1", "Torso 2", \
    "Torso 3", "Torso 4", "Torso 5", \
    "Torso 6", "Torso 7", \
]

listOfUpperFaceProps = [
    "None", "Aviators", "Sports Sunglasses", \
    "Dark Sunglasses", "Hippie Sunglasses", "Half-framed Glasses", \
    "Thick-rimmed Glasses", "Hippie Glasses", "Monocle", \
    "Eyepatch", "Eyebrow Ring", "Earring", \
    "Lip Ring", "Nose Ring", "Nose Stud", \
]

listOfLowerFaceProps = [ \
    "None", "Cigarette", "Cigar", \
    "XCOM Bandana", "Skull Bandana", "Biker Bandana", \
    "Striped Bandana", "Samurai Mask A", "Samurai Mask B", \
    "Muton Mask", \
]

listOfPatterns = [ \
    "None", "Digital", "Classic", \
    "Alien", "Tundra", "Hex", \
    "Arid", "Blots", "Classic 2", \
    "Happy", "Zebra", "Plaid", \
    "Tiger", "Hearts", "Dots", \
    "Stripes", "Wild", "Shemagh", \
    "Alien Structure", "Viper Armor", "Alien Cell", \
    "Muton Armor", "Snake Skin", \
]

listOfFacePaint = [ \
    "None", "Ethereal Divide", "Blood Splatter", \
    "Warrior Skull", "Celtic Warrior", "Killer Clown", \
    "Heavy Metal", "Bandit", "Kabuki Paint", \
    "Midnight Warrior", "Archon", "Beserker", \
    "Cryssalid", "Faceless", "GateKeeper", \
    "Muton", "Maori A", "Maori B", \
    "Maori C", "Maori D", "Arid", \
    "Eye Black", "Sharpshooter", "Skull", \
]

listOfTattoos = [ \
    "None", "Chryssalid Killer", "Berserker Hunter", \
    "Snake Wrap", "Sliced Sectoid", "XCOM Sleeve", \
    "Electric Alien", "Bar Code", "Death Sleeve", \
    "Earth Sleeve", "Ace in the Hole", "Shadow Wolf", \
    "Shen", \
]

listOfFaces = [ \
    "Face A", "Face B", "Face C", \
    "Face D", "Face E", "Face F", \
]

listOfHairStyles = [ \
    "Bald", "Long Curls", "Long Layers", \
    "Brushed Up Short", "Short", "Simple Short", \
    "Slicked-back Ponytail", "Loose Ponytail Thick", "Loose Ponytail", \
    "Slicked-back Braid", "Loose Braid", "Man Bun", \
    "Buzzcut Fade", "Buzzcut", "Short Curly", \
    "Flat Top", "Receding Hair Medium", "Receding Hair Short", \
    "Parted", "Afro", "Dreadlocks", \
    "Dreads Ponytail", "Cornrows", "Wild Dreadlocks", \
    "Wild Dreads Ponytail", "Spiky Mohawk", "Mohawk", \
    "Viking", "Blowout", "Top Knot Fade", \
    "Top Knot", "Tall Mohawk", "Tall Mohawk Fade", \
    "Short Mohawk Striped", "Short Mohawk", "Top Braid", \
    "Spikes", "Pigtails", "Pigtails Fade", \
    "Avatar", \
]

listOfFacialHair = [ \
    "None", "Goatee", "Chin Curatin", \
    "Goatee and Moustache", "Thick Beard", "Horseshoe Moustache", \
    "Moustache", "Mutton Chops", "Sideburns", \
    "Mutton Chops and 'Stache", "Short Sideburns", "Scruffy Beard", \
    "Sideburns and Goatee", "Five o'clock Shadow", "Stubble Goatee", \
    "Short Horseshoe Moustache", "Short Moustache", "Stubble Mutton Chops", \
    "Stubble Sideburns", "Scrappy Beard", \
]

listOfRaces = [ \
    "0 - Caucasian", "1 - Afican", "2 - Asian", \
    "3 - Hispanic", \
]


######################################################
######################################################
################## HELPER FUNCTIONS ##################
######################################################
######################################################


################################
### GENERIC HELPER FUNCTIONS ###
################################


# def print_color_object(colorToPrint):
#     ### INPUT VALIDATION ###
#     if not isinstance(colorToPrint, Color):
#         raise TypeError("Color to print is not a Color object")

#     print("Color Num:\t{}".format(colorToPrint.num))
#     print("Color Hue:\t{}".format(colorToPrint.hue))
#     print("Color Sat:\t{}".format(colorToPrint.sat))
#     print("Color Val:\t{}".format(colorToPrint.val))
#     print("Color Type:\t{}".format(colorToPrint.colorType))
#     print("Brightness:\t{}".format(colorToPrint.brightness))
#     print("Wheel Color:\t{}\n".format(colorToPrint.wheelColor))

#     return


def convert_num_to_word(number, capitalize = False):
    ### INPUT VALIDATION ###
    if not isinstance(number, int):
        raise TypeError("number is not an integer")
    elif not isinstance(capitalize, bool):
        raise TypeError("capitalize is not a bool")

    ### LOCAL VARIABLES ###
    retVal = ""

    ### CONVERSION ###
    if number > 9 or number < 0:
        retVal = str(number)
    elif number == 0:
        retVal = "None"
    elif number == 1:
        retVal = "One"
    elif number == 2:
        retVal = "Two"
    elif number == 3:
        retVal = "Three"
    elif number == 4:
        retVal = "Four"
    elif number == 5:
        retVal = "Five"
    elif number == 6:
        retVal = "Six"
    elif number == 7:
        retVal = "Seven"
    elif number == 8:
        retVal = "Eight"
    elif number == 9:
        retVal = "Nine"
    else:
        # How did we get here?!
        raise ValueError("number '{}' is invalid".format(number))

    if capitalize is False:
        retVal = retVal.lower()

    return retVal


################################
### CHARACTER INFO FUNCTIONS ###
################################


def rando_backstory(name, nationality, gender):
    ### INPUT VALIDATION ###
    if not isinstance(name, str):
        raise TypeError('name is not a string')
    elif not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    if not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = "\n\t\t" + name
    numSiblings = randint(0, 4)
    numLivingSibs = randint(0, numSiblings)
    numLivingParents = randint(0, 2)
    firstName = ""
    lastName = ""
    motherName = ""
    fatherName = ""
    homeTown = ""
    motivation = ""

    ### PARSE NAME ###
    nameList = name.split(" ")
    # First name
    if nameList.__len__() > 0:
        firstName = nameList[0]
    else:
        firstName = ""
    # Last name
    if nameList.__len__() > 2:
        for name in nameList:
            lastName = lastName + name
    elif nameList.__len__() == 2:
        lastName = nameList[1]
    else:
        lastName = ""

    ### BUILD BACKSTORY ###
    # Parents
    fatherName = rando_first_name(nationality, "Male")
    if numLivingParents == 1:
        fatherName = fatherName + " (deceased)"
    motherName = rando_first_name(nationality, "Female")
    if numLivingParents == 0:
        motherName = motherName + " (deceased)"
    retVal = retVal + " was born to " + fatherName + " and " + motherName + " "
    ## Chance for child to have different last name
    if randint(1, 10) == 1:
        retVal = retVal + rando_last_name(nationality)
        if randint(1, 2) == 1:
            retVal = retVal.replace("born to", "adopted by")
        else:
            retVal = retVal.replace("born to", "raised by")
    else:
        retVal = retVal + lastName
    # Hometown
    homeTown = rando_city_state(nationality)
    if homeTown.__len__() > 0:
        retVal = retVal + " in " + homeTown
    retVal = retVal + ".\n\t\t"
    # Siblings
    if numSiblings > 0:
        retVal = retVal + firstName + " grew up with " + convert_num_to_word(numSiblings) 
        if numSiblings == 1:
            retVal = retVal + " sibling"
        else:
            retVal = retVal + " siblings"
        if numLivingSibs != numSiblings:
            if numLivingSibs == 0 and numSiblings == 1:
                retVal = retVal + " (deceased)."
            elif numLivingSibs == 1:
                retVal = retVal + ", " + convert_num_to_word(numLivingSibs) + " of which is still living."
            else:
                retVal = retVal + ", " + convert_num_to_word(numLivingSibs) + " of which are still living."
        else:
            retVal = retVal + "."
        retVal = retVal + "\n\t\t"
    # Job
    retVal = retVal + "As an adult, " + firstName + " was a "
    retVal = retVal + rando_occupation()
    if randint(1, 10) > 4:
        retVal = retVal + " in " + rando_city_state(nationality) + "."
    else:
        retVal = retVal + "."
    retVal = retVal + "\n\t\t"
    # Motivation
    retVal = retVal + rando_motivation(firstName, gender)

    return retVal


def rando_motivation(firstName, gender):
    ### INPUT VALIDATION ###
    if not isinstance(firstName, str):
        raise TypeError('firstName is not a string')
    elif not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""
    listOfMotivations = []
    motivationFile = os.path.join("Lists", "02-Biography_Motivation.txt")

    ### READ MOTIVATIONS ###
    if os.path.isfile(motivationFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(motivationFile, "r") as motiveFile:    
        [listOfMotivations.append(motive) for motive in motiveFile.read().split('\n') if motive.__len__() > 0]

    ### RANDOMIZE A MOTIVATION ###
    retVal = retVal + listOfMotivations[randint(0, listOfMotivations.__len__() - 1)]

    ### REPLACE ALL PLACEHOLDERS ###
    # Replace Name
    retVal = retVal.replace("<name>", firstName)
    # Replace <his/her>
    if gender == "Male":
        retVal = retVal.replace("<his/her>", "his")
    else:
        retVal = retVal.replace("<his/her>", "her")
    # Replace <he/she>
    if gender == "Male":
        retVal = retVal.replace("<he/she>", "he")
    else:
        retVal = retVal.replace("<he/she>", "she")
    # Replace <him/her>
    if gender == "Male":
        retVal = retVal.replace("<him/her>", "him")
    else:
        retVal = retVal.replace("<him/her>", "her")
    # Add newlines and tabs
    retVal = retVal.replace(".  ", ".\n\t\t    ")

    return retVal


def rando_city_state(nationality):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')

    ### LOCAL VARIABLES ###
    retVal = ""
    listOfCityStates = []
    cityStateFile = os.path.join("Lists", "02-Biography_City_State_" + nationality + ".txt")

    ### READ LAST NAME ###
    if os.path.isfile(cityStateFile) is False:
        cityStateFile = cityStateFile.replace(nationality, "USA")
    if os.path.isfile(cityStateFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(cityStateFile, "r") as townFile:    
        [listOfCityStates.append(town) for town in townFile.read().split('\n') if town.__len__() > 0]

    ### RANDOMIZE A NAME ###
    retVal = retVal + listOfCityStates[randint(0, listOfCityStates.__len__() - 1)]

    return retVal


def rando_occupation():
    ### LOCAL VARIABLES ###
    retVal = ""
    listOfOccupations = []
    occupationFile = os.path.join("Lists", "02-Biography_Occupation.txt")

    ### READ LAST NAME ###
    if os.path.isfile(occupationFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(occupationFile, "r") as occFile:    
        [listOfOccupations.append(job) for job in occFile.read().split('\n') if job.__len__() > 0]

    ### RANDOMIZE A NAME ###
    retVal = retVal + listOfOccupations[randint(0, listOfOccupations.__len__() - 1)]

    return retVal


def rando_first_name(nationality, gender):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""
    listOfFirstNames = []
    firstNameFile = os.path.join("Lists", "01-Name_First_" + gender + "_" + nationality + ".txt")

    ### READ FIRST NAME ###
    if os.path.isfile(firstNameFile) is False:
        firstNameFile = firstNameFile.replace(nationality, "USA")
    if os.path.isfile(firstNameFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(firstNameFile, "r") as fnFile:    
        [listOfFirstNames.append(name) for name in fnFile.read().split('\n') if name.__len__() > 0]

    ### RANDOMIZE A NAME ###
    retVal = listOfFirstNames[randint(0, listOfFirstNames.__len__() - 1)]

    return retVal


def rando_last_name(nationality):
# def rando_last_name(nationality, gender):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    # elif not isinstance(gender, str):
    #     raise TypeError('gender is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    # elif gender not in listOfGenders:
    #     raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""
    listOfLastNames = []
    lastNameFile = os.path.join("Lists", "01-Name_Last_" + nationality + ".txt")

    ### READ LAST NAME ###
    if os.path.isfile(lastNameFile) is False:
        lastNameFile = lastNameFile.replace(nationality, "USA")
    if os.path.isfile(lastNameFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(lastNameFile, "r") as fnFile:    
        [listOfLastNames.append(name) for name in fnFile.read().split('\n') if name.__len__() > 0]

    ### RANDOMIZE A NAME ###
    retVal = retVal + listOfLastNames[randint(0, listOfLastNames.__len__() - 1)]

    return retVal


def rando_name(nationality, gender):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""

    ### GET FIRST NAME ###
    retVal = rando_first_name(nationality, gender)

    ### GET LAST NAME ###
    if retVal.__len__() > 0:
        retVal = retVal + " " + rando_last_name(nationality)

    return retVal


######################
### PROP FUNCTIONS ###
######################


def rando_helmet_hat(armorStyle):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')
    ### LOCAL VARIABLES ###
    retVal = ""
    helmetStylizedList = []
    startSlice = ""
    stopSlice = ""
    # print("List of Helmets/Hats:\t{}".format(listOfHelmetHats))  # DEBUGGING
    ### TRUNCATE EXISTING LIST ###
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        startSlice = "None"
        stopSlice = "Powered 4"
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        startSlice = "Kaiser Helmet"
        stopSlice = "Android"
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        startSlice = listOfHelmetHats[0]
        stopSlice = listOfHelmetHats[listOfHelmetHats.__len__() - 1]
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        startSlice = "ADVENT Captain"
        stopSlice = "ADVENT Trooper"
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        startSlice = "Avatar"
        stopSlice = "Andromedon"
    else:
        raise ValueError('This armor style has not yet been implemented')
    # print("List of Helmets/Hats:\t{}".format(listOfHelmetHats))  # DEBUGGING
    # print("Helmet Stylized List:\t{}".format(helmetStylizedList))  # DEBUGGING
    helmetStylizedList = listOfHelmetHats[listOfHelmetHats.index(startSlice):\
        listOfHelmetHats.index(stopSlice) + 1]
    # print("Helmet Stylized List:\t{}".format(helmetStylizedList))  # DEBUGGING
    helmetStylizedList.append("None")
    # print("Helmet Stylized List:\t{}".format(helmetStylizedList))  # DEBUGGING

    retVal = helmetStylizedList[randint(0, helmetStylizedList.__len__() - 1)]
    # print("Helmet Return Value:\t{}".format(retVal))  # DEBUGGING

    return retVal


def rando_armor():
    '''
        PURPOSE:    Choose a set of styles for the character's armor
        INPUT:      None
        OUTPUT:     A tuple of strings ("<Arms>", "<Legs>", "<Torso>", "<Style>")
        NOTE:       Styles include: "Base", "Anarchy", "Chaotic"
    '''
    ### LOCAL VARIABLES ###
    armorStyle = ""
    tmpInt = 0
    retArm = ""
    retLeg = ""
    retTorso = ""

    ### CHOOSE STYLE ###
    tmpInt = randint(1, 13)             # 1 - 13
    if tmpInt <= 5:                     # 1 - 5
        armorStyle = listOfArmorStyles[0]     # "Base"
    elif tmpInt <= 10:                  # 6 - 10
        armorStyle = listOfArmorStyles[1]    # "Anarchy"
    elif tmpInt <= 11:                  # 11
        armorStyle = listOfArmorStyles[2]    # "Chaotic"
    elif tmpInt <= 12:                  # 12
        armorStyle = listOfArmorStyles[3]    # "ADVENT"
    else:                               # 13
        armorStyle = listOfArmorStyles[4]    # "Alien"

    ### RANDOMIZE ARM ###
    if armorStyle in [ "Base", "ADVENT", "Alien" ]:
        tmpInt = randint(0, 6)
    elif armorStyle == "Anarchy":
        tmpInt = randint(7, 11)
    elif armorStyle == "Chaotic":
        tmpInt = randint(0, 11)
    else:
        raise ValueError('This armor style has not yet been implemented')
    retArm = listOfArmorArms[tmpInt]

    ### RANDOMIZE LEG ###
    if armorStyle in [ "Base", "ADVENT", "Alien" ]:
        tmpInt = randint(0, 4)
    elif armorStyle == "Anarchy":
        tmpInt = randint(5, 7)
    elif armorStyle == "Chaotic":
        tmpInt = randint(0, 7)
    else:
        raise ValueError('This armor style has not yet been implemented')
    retLeg = listOfArmorLegs[tmpInt]

    ### RANDOMIZE TORSO ###
    if armorStyle in [ "Base", "ADVENT", "Alien" ]:
        tmpInt = randint(0, 4)
    elif armorStyle == "Anarchy":
        tmpInt = randint(5, 7)
    elif armorStyle == "Chaotic":
        tmpInt = randint(0, 7)
    else:
        raise ValueError('This armor style has not yet been implemented')
    retTorso = listOfArmorTorso[tmpInt]

    return tuple((retArm, retLeg, retTorso, armorStyle))


def rando_upper_face(gender):
    ### INPUT VALIDATION ###
    if not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""
    tmpInt = 0
    lastIndex = listOfUpperFaceProps.__len__() - 1

    ### RANDOMIZE UPPER FACE PROP ###
    if gender == "Male":
        # Decrease chance of 10 - 14 selection for men
        tmpInt = randint(0, lastIndex + 10)  # 0 - 24
        if tmpInt > lastIndex:  # If it's 15 - 24...
            tmpInt = tmpInt - (lastIndex + 1)  # ...Sub 15 to get 0 - 9
    else:
        tmpInt = randint(0, lastIndex)  # 0 - 14
    retVal = listOfUpperFaceProps[tmpInt]

    return retVal


def rando_lower_face(nationality):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')

    ### LOCAL VARIABLES ###
    retVal = ""
    tmpInt = 0
    lastIndex = listOfLowerFaceProps.__len__() - 1
    smokeWeight = 0  # Increased likelihood of choosing a cigarrette
    cigarWeight = 0  # Increased likelihood of choosing a cigar

    ### DETERMINE WEIGHTS ###
    # Smoke Weight
    if nationality == "Russia":
        smokeWeight = 3
    elif nationality in [ "Belgium", "China", "Greece", "South Korea", "Ukraine", "Japan", "Germany", "Italy" ]:
        smokeWeight = 2
    else:
        smokeWeight = 0
    # Cigar Weight
    if nationality == "Mexico":
        cigarWeight = 3
    elif nationality == "Brazil":
        cigarWeight = 2
    elif nationality == "USA":
        cigarWeight = 1

    ### RANDOMIZE LOWER FACE PROP ###
    tmpInt = randint(0, lastIndex + smokeWeight + cigarWeight)

    if tmpInt <= lastIndex:
        retVal = listOfLowerFaceProps[tmpInt]
    elif tmpInt <= (lastIndex + smokeWeight):
        retVal = "Cigarette"
    else:
        retVal = "Cigar"

    return retVal


def rando_armor_pattern(armorStyle):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')

    ### LOCAL VARIABLES ###
    retVal = ""
    startSlice = ""
    stopSlice = ""
    patternStylizedList = []

    ### TRUNCATE EXISTING LIST ###
    if armorStyle == listOfArmorStyles[0]:   # "Base"
        startSlice = "None"
        stopSlice = "Shemagh"
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        startSlice = "None"
        stopSlice = "Shemagh"
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        startSlice = listOfPatterns[0]
        stopSlice = listOfPatterns[listOfPatterns.__len__() - 1]
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        return "None"
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        startSlice = "Alien Structure"
        stopSlice = "Snake Skin"
    else:
        raise ValueError('This armor style has not yet been implemented')
    # print("Pattern Stylized List:\t{}".format(patternStylizedList))  # DEBUGGING
    patternStylizedList = listOfPatterns
    # print("Pattern Stylized List:\t{}".format(patternStylizedList))  # DEBUGGING
    # print("Start:\t{}\nStop:\t{}\n".format(startSlice, stopSlice))  # DEBUGGING
    patternStylizedList = listOfPatterns[listOfPatterns.index(startSlice):listOfPatterns.index(stopSlice) + 1]
    # print("Pattern Stylized List:\t{}".format(patternStylizedList))  # DEBUGGING
    patternStylizedList.append("None")
    # print("Pattern Stylized List:\t{}".format(patternStylizedList))  # DEBUGGING

    retVal = patternStylizedList[randint(0, patternStylizedList.__len__() - 1)]
    # print("Pattern Return Value:\t{}".format(retVal))  # DEBUGGING

    return retVal


def rando_weapon_pattern(armorStyle, armorPattern):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')
    elif not isinstance(armorPattern, str):
        raise TypeError('armorPattern is not a string')
    elif armorPattern not in listOfPatterns:
        raise ValueError('Invalid armorPattern')

    ### LOCAL VARIABLES ###
    retVal = ""
    startSlice = ""
    stopSlice = ""
    tmpInt = randint(1, 100)
    weaponPatternStylizedList = []

    ### TRUNCATE EXISTING LIST ###
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        if tmpInt > 60:
            startSlice = "None"
            stopSlice = "Shemagh"
        elif tmpInt > 80:
            return armorPattern
        else:
            return "None"
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        if tmpInt > 25:
            startSlice = "None"
            stopSlice = "Shemagh"
        elif tmpInt > 75:
            startSlice = listOfPatterns[0]
            stopSlice = listOfPatterns[listOfPatterns.__len__() - 1]
        else:
            return armorPattern
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        startSlice = listOfPatterns[0]
        stopSlice = listOfPatterns[listOfPatterns.__len__() - 1]
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        return "None"
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        if tmpInt > 50:
            startSlice = "Alien Structure"
            stopSlice = "Snake Skin"
        else:
            return "None"
    else:
        raise ValueError('This armor style has not yet been implemented')

    weaponPatternStylizedList = listOfPatterns[listOfPatterns.index(startSlice):listOfPatterns.index(stopSlice) + 1]
    weaponPatternStylizedList.append("None")

    retVal = weaponPatternStylizedList[randint(0, weaponPatternStylizedList.__len__() - 1)]

    return retVal


def rando_face_paint(armorStyle):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')

    ### LOCAL VARIABLES ###
    retVal = ""
    startSlice = ""
    stopSlice = ""
    tmpInt = randint(1, 100)
    facePaintStylizedList = []

    ### TRUNCATE EXISTING LIST ###
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        if tmpInt > 50:
            startSlice = "Arid"
            stopSlice = "Skull"
        else:
            return "None"
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        if tmpInt > 66:
            startSlice = "Ethereal Divice"
            stopSlice = "Midnight Warrior"
        if tmpInt > 33:
            startSlice = "Maori A"
            stopSlice = "Maori D"
        else:
            startSlice = listOfFacePaint[0]
            stopSlice = listOfFacePaint[listOfFacePaint.__len__() - 1]
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        startSlice = listOfFacePaint[0]
        stopSlice = listOfFacePaint[listOfFacePaint.__len__() - 1]
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        return "None"
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        startSlice = "Archon"
        stopSlice = "Muton"
    else:
        raise ValueError('This armor style has not yet been implemented')

    facePaintStylizedList = listOfFacePaint[listOfFacePaint.index(startSlice):listOfFacePaint.index(stopSlice) + 1]
    facePaintStylizedList.append("None")

    retVal = facePaintStylizedList[randint(0, facePaintStylizedList.__len__() - 1)]

    return retVal


def rando_tattoos(armorStyle):
    '''
        INPUT:      Style of armor (see: listOfArmorStyles)
        OUTPUT:     A tuple of strings ("<Left Tattoo>", "<Right Tattoo>", "<Tattoo Color>")
        NOTE:       Current tattoo color is hard-coded to black until color wheel functionality is implemented    
    '''
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')

    ### LOCAL VARIABLES ###
    startSlice = listOfTattoos[0]
    stopSlice = listOfTattoos[listOfTattoos.__len__() - 1]
    retVal = tuple(("None", "None", None))  # No tattoo default
    tmpInt = randint(1, 100)
    numTattoos = 0
    leftTattoo = "None"
    rightTattoo = "None"
    tattooColor = None
    dupeTattoo = False
    tattooStylizedList = []

    ### TRUNCATE EXISTING LIST ###
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        if tmpInt > 90:
            numTattoos = 2
            dupeTattoo = True
        elif tmpInt > 75:
            numTattoos = 2
        elif tmpInt > 40:
            numTattoos = 1
        else:
            return retVal
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        if tmpInt > 95:
            numTattoos = 2
            dupeTattoo = True
        elif tmpInt > 65:
            numTattoos = 2
        elif tmpInt > 30:
            numTattoos = 1
        else:
            return retVal
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        numTattoos = randint(0, 2)
        if numTattoos == 2:
            if randint(0, 1) == 1:
                dupeTattoo = True
        elif numTattoos == 0:
            return retVal
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        return retVal
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        if tmpInt > 50:
            numTattoos = 1
            startSlice = "Chryssalid Killer"
            stopSlice = "Electric Alien"
        if tmpInt > 75:
            numTattoos = 2
        if tmpInt > 90:
            dupeTattoo = True
        else:
            return retVal
    else:
        raise ValueError('This armor style has not yet been implemented')

    tattooStylizedList = listOfTattoos[listOfTattoos.index(startSlice):listOfTattoos.index(stopSlice) + 1]

    ### RANDOMIZE TATTOOS ###
    if numTattoos == 2:
        leftTattoo = tattooStylizedList[randint(0, tattooStylizedList.__len__() - 1)]
        rightTattoo = leftTattoo
        if dupeTattoo == False:
            while rightTattoo == leftTattoo:
                rightTattoo = tattooStylizedList[randint(0, tattooStylizedList.__len__() - 1)]
    elif numTattoos == 1:
        if randint(0, 1) == 1:
            rightTattoo = tattooStylizedList[randint(0, tattooStylizedList.__len__() - 1)]
        else:
            leftTattoo = tattooStylizedList[randint(0, tattooStylizedList.__len__() - 1)]             
    else:
        return retVal

    ### SET COLOR ###
    if numTattoos > 0:
        tattooColor = "94"  # Hard coded until color is implemented

    return tuple((leftTattoo, rightTattoo, tattooColor))


def rando_race(nationality):
    '''
        NOTE: National statistics based on data from www.nationsencyclopedia.com
    '''
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')

    ### LOCAL VARIABLES ###
    retVal = ""
    tmpInt = randint(1, 100)

    if nationality == "Argentina":
        if tmpInt <= 97:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Australia":
        if tmpInt <= 92:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 93:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Belgium":
        if tmpInt <= 100:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Brazil":
        if tmpInt <= 74:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 98:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Canada":
        if tmpInt <= 75:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 81:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 90:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "China":
        if tmpInt <= 0:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Egypt":
        if tmpInt <= 1:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 2:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 51:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "France":
        if tmpInt <= 94:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 96:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 98:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Germany":
        if tmpInt <= 97:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Greece":
        if tmpInt <= 99:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "India":
        if tmpInt <= 0:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 50:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Ireland":
        if tmpInt <= 100:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Israel":
        if tmpInt <= 53:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 67:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 80:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Italy":
        if tmpInt <= 100:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Japan":
        if tmpInt <= 1:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Mexico":
        if tmpInt <= 9:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 10:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Netherlands":
        if tmpInt <= 84:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 92:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Nigeria":
        if tmpInt <= 0:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 100:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Norway":
        if tmpInt <= 100:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Poland":
        if tmpInt <= 100:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Russia":
        if tmpInt <= 94:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 98:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Saudi Arabia":
        if tmpInt <= 94:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 97:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Scotland":
        if tmpInt <= 97:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "South Africa":
        if tmpInt <= 14:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 97:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "South Korea":
        if tmpInt <= 0:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 100:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Spain":
        if tmpInt <= 0:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 0:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Sweden":
        if tmpInt <= 98:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 99:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "Ukraine":
        if tmpInt <= 96:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 0:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 98:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "United Kingdom":
        if tmpInt <= 94:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 97:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 99:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    elif nationality == "USA":
        if tmpInt <= 65:
            retVal = listOfRaces[0]     # "0 - Caucasian"
        elif tmpInt <= 78:
            retVal = listOfRaces[1]     # "1 - Afican"
        elif tmpInt <= 83:
            retVal = listOfRaces[2]     # "2 - Asian"
        else:
            retVal = listOfRaces[3]     # "3 - Hispanic"
    else:
        raise ValueError("{} has not yet been implemented".format(nationality))

    return retVal


def rando_hair_style(armorStyle, gender, nationality, race):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')
    elif not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')
    elif not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif not isinstance(race, str):
        raise TypeError('gender is not a string')
    elif race not in listOfRaces:
        raise ValueError('Invalid race')

    ### LOCAL VARIABLES ###
    retVal = ""
    startSlice = ""
    stopSlice = ""
    tmpInt = randint(1, 100)
    hairStylizedList = listOfHairStyles

    ### TRUNCATE EXISTING LIST ###
    # Adjust for Gender
    if gender == listOfGenders[0]:            # "Male"
        hairStylizedList.remove("Pigtails")
        hairStylizedList.remove("Pigtails Fade")
    else:                                     # "Female"
        hairStylizedList.remove("Receding Hair Medium")
        hairStylizedList.remove("Receding Hair Short")
    # Adjust for Nationality
    if nationality in [ "South Africa", "Nigeria" ]:
        hairStylizedList.insert(hairStylizedList.index("Afro"), "Afro")
        hairStylizedList.insert(hairStylizedList.index("Dreadlocks"), "Dreadlocks")
        hairStylizedList.insert(hairStylizedList.index("Dreads Ponytail"), "Dreads Ponytail")
        hairStylizedList.insert(hairStylizedList.index("Cornrows"), "Cornrows")
        hairStylizedList.insert(hairStylizedList.index("Wild Dreadlocks"), "Wild Dreadlocks")
        hairStylizedList.insert(hairStylizedList.index("Wild Dreads Ponytail"), "Wild Dreads Ponytail")
    # Adjust for Race
    if race == listOfRaces[1]:
        hairStylizedList.insert(hairStylizedList.index("Afro"), "Afro")
        hairStylizedList.insert(hairStylizedList.index("Dreadlocks"), "Dreadlocks")
        hairStylizedList.insert(hairStylizedList.index("Dreads Ponytail"), "Dreads Ponytail")
        hairStylizedList.insert(hairStylizedList.index("Cornrows"), "Cornrows")
        hairStylizedList.insert(hairStylizedList.index("Wild Dreadlocks"), "Wild Dreadlocks")
        hairStylizedList.insert(hairStylizedList.index("Wild Dreads Ponytail"), "Wild Dreads Ponytail")

    # Adjust for Style
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        if tmpInt > 25:
            startSlice = "Bald"
            stopSlice = "Blowout"
        else:
            startSlice = hairStylizedList[0]
            stopSlice = hairStylizedList[hairStylizedList.__len__() - 1]
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        if tmpInt > 25:
            startSlice = "Top Knot Fade"
            stopSlice = "Avatar"
        else:
            startSlice = hairStylizedList[0]
            stopSlice = hairStylizedList[hairStylizedList.__len__() - 1]
    elif armorStyle == listOfArmorStyles[2]:  # "Chaotic"
        startSlice = hairStylizedList[0]
        stopSlice = hairStylizedList[hairStylizedList.__len__() - 1]
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        startSlice = "Bald"
        stopSlice = "Parted"
    elif armorStyle == listOfArmorStyles[4]:  # "Alien"
        startSlice = hairStylizedList[0]
        stopSlice = hairStylizedList[hairStylizedList.__len__() - 1]
    else:
        raise ValueError('This armor style has not yet been implemented')

    hairStylizedList = hairStylizedList[hairStylizedList.index(startSlice):hairStylizedList.index(stopSlice) + 1]

    retVal = hairStylizedList[randint(0, hairStylizedList.__len__() - 1)]

    return retVal


def rando_facial_hair(armorStyle, gender, nationality, race):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')
    elif not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')
    elif not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif not isinstance(race, str):
        raise TypeError('gender is not a string')
    elif race not in listOfRaces:
        raise ValueError('Invalid race')

    ### LOCAL VARIABLES ###
    retVal = ""
    startSlice = ""
    stopSlice = ""
    tmpInt = randint(1, 100)
    facialHairStylizedList = deepcopy(listOfFacialHair)

    ### TRUNCATE EXISTING LIST ###
    # Adjust for Gender
    if gender == listOfGenders[1]:            # "Female"
        return None
    # Adjust for Nationality
    elif nationality in [ "Nigeria" ]:
        if tmpInt <= 75:
            return "None"
    elif nationality in [ "South Africa" ]:
        for style in facialHairStylizedList:
            if style.find("tache") >= 0:
                facialHairStylizedList.remove(style)
    elif nationality in [ "Israel" ]:
        for style in listOfFacialHair:
            # print("Israel:\t{}?".format(style))  # DEBUGGING
            if style.find("eard") >= 0:
                facialHairStylizedList.append(style)
    elif nationality in [ "Egypt", "Germany", "USA" ]:
        for style in listOfFacialHair:
            # print("List of Facial Hair:\t{}\n".format(listOfFacialHair))  # DEBUGGING
            if style.find("tache") >= 0:
                facialHairStylizedList.append(style)
    # print("1. Facial Hair List:\t{}\n".format(facialHairStylizedList))  # DEBUGGING
    # Randomize again to avoid patterns
    tmpInt = randint(1, 100)

    # Adjust for Race
    if race in [ listOfRaces[1] ]:
        if tmpInt <= 75:
            return "None"
    elif race in [ listOfRaces[2] ]:
        if tmpInt <= 50:
            return "None"
        else:
            for style in listOfFacialHair:
                # print("Asian:\t{}?".format(style))  # DEBUGGING
                if (style.find("cruffy") >= 0) or (style.find("rappy") >= 0) or (style.find("tubble") >= 0):
                    facialHairStylizedList.append(style)
    # print("2. Facial Hair List:\t{}\n".format(facialHairStylizedList))  # DEBUGGING
    # Randomize AGAIN to avoid patterns
    tmpInt = randint(1, 100)

    # Adjust for Style
    if armorStyle == listOfArmorStyles[0]:    # "Base"
        if tmpInt > 50:
            return "None"
    elif armorStyle == listOfArmorStyles[1]:  # "Anarchy"
        if tmpInt > 75:
            return "None"
    elif armorStyle == listOfArmorStyles[3]:  # "ADVENT"
        return "None"
    # print("3. Facial Hair List:\t{}\n".format(facialHairStylizedList))  # DEBUGGING
    retVal = facialHairStylizedList[randint(0, facialHairStylizedList.__len__() - 1)]

    return retVal


def rando_color_scheme(armorStyle):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')

    ### LOCAL VARIABLES ###
    tmpInt = randint(0, listOfColorSchemes.__len__() - 1)  # Uncomment this once more color schemes are implemented in ColorPalette
    # tmpInt = randint(0, 4)
    
    ### RANDOMIZE A COLOR SCHEME ###
    ############ IMPLEMENT ARMOR STYLE INFLUENCES... LATER ############
    # retVal = listOfColorSchemes[tmpInt]  # Uncomment this once more color schemes are implemented in ColorPalette
    # retVal = listOfColorSchemes[0]  # Monochromatic - Primary Colors
    # retVal = listOfColorSchemes[1]  # Monochromatic - Secondary Colors
    # retVal = listOfColorSchemes[2]  # Monochromatic - Tertiary Colors
    # retVal = listOfColorSchemes[3]  # 2 Colors - Analogous
    # retVal = listOfColorSchemes[4]  # 2 Colors - Complementary
    # retVal = listOfColorSchemes[9]  # 2 Colors - Earthy
    retVal = listOfColorSchemes[11]  # Random Earthy
    # print("Rando Color Scheme returns:\t{}\n".format(retVal))  # DEBUGGING

    return retVal

######################################################
######################################################
################### MAIN EXECUTION ###################
######################################################
######################################################


if __name__ == "__main__":
    ### LOCAL VARIABLES ###
    charOptions = {}
    charInfoList = [ "Name", "Biography", "Nationality", "Gender" ]
    propsOptions = {}
    propsList = [ \
        "Helmet/Hat", "Arms", "Legs", \
        "Torso", "Upper Face Prop", "Lower Face Prop", \
        "Armor Pattern", "Weapon Pattern", "Face Paint", \
        "Left Arm Tattoo", "Right Arm Tattoo", "Tattoo Color", \
        "Scars"\
    ]
    appearanceOptions = {}
    appearanceList = [ \
        "Face", "Hair", "Facial Hair", \
        "Hair Color", "Eye Color", "Race", \
        "Skin Color", "Main Armor Color", "Secondary Armor Color", \
        "Weapon Color", "Voice", "Attitude", \
    ]
    armorColorScheme = ""
    mainArmorColors = None
    secondaryArmorColors = None
    weaponColors = None
    mainColorObject = None  # Variable to hold Color object returned by MainArmorPalette.get_color()
    secondaryColorObject = None  # Variable to hold Color object returned by SecondaryArmorPalette.get_color()
    weaponColorObject = None  # Variable to hold Color object returned by WeaponColorPalette.get_color()

    ### RANDOMIZE OPTIONS ###
    # 1. CHARACTER INFO
    # 1.1. Nationality
    charOptions["Nationality"] = listOfNations[randint(0, listOfNations.__len__() - 1)]
    # 1.2. Gender
    if randint(1, 100) > 49:
        charOptions["Gender"] = listOfGenders[1]
    else:
        charOptions["Gender"] = listOfGenders[0]
    # 1.3. Name
    charOptions["Name"] = rando_name(charOptions["Nationality"], \
                                     charOptions["Gender"])
    # 1.4. Backstory
    charOptions["Biography"] = rando_backstory(charOptions["Name"], \
                                               charOptions["Nationality"], \
                                               charOptions["Gender"])

    # 2. PROPS
    # 2.1. Armor
    propsOptions["Arms"], propsOptions["Legs"], propsOptions["Torso"], propsOptions["Armor Style"] = rando_armor()
    # 2.2. Helmet/Hat
    propsOptions["Helmet/Hat"] = rando_helmet_hat(propsOptions["Armor Style"])
    # 2.3. Upper Face
    propsOptions["Upper Face Prop"] = rando_upper_face(charOptions["Gender"])
    # 2.4. Lower Face
    propsOptions["Lower Face Prop"] = rando_lower_face(charOptions["Nationality"])
    # 2.5. Armor Pattern
    propsOptions["Armor Pattern"] = rando_armor_pattern(propsOptions["Armor Style"])
    # 2.5. Weapon Pattern
    propsOptions["Weapon Pattern"] = rando_weapon_pattern(propsOptions["Armor Style"], \
                                                          propsOptions["Armor Pattern"])
    # 2.6. Face Paint
    propsOptions["Face Paint"] = rando_face_paint(propsOptions["Armor Style"])
    # 2.7. Left and Right Arm Tattoos
    propsOptions["Left Arm Tattoo"], propsOptions["Right Arm Tattoo"], propsOptions["Tattoo Color"] = rando_tattoos(propsOptions["Armor Style"])
    # 2.8. Scars
    # Not implementing scars because I want to choose scars as my characters get injured on mission

    # 3. APPEARANCE
    # 3.1. Face
    appearanceOptions["Face"] = listOfFaces[randint(0, listOfFaces.__len__() - 1)]
    # 3.5. Race
    appearanceOptions["Race"] = rando_race(charOptions["Nationality"])
    # 3.2. All Hair Styles
    # 3.2.1. Hair
    appearanceOptions["Hair"] = rando_hair_style(propsOptions["Armor Style"], \
                                                 charOptions["Gender"], \
                                                 charOptions["Nationality"], \
                                                 appearanceOptions["Race"])
    # 3.2.2. Facial Hair
    appearanceOptions["Facial Hair"] = rando_facial_hair(propsOptions["Armor Style"], \
                                                         charOptions["Gender"], \
                                                         charOptions["Nationality"], \
                                                         appearanceOptions["Race"])
    # 3.3. Hair Color
    # 3.4. Eye Color
    # 3.6. Skin Color
    # 3.7. Main Armor Color
    # 3.7.1. Randomize a Color Scheme
    armorColorScheme = rando_color_scheme(propsOptions["Armor Style"])
    # print("Armor Color Scheme:\t{}\n".format(armorColorScheme))  # DEBUGGING
    # 3.7.2. Instanstiate Main Armor Colors Object
    mainArmorColors = MainArmorPalette(armorColorScheme)
    # 3.7.3. Randomize a Main Armor Color
    mainColorObject = mainArmorColors.get_color()
    # 3.7.4. Store the Main Armor Color Object's number
    appearanceOptions["Main Armor Color"] = mainColorObject.num
    # 3.8. Secondary Armor Color
    # 3.8.1. Instanstiate Secondary Armor Colors Object
    secondaryArmorColors = SecondaryArmorPalette(armorColorScheme)
    # 3.8.2. Randomize a Secondary Armor Color Object
    secondaryColorObject = secondaryArmorColors.get_color(mainColorObject)
    # 3.8.3. Store the Secondary Armor Color Object's number
    appearanceOptions["Secondary Armor Color"] = secondaryColorObject.num
    # 3.9. Weapon Color
    # 3.9.1. Instantiate Weapon Color Object
    weaponColors = WeaponColorPalette(armorColorScheme)
    # 3.9.2. Randomize a Weapon Color Object
    weaponColorObject = weaponColors.get_color(mainColorObject, secondaryColorObject)
    
    # 3.9.3. Store the Weapon Color Object's number
    appearanceOptions["Weapon Color"] = weaponColorObject.num
    # 3.10. Voice
    # 3.11. Attitude

    ### PRINT RANDOMIZED OPTIONS ###
    # 1. CHARACTER INFO
    print("\n")
    # print("CHARACTER INFO:")
    # for key in charInfoList:
    #     if key in charOptions.keys():
    #         if charOptions[key] != None:
    #             print("\t{}:  {}".format(key, charOptions[key]))
    # print("\n")

    # 2. PROPS
    # print("PROPS:")
    # for key in propsList:
    #     if key in propsOptions.keys():
    #         if propsOptions[key] != None:
    #             print("\t{}:  {}".format(key, propsOptions[key]))
    # print("\n")

    # 3. APPEARANCE
    print("APPEARANCE:")
    print("\t{}:\t{}".format("Armor Style", propsOptions["Armor Style"]))  # DEBUGGING
    for key in appearanceList:
        if key in appearanceOptions.keys():
            if appearanceOptions[key] != None:
                print("\t{}:  {}".format(key, appearanceOptions[key]))
    print("\n")

    ### TESTING ###
    print("Armor Color Scheme:\t{}\n".format(armorColorScheme))  # DEBUGGING
    print_color_object(mainColorObject)  # DEBUGGING
    print_color_object(secondaryColorObject)  # DEBUGGING
    print_color_object(weaponColorObject)  # DEBUGGING
    # print(dir(mainArmorColors))
    # for swatch in mainArmorColors.listOfBrownColors:
    #     print("{} is Brown".format(swatch.num))
    # print_color_object(Color(41, 18, 15, 45))  # DEBUGGING
    # for swatch in mainArmorColors.listOfColors:
    #     if swatch.num in [ 0, 1, 28, 33, 34, 79, 80, 81 ]:
    #         print("{} is light green?".format(swatch.num))
    #         print_color_object(swatch)


