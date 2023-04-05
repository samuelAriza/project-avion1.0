import random
from Generator import *
from Passengers import *

def asignar(name, id, row, col, age, status):
  (x,y) = location(row, col)
  passenger = Passengers(name, id, (row, col), age, status)
  if (plane[x][y] == 0):
    plane[x][y] = passenger
    if(status == 1):
       pasajeros_comprado.append(passenger)
    else:
      pasajeros_reservado.append(passenger)
  else:
    print("OCUPADO")
  

def asignar_bebida():
  print("----------------------------------")
  print("Orden de asignación de bebidas\n")
  orden_bebida = []
  for i in range(0, 23):
    num = 5
    for j in range(0,6):
      if(j > 2):
        if(plane[i][num] != 0):
          if(plane[i][num].getStatus() == 1):
            orden_bebida.append(plane[i][num].getAssignment())
            num = num - 1
          else:
            num = num - 1
          
        else:
          num = num - 1
      else:
        if(plane[i][j] != 0):
          if(plane[i][j].getStatus() == 1):
            orden_bebida.append(plane[i][j].getAssignment())
  return orden_bebida

def asignar_comida():
  orden_comida = []
  print("----------------------------------")
  print("Orden de asignación de comida\n")
  i = 22
  while(i >= 0):
    num = 5
    for j in range(0,6):
      if(j > 2):
        if(plane[i][num] != 0):
          if(plane[i][num].getStatus() == 1):
            orden_comida.append(plane[i][num].getAssignment())
            num = num - 1
          else:
            num = num - 1
          
        else:
          num = num - 1
      else:
        if(plane[i][j] != 0):
          if(plane[i][j].getStatus() == 1):
            orden_comida.append(plane[i][j].getAssignment())
    i = i - 1
  return orden_comida
        
def dispose_plane():
  #Hacer el avion disponible
  for i in range(0, 23):
    col = []
    for j in range(0, 6):
      col.append(0)
    plane.append(col)

def mostrar_matriz():
  #Mostrar matriz
  count_row = 5
  count_col = 0
  print("------------ Airbus 320 ----------")
  l = ["A", "B", "C", "H", "J", "K"]
  for i in range(0, 23):
    stdout = ""
    for j in range(0, 6):
      if(plane[i][j] != 0):
        stdout += f'|{l[j]}:{str(plane[i][j].getStatus())}|'
        count_col = count_col + 1
      else:
        stdout+=f'|{l[j]}:0|'
    print(f'{count_row} : {stdout}')
    count_row = count_row + 1
  print("----------------------------------")

def set_up(num_passenger):
  count_passengers = 0
  while(count_passengers < num_passenger):
    (f, s) = assignment()
    (x, y) = location(f, s)
    if(plane[x][y] == 0):
      passenger_name = random_name()
      passenger_id = random.randint(0, 1000)
      passenger_assignment = (f, s)
      passenger_age = random.randint(1, 100)
      passenger_status = random.randint(1, 2)
      passenger = Passengers(passenger_name, passenger_id, passenger_assignment, passenger_age, passenger_status)
      plane[x][y] = passenger
      count_passengers = count_passengers + 1
      if (passenger.getStatus() == 1):
        pasajeros_comprado.append(passenger)
      elif (passenger.getStatus() == 2):
        pasajeros_reservado.append(passenger)
      pasajeros_general.append(passenger)

def order(list):
  pasajeros_nombre  = []
  datos = []
  for passenger in list:
    pasajeros_nombre.append(passenger.getName())
  pasajeros_ordenado = sorted(pasajeros_nombre)
  
  for name in pasajeros_ordenado:
    for i in range(len(list)):
      if(name ==list[i].getName()):
        datos.append(list[i])
  for dt in datos:
    dt.showPassenger()
    
if __name__ == '__main__':
  
  plane = []
  pasajeros_general = []
  pasajeros_comprado = []
  pasajeros_reservado = []
  dispose_plane()
  set_up(6)
  
  state = True
  mostrar_matriz()
  while(state):
    number_user = int(input("1. Datos pasajero\n2. Lista de pasajeros por orden alfabético\n3. Lista de pasajeros en espera por orden alfabético\n4. Todos los datos\n5. Ver asientos vendidos, libres y reservados\n6. Lista del orden de reparticion de las bebidas\n7. Ingresar un pasajero\n8. Lista del orden de repartición de las comidas\n"))
    diC = {"A":0, "B":1, "C":2, "H":3, "J":4, "K":5}
    match number_user:
      case 1:
        fila = int(input("- Ingrese la fila asignada:\n "))
        columna = input("- Ingrese la columna asignada:\n ")
        print(plane[fila - 5][diC[columna]].showPassenger())
      case 2: 
        order(pasajeros_comprado)

      case 3:
        order(pasajeros_reservado)
      case 4:
        order(pasajeros_general)
      case 5:
        dicSilla = {0:"A", 1:"B", 2:"C", 3:"H", 4:"J", 5:"K"}
        count_dispose = []
        count_reser = []
        count_vend = []

        for i in range(0, 23):
          for j in range(0, 6):
            str = f'{i + 5} : {dicSilla[j]}'
            if (plane[i][j] == 0):
              count_dispose.append(str)
            elif (plane[i][j].getStatus() == 1):
              count_vend.append(str)
            else:
              count_reser.append(str)
        print("--------------------------------")
        print("Asientos disponibles: \n")

        count_row = 5
        count_col = 0
        l = ["A", "B", "C", "H", "J", "K"]
        for i in range(0, 23):
          stdout = ""
          for j in range(0, 6):
            if(plane[i][j] == 0):
              stdout += f'| {l[j]} |'
              count_col = count_col + 1
          print(f'{count_row} : {stdout}')
          count_row = count_row + 1
            
            
        
        print("--------------------------------")
        print("Lista de asientos reservados: \n")
        print(count_reser)
        print("--------------------------------")
        print("Lista de asientos comprados: \n")
        print(count_vend)
        print("\n")
      case 6:
        print(asignar_bebida())
        print("\n")
      case 7:
        name = input("- Ingrese el nombre:\n ")
        id = int(input("- Ingrese el id\n "))
        row = int(input("- Ingrese la fila\n "))
        col = input("- Ingrese la columna\n ")
        edad = int(input("- Ingrese la fila\n "))
        status = int(input("- Ingrese el estado(1. Compra 2. Reserva)\n "))
        asignar(name, id, row, col, edad, status)
        mostrar_matriz()
      case 8:
        print(asignar_comida())
        print("\n")
        
    


  
  



  

