from random import randint
import os

'''
Props:
Upper Face Prop
Lower Face Prop
Armor Pattern (Optional)
Weapon Pattern (Optional)
Face Paint
Left Arm Tattoo
Right Arm Tattoo
Tattoo Color
Scars

Face:
Hair:
Facial Hair:
Hair Color:
Eye Color:
Race:
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
    "Colors - Analogous", "2 Colors - Complementary", "3 Colors - Triad", \
    "Random Chaos", "Earthy", "Urban", \
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
######################################################
######################################################
################## HELPER FUNCTIONS ##################
######################################################
######################################################


########################
### HELPER FUNCTIONS ###
########################


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


def rando_helmet_hat():
    ### LOCAL VARIABLES ###
    retVal = listOfHelmetHats[randint(0, listOfHelmetHats.__len__() - 1)]

    return retVal


def rando_armor():
    '''
        PURPOSE:    Choose a set of styles for the character's armor
        INPUT:      None
        OUTPUT:     A tuple of strings ("<Arms>", "<Legs>", "<Torso>", "<Style>")
        NOTE:       Styles include: "Base", "Anarchy", "Chaotic"
    '''
    ### LOCAL VARIABLES ###
    style = ""
    tmpInt = 0
    retArm = ""
    retLeg = ""
    retTorso = ""

    ### CHOOSE STYLE ###
    tmpInt = randint(1, 10)
    if tmpInt <= 4:
        style = "Base"
    elif tmpInt <= 8:
        style = "Anarchy"
    else:
        style = "Chaotic"

    ### RANDOMIZE ARM ###
    if style == "Base":
        tmpInt = randint(0, 6)
    elif style == "Anarchy":
        tmpInt = randint(7, 11)
    else:
        tmpInt = randint(0, 11)
    retArm = listOfArmorArms[tmpInt]

    ### RANDOMIZE LEG ###
    if style == "Base":
        tmpInt = randint(0, 4)
    elif style == "Anarchy":
        tmpInt = randint(5, 7)
    else:
        tmpInt = randint(0, 7)
    retLeg = listOfArmorLegs[tmpInt]

    ### RANDOMIZE TORSO ###
    if style == "Base":
        tmpInt = randint(0, 4)
    elif style == "Anarchy":
        tmpInt = randint(5, 7)
    else:
        tmpInt = randint(0, 7)
    retTorso = listOfArmorTorso[tmpInt]

    return tuple((retArm, retLeg, retTorso, style))


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
    
    ### RANDOMIZE OPTIONS ###
    # 1. CHARACTER INFO
    # 1.1. Nationality
    charOptions["Nationality"] = listOfNations[randint(0, listOfNations.__len__() - 1)]
    # 1.2. Gender
    charOptions["Gender"] = listOfGenders[randint(0, listOfGenders.__len__() - 1)]
    # 1.3. Name
    charOptions["Name"] = rando_name(charOptions["Nationality"], charOptions["Gender"])
    # 1.4. Backstory
    charOptions["Biography"] = rando_backstory(charOptions["Name"], \
                                               charOptions["Nationality"], \
                                               charOptions["Gender"])

    # 2. PROPS
    # 2.1. Helmet/Hat
    propsOptions["Helmet/Hat"] = rando_helmet_hat()
    # 2.2. Armor
    propsOptions["Arms"], propsOptions["Legs"], propsOptions["Torso"], \
    propsOptions["Armor Style"] = rando_armor()
    # 2.3. Upper Face
    propsOptions["Upper Face Prop"] = rando_upper_face(charOptions["Gender"])
    # 2.4. Lower Face
    # propsOptions["Lower Face Prop"] = rando_lower_face(charOptions["Gender"])


    ### PRINT RANDOMIZED OPTIONS ###
    # 1. CHARACTER INFO
    print("\n")
    print("CHARACTER INFO:")
    for key in charInfoList:
        if key in charOptions.keys():
            print("\t{}:  {}".format(key, charOptions[key]))
    print("\n")

    # 2. PROPS
    print("PROPS:")
    for key in propsList:
        if key in propsOptions.keys():
            print("\t{}:  {}".format(key, propsOptions[key]))
    print("\n")
    # print("\t{}:  {}".format("Armor Style", propsOptions["Armor Style"]))  # DEBUGGING













