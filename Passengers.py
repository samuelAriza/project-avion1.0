class Passengers:
  def __init__(self, name, id, assignment, age, status):
    self.name = name
    self.id = id
    self.age = age
    self.assignment = assignment
    self.status = status

  def getName(self):
    return self.name
    
  def getId(self):
    return self.id
    
  def getAssignment(self):
    return self.assignment

  def getStatus(self):
    return self.status
    
  def showPassenger(self):
    if(self.status == 1):
      str = "COMPRADO"
    else:
      str = "RESERVA"
    print("--------------------------------")
    print(f'-NOMBRE: {self.name} \n-ID:  {self.id}\n-EDAD : {self.age}\n-ASIGNACIÓN: {self.assignment} \n-ESTADO: {str}')
    print("--------------------------------")
    
