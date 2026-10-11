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
      return f"Successfuly parked car with carplate {carplate} in bay {baynum}"
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
      for line in file:
        bayNum, plate, occupied = line.strip().split(",")
        bayNum = int(bayNum)
        occupied = occupied.strip()
        plate = plate.strip()
        if occupied == "True":
          occupied = True
        else:
          occupied = False
        if occupied is True:
          bay = findBay(lstBays, bayNum)
          if bay is not None:
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
        print("\nParking Lot Tracker")
        print("1. Display parking bays")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Save data")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayBay(lstBays)

        elif choice == "2":
            carp = input("what's your carplate?")
            try:
              bayn = int(input("which bay do you wish to park in?"))
            except ValueError:
              print("please enter a valid bay number")
              continue
            print(parkVehicle(lstBays, bayn, carp))
            

        elif choice == "3":
            try:
              bayn = int(input("what's your bay number?"))
            except ValueError:
              print("Please enter an integer")
              continue
            carp = input("What's your car plate?")
            print(removeVehicle(lstBays, bayn, carp))
            

        elif choice == "4":
          saveData()
          

        elif choice == "5":
          saveData()
          break

        else:
            print("Invalid choice. Please try again.")

loadData()
main()
