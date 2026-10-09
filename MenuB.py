class ParkingBay:
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

lstBays = [
    ParkingBay(1),
    ParkingBay(2),
    ParkingBay(3),
    ParkingBay(4),
    ParkingBay(5)
]

def findBay(lstBays, Baynum):
  for bay in lstBays:
    if bay.getBaynumber() == Baynum:
      return getBayNumber
  return None
  
def displayBay(lstBays):
  for bay in lstBays:
    if not bay.isoccupied():
      print(f"{bay.getBaynumber()}: unoccupied")
    else:
      print(f"{bay.getBaynumber()}: {bay.getplate()}")

def parkVehicle(lstBays, baynum, carplate):
  if findBay(baynum) != none:
    parkCar(carplate)
  else:
    return "Enter a valid Baynumber please"
  
