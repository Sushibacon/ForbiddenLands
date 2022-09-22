from random import randint
classnumber = int(str(randint(1, 6)) + str(randint(1, 6)))
# print(classnumber)
race = ""


if classnumber <= 22:
    race = "Alderlander Human"
elif classnumber >= 23 and classnumber <= 31:
    race = "Aslene Human"
elif classnumber >= 32 and classnumber <= 34:
    race = "Ailander Human"
elif classnumber >= 35 and classnumber <= 41:
    race = "Half-Elf"
elif classnumber >= 42 and classnumber <= 44:
    race = "Halfling"
elif classnumber >= 45 and classnumber <= 52:
    race = "Goblin"
elif classnumber >= 53 and classnumber <= 56:
    race = "Orc"
elif classnumber >= 57 and classnumber <= 62:
    race = "Wolfkin"
elif classnumber >= 63 and classnumber <= 64:
    race = "Dwarf"
elif classnumber >= 65 and classnumber <= 66:
    race = "Elf"
else:
    race = "TryAgain"

print('The classnumber is: ' + str(classnumber) + '\n' + 'the race is: ' + race)
