#Dictionary of the bays and their state
Bays = {
    1: {"plate": "", "occupied": False},
    2: {"plate": "", "occupied": False},
    3: {"plate": "", "occupied": False},
    4: {"plate": "", "occupied": False},
    5: {"plate": "", "occupied": False}
}

#Menu function
def display_menu():
  loadData()
#the different choices printed
  print("Parking Lot Tracker")
  print("1. Entering a bay")
  print("2. Leaving a bay")
  print("3. View status of all bays")
  print("4. View occupancy totals")
  print("5. Save Data and Exit")
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



#record entry option function
def recordEntry():
  bay = int(input("Enter bay number (1-5):"))
  if bay in Bays:
    if Bays[bay]["occupied"]:
      print("Bay is already occupied.")
    else:
      car_plate = input("Enter car number plate:")
      Bays[bay]["plate"] = car_plate
      Bays[bay]["occupied"] = True
      print(f"Car with plate {car_plate} has parked in bay {bay}.")

#function to remove a car from a bay 
def removeCar():
    cp = inpuit("Enter car number plate: ")
    for bay, details in Bays.items():
    if details["plate"] == plate:
        print(f"you parked your car in {bay}")
        Bay[bay]["plate"] = ""
        Bays[bay]["occupied"] = False
        print("Have a lovely day! Thank you for parking in xx parking")
    else:
        print("we could not find your carplate in the system")
        display_menu()
    
        
