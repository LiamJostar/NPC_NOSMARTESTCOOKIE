import random
gender = input("Male or Female? ").strip().lower()
race = input("Enter race (human, elf, dwarf): ").strip().lower()
human_male = ["George", "John", "Tim", "Tom", "Bob", "Gerald", "Joe", "Jim", "Mark", "Edward", "Nathan", "Arthur"]
human_female = ["Ann", "Mary" , "Laura", "Erin", "Betsy", "Catherine", "Dawn"]
elf_male = ["Ruithain", "Sinduril", "Legolas", "Lorian", "Tidurrel"]
elf_female = ["Amenth", "Solyn", "Galendreth", "Murthera", "Wendryll"]
dwarf_male = ["Glorin", "Dorin", "Borin", "Kili", "Fili", "Bombur", "Oin", "Gloin", "Durthrang", "Garth"]
dwarf_female = ["Clergh", "Melva", "Bronth", "Syndar", "Glorbyth"]
print()
print(race)
if race == "human":
    if gender == "male":
        print(random.choice(human_male))
    elif gender == "female":
        print(random.choice(human_female))
    else:
        print("Unknown gender.")
elif race == "elf":
    if gender == "male":
        print(random.choice(elf_male))
    elif gender == "female":
        print(random.choice(elf_female))
    else:
        print("Unknown gender.")
elif race == "dwarf":
    if gender == "male":
        print(random.choice(dwarf_male))
    elif gender == "female":
        print(random.choice(dwarf_female))
    else:
        print("Unknown gender.")
else:
    print("Unknown race.")
print()
print("Characteristics: ")
strength = ["Strong", "Weak", "Decent"]
experience = ["Experienced", "New", "Decent"]
hp = ["High", "Low", "Decent"]
print("Strenth = ", random.choice(strength))
print("Experience = ", random.choice(experience))
print("Hp= ", random.choice(hp))
print()
print("Personality: ")
personalities = ["Sassy", "Brooding", "Surly", "Nerdy", "Hyper", "Rude", "Adventurous", "Lazy", "Arrogant", "Charming", "Mysterious", "Stubborn"]
print(random.choice(personalities))
targeting = ["Nuetral", "Agressive", "Passive"]
print(random.choice(targeting))