# creating a class for carpark
class ParkingBay:
  #Constructor
  def __init__(self, baynum):
    self.__baynum = baynum
    self.__plate = ""
    self.__occupied = False
  
#Methods for parking/removing car and returning True/False
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
    

  def removeCar(self):
    if not self.__occupied:
      return False
    else:
      self.__plate = ""
      self.__occupied = False
      return True

  #Methods for retrieving informations
  def isOccupied(self):
    return self.__occupied

  def getBayNumber(self):
    return self.__baynum

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


#functions
def findBay(lstBays, Baynum):
  for bay in lstBays:
    if bay.getBayNumber() == Baynum:
      return bay
  return None
  
def displayBay(lstBays):
  for bay in lstBays:
    if not bay.isOccupied():
      print(f"{bay.getBayNumber()}: unoccupied")
    else:
      print(f"{bay.getBayNumber()}: {bay.getPlate()}")

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

#Loading and Saving Funtioons
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
    

def saveData():
  with open("Carpark.txt", "w") as file:
    for bay in lstBays:
      bayn = bay.getBayNumber()
      plate = bay.getPlate()
      occupied = bay.isOccupied()
      file.write(
        f"{bayn},{plate},{occupied}\n"
      )
  
#Menu function
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
