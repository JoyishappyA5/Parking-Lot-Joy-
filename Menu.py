def display_menu():
  loadData()
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
