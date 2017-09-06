from argparse import ArgumentParser
from collections import OrderedDict
from copy import deepcopy
from Harklepalette import Color
from Harklepalette import MainArmorPalette
from Harklepalette import print_color_object
from Harklepalette import SecondaryArmorPalette
from Harklepalette import WeaponColorPalette
from Harklepalette import EyeColorPalette
from random import randint
import os


######################################################
######################################################
##################### ARG PARSER #####################
######################################################
######################################################


class ParseArgument(ArgumentParser):
    
    
    def parse_error(self, message):
        os.stderr.write("Error:  %s\n" % message)
        self.print_help()
        exit(2)
        
        
def parse_arguments():
    '''
        Input - None
        Output - Command line argument list from ParseArgument object
    '''
    # Parser object
    parser = ParseArgument()
    
    # Command line arguments
    parser.add_argument("-f", "--file", required = False, action = "store_true", help = "Print character details to a file")
    parser.add_argument("-q", "--quiet", required = False, action = "store_true", help = "Do not print to screen (inherint -f)")
    parser.add_argument("-w", "--WotC", required = False, action = "store_true", help = "Randomize for War of the Chosen expansion")
    
    # List of arguments from the command line
    args = parser.parse_args()
    
    return args


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
        "2 Colors - Earthy", \
        # "3 Colors - Earthy" not yet implemented
        "Random Earthy", \
        "Urban", "Goth", "Parallel", \
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
    "Torso 6", "Torso 7", "Torso 8", \
    "Torso 9", "Torso 10", "Torso 11", \
    "Torso 12", "Torso 13", "Torso 14", \
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

listOfVoices = [ \
    "American English 1", "American English 2", "American English 3", \
    "American English 4", "American English 5", "American English 6", \
    "American English 7", "American English 8", "American English 9", \
    "American English 10", \
    "UK English 1", "UK English 2", "UK English 3", "UK English 4", \
    "Australian English 1", "Australian English 2", \
    "French 1", "French 2", "French 3", \
    "French 4", "French 5", "French 6", \
    "French 7", "French 8", "French 9", \
    "French 10", \
    "German 1", "German 2", "German 3", \
    "German 4", "German 5", "German 6", \
    "German 7", "German 8", "German 9", \
    "German 10", \
    "Italian 1", "Italian 2", "Italian 3", \
    "Italian 4", "Italian 5", "Italian 6", \
    "Italian 7", "Italian 8", "Italian 9", \
    "Italian 10", \
    "Spanish 1", "Spanish 2", "Spanish 3", \
    "Spanish 4", "Spanish 5", "Spanish 6", \
    "Spanish 7", "Spanish 8", "Spanish 9", \
    "Spanish 10", \
]

listOfAttitudes = [ \
    "By The Book", "Laid Back", "Normal", \
    "Twitchy", "Happy-Go-Lucky", "Hard Luck", \
    "Intense", \
]


######################################################
######################################################
################## HELPER FUNCTIONS ##################
######################################################
######################################################


################################
### GENERIC HELPER FUNCTIONS ###
################################


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


def print_char_to_file(sectionHeaderDict, charDetails):
    '''
        Input
            sectionHeaderDict - OrderedDict of headers and list items to print
            charDetails - Dictionary of all the character details to print
        Output - Filename that was created
        Note
            Filename will be first_last.txt
            Spaces in the name will be replaced by underscores
    '''
    ### INPUT VALIDATION ###
    if not isinstance(sectionHeaderDict, dict):
        raise TypeError("Not a dict")
    elif not isinstance(charDetails, dict):
        raise TypeError("Not a dict")
    elif sectionHeaderDict.__len__() < 3:
        raise ValueError("Not enough sections")
    elif charDetails.__len__() == 0:
        raise ValueError("Character details are empty")
    # This is the common thread between both version
    elif "CHARACTER INFO" not in sectionHeaderDict.keys():
        raise ValueError("Character info missing")
    # This key is necessary to create the filename
    elif "Name" not in charDetails.keys():
        raise ValueError("Character name missing")
    elif charDetails["Name"].__len__() < 2 or charDetails["Name"] is None:
        raise ValueError("Invalid character name")

    ### LOCAL VARIABLES ###
    retVal = ""
    tempFilename = ""
    fileNumber = 0

    ### BUILD FILENAME ###
    # Get the character's name
    retVal = charDetails["Name"]
    # Remove leading space
    if retVal[0] == " ":
        retVal = retVal[1:]
    # Remove trailing space
    if retVal[retVal.__len__() - 1] == " " and retVal.__len__() > 1:
        retVal = retVal[:retVal.__len__() - 2]
    # Replace spaces
    retVal = retVal.replace(" ", "_")
    # Replace odd characters
    retVal = retVal.replace("À", "A")
    retVal = retVal.replace("Ã", "A")
    retVal = retVal.replace("á", "a")
    retVal = retVal.replace("ä", "a")
    retVal = retVal.replace("å", "a")
    retVal = retVal.replace("é", "e")
    retVal = retVal.replace("ë", "e")
    retVal = retVal.replace("è", "e")
    retVal = retVal.replace("Í", "I")
    retVal = retVal.replace("ï", "i")
    retVal = retVal.replace("í", "i")
    retVal = retVal.replace("ñ", "n")
    retVal = retVal.replace("Õ", "O")
    retVal = retVal.replace("ó", "o")
    retVal = retVal.replace("ô", "o")
    retVal = retVal.replace("õ", "o")
    retVal = retVal.replace("ú", "u")
    retVal = retVal.replace("ù", "u")    

    ### VALIDATE FILENAME ###
    while True:
        # Add fileNumber
        if fileNumber == 0:
            tempFilename = retVal
        else:
            tempFilename = retVal + str(fileNumber) 
        # Add file type
        tempFilename = tempFilename + ".txt"

        if os.path.exists(tempFilename):
            fileNumber += 1
        else:
            retVal = tempFilename
            break

    ### PRINT TO THE FILE ###
    with open(tempFilename, "w") as outFile:
        outFile.write("\n")
        for header in sectionHeaderDict:
            outFile.write(header + ":\n")
            for listEntry in sectionHeaderDict[header]:
                if listEntry in charDetails.keys():
                    if charDetails[listEntry] != None:
                        outFile.write("\t{}:  {}\n".format(listEntry, charDetails[listEntry]))
            outFile.write("\n")
        outFile.write("\n")

    return retVal


################################
### CHARACTER INFO FUNCTIONS ###
################################


def rando_nation():
    ### LOCAL VARIABLES ###
    retVal = ""     # Will hold one of the entries from listOfNations
    randNum = 0     # Randomly generated number
    randNum = randint(1, 10000)

    if randNum > 9982:
        retVal = "Israel"
    elif randNum > 9283:
        retVal = "USA"
    elif randNum > 9272:
        retVal = "Norway"
    elif randNum > 9262:
        retVal = "Ireland"
    elif randNum > 6291:
        retVal = "China"
    elif randNum > 6151:
        retVal = "United Kingdom"
    elif randNum > 6032:
        retVal = "South Africa"
    elif randNum > 5621:
        retVal = "Nigeria"
    elif randNum > 2748:
        retVal = "India"
    elif randNum > 2670:
        retVal = "Canada"
    elif randNum > 2575:
        retVal = "Ukraine"
    elif randNum > 2563:
        retVal = "Scotland"
    elif randNum > 2527:
        retVal = "Netherlands"
    elif randNum > 2504:
        retVal = "Greece"
    elif randNum > 2052:
        retVal = "Brazil"
    elif randNum > 2030:
        retVal = "Sweden"
    elif randNum > 1960:
        retVal = "Saudi Arabia"
    elif randNum > 1682:
        retVal = "Mexico"
    elif randNum > 1509:
        retVal = "Germany"
    elif randNum > 1484:
        retVal = "Belgium"
    elif randNum > 1386:
        retVal = "Spain"
    elif randNum > 1079:
        retVal = "Russia"
    elif randNum > 809:
        retVal = "Japan"
    elif randNum > 670:
        retVal = "France"
    elif randNum > 618:
        retVal = "Australia"
    elif randNum > 509:
        retVal = "South Korea"
    elif randNum > 427:
        retVal = "Poland"
    elif randNum > 299:
        retVal = "Italy"
    elif randNum > 95:
        retVal = "Egypt"
    elif randNum > 0:
        retVal = "Argentina"
    else:
        raise RuntimeError("rando_nation:  How did we get here?")

    return retVal


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
    # Handle errant spaces
    if "" in nameList:
        nameList.remove("")

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
        retVal = retVal + " in " + homeTown + " " + nationality
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
        retVal = retVal + " in " + rando_city_state(nationality) + " " + nationality + "."
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
    cityStateFile = os.path.join("Lists", "02-Biography_City_State_" + nationality.replace(" ", "_") + ".txt")

    ### READ LAST NAME ###
    if os.path.isfile(cityStateFile) is False:
        cityStateFile = cityStateFile.replace(nationality.replace(" ", "_"), "USA")
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
    firstNameFile = os.path.join("Lists", "01-Name_First_" + gender + "_" + nationality.replace(" ", "_") + ".txt")
    # print("First Name File:\t{}".format(firstNameFile))  # DEBUGGING 

    ### READ FIRST NAME ###
    # if os.path.isfile(firstNameFile) is False:
    #     firstNameFile = firstNameFile.replace(nationality.replace(" ", "_"), "USA")
    if os.path.isfile(firstNameFile) is False:
        raise OSError('Unable to find necessary list file {} for nationality {}, gender {}'.format(firstNameFile, nationality, gender))

    with open(firstNameFile, "r") as fnFile:    
        [listOfFirstNames.append(name) for name in fnFile.read().split('\n') if name.__len__() > 0]

    ### RANDOMIZE A NAME ###
    if listOfFirstNames.__len__() == 0:
        print("List of First Names is empty for nationality {} and gender {}".format(nationality, gender))  # DEBUGGING
    retVal = listOfFirstNames[randint(0, listOfFirstNames.__len__() - 1)]

    return retVal


def rando_last_name(nationality):
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
    lastNameFile = os.path.join("Lists", "01-Name_Last_" + nationality.replace(" ", "_") + ".txt")

    ### READ LAST NAME ###
    # if os.path.isfile(lastNameFile) is False:
    #     lastNameFile = lastNameFile.replace(nationality.replace(" ", "_"), "USA")
    if os.path.isfile(lastNameFile) is False:
        raise OSError('Unable to find necessary list file {} for nationality {}'.format(lastNameFile, nationality))

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
    
    ### RANDOMIZE A COLOR SCHEME ###
    retVal = listOfColorSchemes[tmpInt]  # Uncomment this once more color schemes are implemented in ColorPalette

    return retVal


def rando_voice(nationality, race):
    ### INPUT VALIDATION ###
    if not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif not isinstance(race, str):
        raise TypeError('gender is not a string')
    elif race not in listOfRaces:
        raise ValueError('Invalid race')

    ### LOCAL VARIABLES ###
    retVal = None       # Will hold a string from listOfVoices
    tmpVoiceList = []   # Will hold a dynamically built list of nation-appropriate voices

    ### CHOOSE A VOICE ###
    # Setup dynamically built lists of appropriate voices
    if nationality in [ "Argentina", "Brazil", "Mexico", "Spain" ]:
        if race == "0 - Caucasian":
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        elif race == "3 - Hispanic":
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Spanish") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Spanish") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Spanish") >= 0 ]
    elif nationality in [ "Australia" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Australian") >= 0 ]
    elif nationality in [ "United Kingdom" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
    elif nationality in [ "Canada" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("French") >= 0 ]
    elif nationality in [ "Belgium" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("French") >= 0 ]
    elif nationality in [ "France" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("French") >= 0 ]
    elif nationality in [ "Germany" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("German") >= 0 ]
    elif nationality in [ "China", "Greece", "Israel", "Japan", "Poland", "Russia", "Saudi Arabia", "South Korea", "Sweden", "Ukraine" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
    elif nationality in [ "India", "Ireland", "Scotland" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
    elif nationality in [ "Egypt", "Nigeria", "Netherlands", "Norway", "South Africa" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("UK") >= 0 ]
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
    elif nationality in [ "Italy" ]:
        tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Italian") >= 0 ]
    elif nationality in [ "USA" ]:
        if race in [ "0 - Caucasian", "1 - Afican", "2 - Asian" ]:
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
        elif race == "3 - Hispanic":
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("Spanish") >= 0 ]
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
            tmpVoiceList = tmpVoiceList + [ voice for voice in listOfVoices if voice.find("American") >= 0 ]
    else:
        raise RuntimeError("rando_voice:\tNationality '{}' is not implemented".format(nationality))


    # Randomly select from dynamically built list
    if tmpVoiceList.__len__() == 0:
        raise RuntimeError("rando_voice:\tDid not dynamically add any voices to the list")
    else:
        retVal = tmpVoiceList[randint(0, tmpVoiceList.__len__() - 1)]

    return retVal


def rando_attitude(armorStyle):
    ### INPUT VALIDATION ###
    if not isinstance(armorStyle, str):
        raise TypeError('armorStyle is not a string')
    elif armorStyle not in listOfArmorStyles:
        raise ValueError('Invalid armorStyle')

    ### LOCAL VARIABLES ###
    retVal = None       # Will hold a string from listOfAttitudes
    tmpAttList = []     # Will hold a dynamically built list of style-appropriate attitudes

    ### CHOOSE A VOICE ###
    # Setup dynamically built lists of appropriate voices
    if armorStyle in [ "Base" ]:
        tmpAttList = tmpAttList + [ attitude for attitude in listOfAttitudes if attitude.__len__() > 0 ]
    elif armorStyle in [ "Anarchy", "Chaotic" ]:
        tmpAttList = tmpAttList + [ attitude for attitude in listOfAttitudes if attitude.__len__() > 0 ]
        tmpAttList.remove("By The Book")
        tmpAttList.append("Laid Back")
        tmpAttList.append("Twitchy")
        tmpAttList.append("Hard Luck")
        tmpAttList.append("Intense")
    elif armorStyle in [ "ADVENT" ]:
        tmpAttList = tmpAttList + [ attitude for attitude in listOfAttitudes if attitude.__len__() > 0 ]
        tmpAttList.append("By The Book")
        tmpAttList.append("Normal")
        tmpAttList.append("Twitchy")
        tmpAttList.append("Hard Luck")
        tmpAttList.append("Intense")
    elif armorStyle in [ "Alien" ]:
        tmpAttList = tmpAttList + [ attitude for attitude in listOfAttitudes if attitude.__len__() > 0 ]
        tmpAttList.remove("Laid Back")
        tmpAttList.remove("Happy-Go-Lucky")
    else:
        raise RuntimeError("rando_voice:\tNationality '{}' is not implemented".format(nationality))
    # Randomly select from dynamically built list
    if tmpAttList.__len__() == 0:
        raise RuntimeError("rando_attitude:\tDid not dynamically add any attitudes to the list")
    else:
        retVal = tmpAttList[randint(0, tmpAttList.__len__() - 1)]

    return retVal


######################################################
######################################################
################### MAIN EXECUTION ###################
######################################################
######################################################


def main():
    ### LOCAL VARIABLES ###
    charDetails = {}  # One dictionary to rule them all
    charInfoList = [ "Name", "Biography", "Nationality", "Gender" ]
    propsList = [ \
        "Helmet/Hat", "Arms", "Legs", \
        "Torso", "Upper Face Prop", "Lower Face Prop", \
        "Armor Pattern", "Weapon Pattern", "Face Paint", \
        "Left Arm Tattoo", "Right Arm Tattoo", "Tattoo Color", \
        "Scars", \
    ]
    appearanceList = [ \
        "Face", "Hair", "Facial Hair", \
        "Hair Color", "Eye Color", "Race", \
        "Skin Color", "Main Armor Color", "Secondary Armor Color", \
        "Weapon Color", "Voice", "Attitude", \
    ]
    sectionHeaderDict = OrderedDict()  # Ordered dictionary of section headers and lists to print
    armorColorScheme = ""
    mainArmorColors = None
    secondaryArmorColors = None
    weaponColors = None
    eyeColors = None            # Holds EyeColorPalette object
    mainColorObject = None      # Variable to hold Color object returned by MainArmorPalette.get_color()
    secondaryColorObject = None # Variable to hold Color object returned by SecondaryArmorPalette.get_color()
    weaponColorObject = None    # Variable to hold Color object returned by WeaponColorPalette.get_color()
    eyeColorObject = None       # Holds Color object returned by EyeColorPalette.get_eye_color()
    # War of the Chosen variables
    warOfTheChosen = False      # Are we randomzing for the War of the Chosen expansion?
    wotcCharInfoList = charInfoList + [ "Voice", "Attitude" ]
    wotcHeadList = appearanceList[:appearanceList.index("Main Armor Color")] + \
        [ "Helmet/Hat", "Upper Face Prop", "Lower Face Prop", "Face Paint", "Scars" ]
    wotcBodyList = [ \
        "Main Armor Color", "Secondary Armor Color", "Armor Pattern", \
        "Arms", "Torso", "Legs", \
        "Left Arm Tattoo", "Right Arm Tattoo", "Tattoo Color", \
    ]
    wotcWeaponList = [ "Weapon Color", "Weapon Pattern" ]
    # Other command line variables
    saveToFile = False          # Save character info to a file?
    outFilename = ""            # Filename to save the file to
    quietMode = False           # Indicates whether or not to print to screen
    

    ### PARSE XRANDO ARGUMENTS ###
    args = parse_arguments()
    # print("Args:\t{}".format(args))  # DEBUGGING

    #############################################################
    # -w, --WotC, "Randomize for War of the Chosen expansion"
    #############################################################
    try:
        # War of the Chosen
        if args.WotC:
            # Set boolean
            warOfTheChosen = True

            # Build sectionHeaderDict for War of the Chosen
            sectionHeaderDict["CHARACTER INFO"] = wotcCharInfoList
            sectionHeaderDict["HEAD"] = wotcHeadList
            sectionHeaderDict["BODY"] = wotcBodyList
            sectionHeaderDict["WEAPON"] = wotcWeaponList

            # Modify existing lists
            # 1. CHARACTER INFO
            # Nationality
            listOfNations = listOfNations + [ \
                "Colombia", "Indonesia", "Iran", \
                "Pakistan", "Portugal", "Turkey", \
                "Venezuela", \
            ]
            listOfNations.remove("Saudi Arabia")
            # 2. HEAD
            # 3. BODY
            # 4. WEAPON
    except:
        pass

    # Base XCOM 2
    if sectionHeaderDict.__len__() == 0:
        # Build sectionHeaderDict for Base XCOM 2
        sectionHeaderDict["CHARACTER INFO"] = charInfoList
        sectionHeaderDict["PROPS"] = propsList
        sectionHeaderDict["APPEARANCE"] = appearanceList

    #############################################################
    # -f, --file, "Print character details to a file"
    #############################################################
    try:
        if args.file:
            # Set boolean
            saveToFile = True
    except:
        pass

    #############################################################
    # -q, --quiet, "Do not print to screen (inherint -f)"
    #############################################################
    try:
        if args.quiet:
            # Set boolean
            quietMode = True
            saveToFile = True
    except:
        pass

    ### RANDOMIZE OPTIONS ###
    # 1. CHARACTER INFO
    # 1.1. Nationality
    charDetails["Nationality"] = rando_nation()
    # 1.2. Gender
    if randint(1, 100) > 49:
        charDetails["Gender"] = listOfGenders[1]
    else:
        charDetails["Gender"] = listOfGenders[0]
    # 1.3. Name
    charDetails["Name"] = rando_name(charDetails["Nationality"], \
                                     charDetails["Gender"])
    # 1.4. Backstory
    charDetails["Biography"] = rando_backstory(charDetails["Name"], \
                                               charDetails["Nationality"], \
                                               charDetails["Gender"])

    # 2. PROPS
    # 2.1. Armor
    charDetails["Arms"], charDetails["Legs"], charDetails["Torso"], charDetails["Armor Style"] = rando_armor()
    # 2.2. Helmet/Hat
    charDetails["Helmet/Hat"] = rando_helmet_hat(charDetails["Armor Style"])
    # 2.3. Upper Face
    charDetails["Upper Face Prop"] = rando_upper_face(charDetails["Gender"])
    # 2.4. Lower Face
    charDetails["Lower Face Prop"] = rando_lower_face(charDetails["Nationality"])
    # 2.5. Armor Pattern
    charDetails["Armor Pattern"] = rando_armor_pattern(charDetails["Armor Style"])
    # 2.5. Weapon Pattern
    charDetails["Weapon Pattern"] = rando_weapon_pattern(charDetails["Armor Style"], \
                                                         charDetails["Armor Pattern"])
    # 2.6. Face Paint
    charDetails["Face Paint"] = rando_face_paint(charDetails["Armor Style"])
    # 2.7. Left and Right Arm Tattoos
    charDetails["Left Arm Tattoo"], charDetails["Right Arm Tattoo"], charDetails["Tattoo Color"] = rando_tattoos(charDetails["Armor Style"])
    # 2.8. Scars
    # Not implementing scars because I want to choose scars as my characters get injured on mission

    # 3. APPEARANCE
    # 3.1. Face
    charDetails["Face"] = listOfFaces[randint(0, listOfFaces.__len__() - 1)]
    # 3.5. Race
    charDetails["Race"] = rando_race(charDetails["Nationality"])
    # 3.2. All Hair Styles
    # 3.2.1. Hair
    charDetails["Hair"] = rando_hair_style(charDetails["Armor Style"], \
                                           charDetails["Gender"], \
                                           charDetails["Nationality"], \
                                           charDetails["Race"])
    # 3.2.2. Facial Hair
    charDetails["Facial Hair"] = rando_facial_hair(charDetails["Armor Style"], \
                                                         charDetails["Gender"], \
                                                         charDetails["Nationality"], \
                                                         charDetails["Race"])
    # 3.3. Hair Color

    # 3.6. Skin Color
    # 3.7. Main Armor Color
    # 3.7.1. Randomize a Color Scheme
    armorColorScheme = rando_color_scheme(charDetails["Armor Style"])
    # print("Armor Color Scheme:\t{}\n".format(armorColorScheme))  # DEBUGGING
    # 3.7.2. Instanstiate Main Armor Colors Object
    mainArmorColors = MainArmorPalette(armorColorScheme)
    # 3.7.3. Randomize a Main Armor Color
    mainColorObject = mainArmorColors.get_color()
    # 3.7.4. Store the Main Armor Color Object's number
    charDetails["Main Armor Color"] = mainColorObject.num
    # 3.8. Secondary Armor Color
    # 3.8.1. Instanstiate Secondary Armor Colors Object
    secondaryArmorColors = SecondaryArmorPalette(armorColorScheme)
    # 3.8.2. Randomize a Secondary Armor Color Object
    secondaryColorObject = secondaryArmorColors.get_color(mainColorObject)
    # 3.8.3. Store the Secondary Armor Color Object's number
    charDetails["Secondary Armor Color"] = secondaryColorObject.num
    # 3.9. Weapon Color
    # 3.9.1. Instantiate Weapon Color Object
    weaponColors = WeaponColorPalette(armorColorScheme)
    # 3.9.2. Randomize a Weapon Color Object
    weaponColorObject = weaponColors.get_color(mainColorObject, secondaryColorObject)
    
    # 3.9.3. Store the Weapon Color Object's number
    charDetails["Weapon Color"] = weaponColorObject.num
    # 3.10. Voice
    charDetails["Voice"] = rando_voice(charDetails["Nationality"], charDetails["Race"])
    # 3.11. Attitude
    charDetails["Attitude"] = rando_attitude(charDetails["Armor Style"])


    # 3.4. Eye Color
    # 3.4.1. Instantiate Eye Color Palette
    # EyeColorPalette(scheme, armorStyle, nationality, race, gender, mainColor)
    eyeColors = EyeColorPalette(armorColorScheme, charDetails["Armor Style"], charDetails["Nationality"], \
                                charDetails["Race"], charDetails["Gender"], mainColorObject)
    # 3.4.2. Randomize an Eye Color Object
    eyeColorObject = eyeColors.get_eye_color()
    # 3.4.3. Store the Eye Color Object's number
    charDetails["Eye Color"] = eyeColorObject.num

    ### PRINT RANDOMIZED OPTIONS ###
    if not quietMode:
        print("\n")
        for header in sectionHeaderDict:
            print(header + ":")
            for listEntry in sectionHeaderDict[header]:
                if listEntry in charDetails.keys():
                    if charDetails[listEntry] != None:
                        print("\t{}:  {}".format(listEntry, charDetails[listEntry]))
            print("\n")

    ### PRINT FILE ###
    if saveToFile:
        outFilename = print_char_to_file(sectionHeaderDict, charDetails)
        if not quietMode:
            print("\nExported character to:\t{}".format(outFilename))

    ### TESTING ###


if __name__ == "__main__":
    main()