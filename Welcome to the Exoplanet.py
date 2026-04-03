import csv
import time

print("*" * 50)
print("     EXOPLANET TERMINAL PROJECT      ")
print("*" * 50)
time.sleep(2) 
'''delay makes it look cool and like its actually thinking'''

# We opening the planet list with this one(block of code)
planet_list = []
file = open("Exoplanet.csv", "r")
reader = csv.reader(file)

for row in reader:
    planet_list.append(row)

file.close()

header = planet_list.pop(0)

while True:
    print("\n--- MAIN MENU ---")
    print("1. Search for a planet")
    print("2. Find habitable planets")
    print("3. Average mass of all planets")
    print("4. Exit")

    ch = input("Enter your choice (1-4): ")

    if ch == '1':
        name = input("Enter planet name to search: ")
        print("Searching...")
        time.sleep(1)

        found = 0
        for p in planet_list:
            if name.lower() in p[0].lower():
                print("\nPlanet Found!")
                print("Name:", p[0])
                print("Distance:", p[1], "Lightyears")
                print("mass:", p[2], "Jupiters")
                print("Habitable:", p[4])
                found = 1

        if found == 0:
            print("Sorry, planet not in database.")

    elif ch == '2':
        print("\nSanning for habitable worlds...")
        time.sleep(1)
        count = 0

        for p in planet_list:
            if p[4].strip().lower() == "yes":
                print("-", p[0], "is", p[1], "LY away")
                count = count + 1
    
        print("Total habitable planets found:", count)

    elif ch == '3':
        print("\nCalculating average mass...")
        time.sleep(1)

        total = 0.0
        planets_counted = 0

        for p in planet_list:
            try:
                m = float(p[2])
                total = total + m
                planets_counted = planets_counted + 1
            except:
                pass

        avg = total/planets_counted
        print("Analyzed", planets_counted, "planets.")
        print("Average Mass is:", round(avg, 2), "Jupiters")

    elif ch == '4':
        print("Exiting terminal...")
        time.sleep(1)
        break

    else:
        print("Invalid input! Try again.")