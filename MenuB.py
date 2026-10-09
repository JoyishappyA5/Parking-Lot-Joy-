# creating a class for carpark
class ParkingBay:
  #Constructor
  def __init__(self, baynum):
    self.__baynum = baynum
    self.__plate = ""
    self.__occupied = False

  def parkCar(self, plate):
    if not isinstance(plate, str) or not plate.strip():
      print("Please enter valid carplate")
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
    if bay.getBaynumber() == Baynum:
      return Baynum
  return None
  
def displayBay(lstBays):
  for bay in lstBays:
    if not bay.isOccupied():
      print(f"{bay.getBayNumber()}: unoccupied")
    else:
      print(f"{bay.getBayNumber()}: {bay.getPlate()}")

def parkVehicle(lstBays, baynum, carplate):
  if findBay(lstBays, baynum) != None:
    parkCar(carplate)
  else:
    return "Enter a valid Baynumber please"
def removeVehicle(lstBays, baynum, carplate):
  if findBay(lstBays, baynum) != None:
    if carplate == baynum.getBayNumber:
      bay.removeCar()
      return f"Your car has been removed from bay {baynum}"
    else:
      return f"sorry, but your car doesn't seem to be parked at bay {baynum}}"
  else:
    return "Enter a valid Baynumber please"

def main():

    while True:
        print("\nParking Lot Tracker")
        print("1. Display parking bays")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Save data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayBay()
            pass

        elif choice == "2":
            carp = input("what's your carplate?")
            try:
              bayn = int(input("which bay do you wish to park in?"))
            except ValueError:
              print("please enter a valid bay number")
            parkVehicle(lstBays, bayn, carp)
            pass

        elif choice == "3":
            bayn = input("what's your bay number?")
            removeVehicle()
            pass

        elif choice == "4":
              
            pass

        elif choice == "5":
            # Save if required, then exit the loop
            break

        else:
            print("Invalid choice. Please try again.")


main()
