from random import randint
import os

# TEMPLATE
'''
Character Info:
First Name
Last Name
Biography (Optional)
Nationality
Gender

Props:
Helmet/Hat
Arms
Legs
Torso
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

listOfNations = [ 
    "Argentina", "Australia", "Belgium", "Brazil", "Canada", "China", \
    "Egypt", "France", "Germany", "Greece", "India", "Ireland", "Israel", \
    "Italy", "Japan", "Mexico", "Netherlands", "Nigeria", "Norway", \
    "Poland", "Russia", "Saudi Arabia", "Scotland", "South Africa", \
    "South Korea", "Spain", "Sweden", "Ukraine", "United Kingdom", "USA", \
]

listOfGenders = [ "Male", "Female" ]


def rando_backstory(firstName, lastName, nationality, gender):
    ### INPUT VALIDATION ###
    if not isinstance(firstName, str):
        raise TypeError('firstName is not a string')
    elif not isinstance(lastName, str):
        raise TypeError('lastName is not a string')
    elif not isinstance(nationality, str):
        raise TypeError('nationality is not a string')
    if not isinstance(gender, str):
        raise TypeError('gender is not a string')
    elif nationality not in listOfNations:
        raise ValueError('Invalid nationality')
    elif gender not in listOfGenders:
        raise ValueError('Invalid gender')

    ### LOCAL VARIABLES ###
    retVal = ""

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
    listOfFirstNames = []
    listOfLastNames = []
    firstNameFile = os.path.join("Lists", "01-Name_First_" + gender + "_" + nationality + ".txt")
    lastNameFile = os.path.join("Lists", "01-Name_Last_" + nationality + ".txt")

    ### READ FIRST NAME ###
    if os.path.isfile(firstNameFile) is False:
        firstNameFile = firstNameFile.replace(nationality, "USA")
    if os.path.isfile(firstNameFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(firstNameFile, "r") as fnFile:    
        [listOfFirstNames.append(name) for name in fnFile.read().split('\n') if name.__len__() > 0]

    # print(listOfFirstNames)  # DEBUGGING

    ### READ LAST NAME ###
    if os.path.isfile(lastNameFile) is False:
        lastNameFile = lastNameFile.replace(nationality, "USA")
    if os.path.isfile(lastNameFile) is False:
        raise OSError('Unable to find necessary list file')

    with open(lastNameFile, "r") as fnFile:    
        [listOfLastNames.append(name) for name in fnFile.read().split('\n') if name.__len__() > 0]

    # print(listOfLastNames)  # DEBUGGING

    ### RANDOMIZE A NAME ###
    retVal = listOfFirstNames[randint(0, listOfFirstNames.__len__() - 1)] + " "
    retVal = retVal + listOfLastNames[randint(0, listOfLastNames.__len__() - 1)]

    return retVal


if __name__ == "__main__":
    ### LOCAL VARIABLES ###
    charOptions = {}
    charInfoList = ["Name", "Biography", "Nationality", "Gender"]
    
    ### RANDOMIZE OPTIONS ###
    # 1. CHARACTER INFO
    # 1.1. Nationality
    charOptions["Nationality"] = listOfNations[randint(0, listOfNations.__len__() - 1)]
    # 1.2. Gender
    charOptions["Gender"] = listOfGenders[randint(0, listOfGenders.__len__() - 1)]
    # 1.3. Name
    charOptions["Name"] = rando_name(charOptions["Nationality"], charOptions["Gender"])

    ### PRINT RANDOMIZED OPTIONS ###
    print("CHARACTER INFO:")
    for key in charInfoList:
        if key in charOptions.keys():
            print("\t{}:  {}".format(key, charOptions[key]))

    print("\n")














