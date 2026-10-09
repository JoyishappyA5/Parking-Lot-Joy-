class ParkingBay:
  def __init__(self, baynum):
    self.__baynum = baynum
    self.__plate = ""
    self.__occupied = False

  def parkCar(self, plate):
    self.__plate = plate
    if not plate.strip():
      print("Please enter valid carplate")
      return False

    if self.__occupied:
      return False
    else:
      self.__occupied = True
      return True
    

  def removeCar(self):

  def isOccupied(self):
    return self.__occupied

  def getBayNumber(self):
    return self.__baynum

  def getPlate(self):
    return self.__plate
