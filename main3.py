import csv
import time
import random

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
    print("4. Random Planet of the Day")
    print("5. Exit")

    ch = input("Enter your choice (1-5): ")

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

        report_lines=[]

        for p in planet_list:
            if p[4].strip().lower() == "yes":
                line = "- " + p[0] + "is" + str(p[1]) + " LY away"
                print(line)
                report_lines.append(line)
                count = count + 1
        
        print("Total habitable planets found:", count)

        print("\nWould you like to export this list to a text file?")
        export_choice = input("Enter Y for Yes, or N for No: ")

        if export_choice.lower() == 'y':
            print("Exporting data...")
            time.sleep(1)

            out_file = open("Habitable_Report.txt", "w")
            
            out_file.write("HABITABLE PLANETS REPORT\n")
            out_file.write("========================\n")

            for item in report_lines:
                out_file.write(item + "\n")
            out_file.write("\nTotal planets found: " + str(count) + "\n")

            out_file.close()

            print("Done! Data successfully saved to Habitable_Report.txt")

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
        print("\nCalculating random hyperspace coordinates...")
        time.sleep(1.5)

        rp = random.choice(planet_list)

        print("n" + "*" * 35)
        print("     RANDOM PLANET OF THE DAY     ")
        print("*" * 35)
        print("Name:", rp[0])
        print("Distance:", rp[1], "Lightyears")
        print("Mass:", rp[2], "Jupiters")
        print("Habitable:", rp[4])
        print("*" * 35)
    elif ch == '5':
        print("Exiting terminal...")
        time.sleep(1)
        break

    else:
        print("Invalid input! Try again.")
