import json,random

#Unused couldnt be arsed removing, it has too much emotional value to me.
usedNames = []

with open('first-names.json', 'r', encoding = "utf-8-sig") as outfile:
    data = json.load(outfile)

class Critter(object):
    """a virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nThe total number of critters is ", Critter.total)

    def __init__(self, name, colour):
        print("A critter is born, ", name)
        self.name = name
        self.colour = colour
        Critter.total += 1

#Main

print("Accessing the class attribute Critter.total: ", Critter.total)
print("creating critters: ")

for i in range(len(data)):
    # Gets a random name from a json file.
    index = random.randrange(len(data))
    crit = Critter(data[index], "Red")
    del data[index]

Critter.status()

input("press any key to exit...")