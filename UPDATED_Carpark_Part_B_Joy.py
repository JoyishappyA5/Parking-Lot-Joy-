# File: parking_lot_tracker_part_b.py
# Description: Tracks parking-bay occupancy using Classes - Object Oriented Coding
# Author: Joy Gong
# Date created: 11/16/2026

# Ckass Parking Bay
class ParkingBay:
  #Constructor
  # Purpose: Initialise parking bay object with a bay number, empty licence plate and an unoccupied state
  # Inputs: baynum (integer)
  # Outputs: initialised objects
  # Data types: integer, string, boolean value
  def __init__(self, baynum):
    self.__baynum = baynum
    self.__plate = ""
    self.__occupied = False
  
#Method: parkCar()
#Purpose: Occupy a free parking bay with a validated licence plate.
#Inputs: plate (string)
#Outputs: Boolean success status (True if successful, False otherwise)
#Data types: string, bool
  def parkCar(self, plate):
    
    if not isinstance(plate, str):
      return False
    
    plate = plate.strip()
    
    if not plate:
      return False
  
    if self.__occupied:
      return False
    else:
      self.__plate = plate 
      self.__occupied = True
      return True
    
   # Method: removeCar()
   # Purpose: Remove a vehicle from an occupied bay and reset its licence plate and occupancy state.
   # Inputs: None
   # Outputs: Boolean success status (True if successful, False if the bay is empty)
   # Data types: bool, string
  def removeCar(self):
    if not self.__occupied:
      return False
    else:
      self.__plate = ""
      self.__occupied = False
      return True

    # Method: isOccupied()
    # Purpose: Retrieve whether the parking bay is currently occupied.
    # Inputs: None
    # Outputs: Occupancy state (True if occupied, False otherwise)
    # Data types: bool
  def isOccupied(self):
    return self.__occupied
    
    # Method: getBayNumber()
    # Purpose: Retrieve the number identifying the parking bay.
    # Inputs: None
    # Outputs: Bay number (integer)
    # Data types: integer
  def getBayNumber(self):
    return self.__baynum

    # Method: getPlate()
    # Purpose: Retrieve the licence plate stored in the parking bay.
    # Inputs: None
    # Outputs: Licence plate (string; empty string if the bay is unoccupied)
    # Data types: string
  def getPlate(self):
    return self.__plate
#End of Class

#List of bays
lstBays = [
    ParkingBay(1),
    ParkingBay(2),
    ParkingBay(3),
    ParkingBay(4),
    ParkingBay(5)
]


# Function: findBay()
# Purpose: Find and return the parking bay object matching the specified bay number.
# Inputs: lstBays (list of ParkingBay objects), Baynum (integer)
# Outputs: Matching ParkingBay object, or None if no matching bay exists.
# Data types: list, ParkingBay, integer, NoneTypedef findBay(lstBays, Baynum):
def findBay(lstBays, Baynum):
  for bay in lstBays:
    if bay.getBayNumber() == Baynum:
      return bay
  return None

# Function: displayBay()
# Purpose: Display each parking bay's number, occupancy status and licence plate if occupied.
# Inputs: lstBays (list of ParkingBay objects)
# Outputs: Printed parking bay information (no explicit return value)
# Data types: list, ParkingBay, string, integer, bool, NoneType
def displayBay(lstBays):
  for bay in lstBays:
    if not bay.isOccupied():
      print(f"{bay.getBayNumber()}: unoccupied")
    else:
      print(f"{bay.getBayNumber()}: {bay.getPlate()}")

# Function: parkVehicle() 
# Purpose: Park a vehicle in the specified bay and return an appropriate success or error message. 
# Inputs: lstBays (list of ParkingBay objects), baynum (integer), carplate (string) 
# Outputs: Success message or error message (string) 
# Data types: list, ParkingBay, integer, string, bool
def parkVehicle(lstBays, baynum, carplate):
  carplate = carplate.strip()
  bay = findBay(lstBays, baynum) 
  if bay is None:
    return "Please enter a valid bay number"
  else:
    success = bay.parkCar(carplate)
    if success is True:
      return f"Successfully parked car with carplate {carplate} in bay {baynum}"
    else:
      return "Sorry, but the bay is already occupied or your carplate is invalid"

# Function: removeVehicle()
# Purpose: Remove a vehicle from the specified bay after checking that the bay exists, is occupied and contains the matching plate.
# Inputs: lstBays (list of ParkingBay objects), baynum (integer), carplate (string)
# Outputs: Success message or error message (string)
# Data types: list, ParkingBay, integer, string, bool
def removeVehicle(lstBays, baynum, carplate):
  bayn = findBay(lstBays, baynum)
  carplate = carplate.strip()
  if bayn != None:
    if carplate == bayn.getPlate() and bayn.isOccupied():
      removal = bayn.removeCar()
      if removal is True:
        return f"Successfully removed car {carplate} from bay {baynum}"
      else:
        return "Please check your information and try again"
    else:
      return f"sorry, your car doesn't seem to be parked at bay {baynum}"
  else:
    return "Please Enter a valid Baynumber"

# Function: loadData()
# Purpose: Load and validate saved parking data from Carpark.txt and restore the state of occupied parking bay objects.
# Inputs: Carpark.txt file
# Outputs: Updated parking bay objects; handles a missing file without crashing
# Data types: file, string, integer, bool, ParkingBay, list, NoneType
def loadData():
  try:
    with open("Carpark.txt", "r") as file:
      #for each line in the saved file
      for line in file:
        #removal of space and comma
        parts = line.strip().split(",")
        #check if there's 3 parts to it so error file doesn't gets recorded
        if len(parts) != 3:
          continue
        bayNum, plate, occupied = parts
        
         #checks if bay is integer
        try:
          bayNum = int(bayNum)
        except ValueError:
          continue
          
        #check if bay ecist
        bay = findBay(lstBays, bayNum)
        if bay is None:
          continue

        #in case there's space after the comma has been removed for the occupation state and plate
        occupied = occupied.strip()
        plate = plate.strip()
        if occupied not in ("True", "False"):
          continue
        occupied = (occupied == "True")

        #if occupied data is recorded, if not data is left blank
        if occupied:
          bay.parkCar(plate)
      
  except FileNotFoundError:
    pass  
    
# Function: saveData()
# Purpose: Save each parking bay's number, licence plate and occupancy state to Carpark.txt.
# Inputs: Current list of ParkingBay objects (lstBays, accessed globally)
# Outputs: Updated Carpark.txt file; no explicit return value
# Data types: list, ParkingBay, integer, string, bool, file, NoneType
def saveData():
  with open("Carpark.txt", "w") as file:
    for bay in lstBays:
      bayn = bay.getBayNumber()
      plate = bay.getPlate()
      occupied = bay.isOccupied()
      file.write(
        f"{bayn},{plate},{occupied}\n"
      )
  
# Function: main()
# Purpose: Display the menu and coordinate parking operations, vehicle removal, status display, occupancy totals and program exit.
# Inputs: User's menu choice and operation-specific input
# Outputs: Menu, prompts, status information, messages and occupancy totals
# Data types: string, integer, list, ParkingBay, bool, NoneType
def main():

    while True:
        print("")
        print("========================================")
        print("         PARKING LOT TRACKER")
        print("========================================")
        print("1. Display parking bays")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Occupancy state")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
            displayBay(lstBays)

        elif choice == "2":
            carp = input("what's your carplate: ")
            try:
              bayn = int(input("which bay do you wish to park in: "))
            except ValueError:
              print("please enter a valid bay number")
              continue
            print(parkVehicle(lstBays, bayn, carp))
            

        elif choice == "3":
            try:
              bayn = int(input("what's your bay number: "))
            except ValueError:
              print("Please enter an integer")
              continue
            carp = input("What's your car plate: ")
            print(removeVehicle(lstBays, bayn, carp))
            

        elif choice == "4":
          occupied_bays = 0
          for bay in lstBays:
            if bay.isOccupied():
              occupied_bays += 1
          unoccupied_bays = len(lstBays) - occupied_bays
          print(f"Total Bays: {len(lstBays)}")    
          print(f"Occupied Bays: {occupied_bays}")
          print(f"Unoccupied Bays: {unoccupied_bays}")

        elif choice == "5":
          saveData()
          break

        else:
            print("Invalid choice. Please try again.")

loadData()
main()
