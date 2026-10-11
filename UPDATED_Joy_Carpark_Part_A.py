# File: parking_lot_tracker_part_a.py
# Description: Tracks parking-bay occupancy using a dictionary of dictionaries.
# Author: Joy
# Date created: 08/10/26

#Dictionary of the bays and their state
Bays = {
    1: {"plate": "", "occupied": False},
    2: {"plate": "", "occupied": False},
    3: {"plate": "", "occupied": False},
    4: {"plate": "", "occupied": False},
    5: {"plate": "", "occupied": False}
}

# Function: display_menu()
# Purpose: Display the menu and allow the user to select a parking operation until they choose to save and exit.
# Inputs: User's menu choice (integer)
# Outputs: Menu options, prompts and results of selected operations; no explicit return value.
# Data types: bool, int, NoneType
def display_menu():
    running = True
    #the different choices printed
    while running:
        print("========================================")
        print("         PARKING LOT TRACKER")
        print("========================================")
        print("Parking Lot Tracker")
        print("1. Entering a bay")
        print("2. Leaving a bay")
        print("3. View status of all bays")
        print("4. View occupancy totals")
        print("5. Save Data and Exit")
        print("========================================")
        action = int(input("Enter your choice: "))
        if action == 1:
            recordEntry()
        elif action == 2:
            removeCar()
        elif action == 3:
            viewStatus()
        elif action == 4:
            calculateTotals()
        elif action == 5:
            saveData()
            # exit()
            running = False



# Function: recordEntry()
# Purpose: Park a car in a specified bay if the bay number is valid and the bay is unoccupied.
# Inputs: Bay number (integer), car plate (string)
# Outputs: Confirmation message or error message; updates the corresponding bay's plate and occupancy state.
# Data types: int, string, bool, dict, NoneType
def recordEntry():
  bay = int(input("Enter bay number (1-5):"))
  if bay in Bays:
    if Bays[bay]["occupied"]:
        print("Bay is already occupied.")
   
        
    else:
        car_plate = input("Enter car number plate:").strip()
    if not car_plate:
        print("Invalid car plate. Please enter a valid car plate.")
    else:
        Bays[bay]["plate"] = car_plate
        Bays[bay]["occupied"] = True
        print(f"Car with plate {car_plate} has parked in bay {bay}.")
  else:
      print("Please enter a valid bay number")
      
# Function: removeCar()
# Purpose: Find a car by its registration plate and remove it from the parking bay if it exists in the system.
# Inputs: Car registration plate (string)
# Outputs: Removal confirmation or error message; updates the bay's plate and occupancy state when removal succeeds.
# Data types: string, bool, int, dict, NoneType
def removeCar():
    cp = input("Enter car number plate: ")
    found = False
    for bay, details in Bays.items():
        if details["plate"] == cp:
            print(f"you parked your car in {bay}")
            Bays[bay]["plate"] = ""
            Bays[bay]["occupied"] = False
            found = True
            print("Have a lovely day! Thank you for parking in xx parking")
            break
    if not found:
        print("we could not find your carplate in the system")
    #go back to menu after seeing the message

# Function: viewStatus()
# Purpose: Display the status of every parking bay, including its bay number and registration plate if occupied.
# Inputs: None (uses the global Bays dictionary)
# Outputs: Formatted parking bay status display; no explicit return value.
# Data types: dict, int, string, bool, NoneType
def viewStatus():
    print("========================================")
    print("CAR PARK STATUS")
    print("========================================")
    for bay in Bays:
        if Bays[bay]["occupied"]:
            status = Bays[bay]["plate"]
            print("┌───────────┐")
            print(f"│   BAY {bay}   │")
            print("│           │")
            print(f"│{status:^11}│")
            print("│           │")
            print("└───────────┘")
        else:
            status = "UNOCCUPIED"
            print("┌───────────┐")
            print(f"│   BAY {bay}   │")
            print("│           │")
            print(f"│{status:^11}│")
            print("│           │")
            print("└───────────┘")
    
    print("========================================")
        
# Function: calculateTotals()
# Purpose: Calculate and display the total number of bays, occupied bays and unoccupied bays.
# Inputs: None (uses the global Bays dictionary)
# Outputs: Printed occupancy totals; no explicit return value.
# Data types: int, dict, bool, NoneType       
def calculateTotals():
    occupied_bays = 0
    for bay in Bays:
        if Bays[bay]["occupied"]:
            occupied_bays += 1
    unoccupied = len(Bays) - occupied_bays
    print("Total: 5")
    print(f"occupied: {occupied_bays}")
    print(f"unoccupied: {unoccupied}")
  

# Function: saveData()
# Purpose: Save each parking bay's number, registration plate and occupancy state to Carpark.txt.
# Inputs: None (uses the global Bays dictionary)
# Outputs: Updated Carpark.txt file; no explicit return value.
# Data types: dict, int, string, bool, file, NoneType
def saveData():
    with open("Carpark.txt", "w") as file:
        for bayNum, details in Bays.items():
            file.write(
                f"{bayNum}, {details['plate']}, {details['occupied']}\n"
                )

# Function: loadData()
# Purpose: Read saved parking information from Carpark.txt and restore the bay data in the Bays dictionary.
# Inputs: Carpark.txt file
# Outputs: Updated Bays dictionary; handles a missing file without terminating the program.
# Data types: file, string, int, bool, dict, NoneType
def loadData():
    try:
        with open("Carpark.txt", "r") as file:
            for line in file:
                line = line.strip()
                bayNum, plate, occupied = line.split(",")
                bayNum = int(bayNum)
                occupied = occupied.strip()
                plate = plate.strip()
                if occupied == "True":
                             occupied = True
                else:
                    occupied = False
                Bays[bayNum] = {
                    "plate": plate,
                    "occupied": occupied}
    except FileNotFoundError:
        pass


loadData()
display_menu()
