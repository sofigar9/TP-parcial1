
cantidad_paises = ["Argentina", "Brasil", "Francia", "España", "Italia"] 
"Argentina" = ["A"]
"Brasil" = ["B"]
"Francia" = ["F"]
"España" = ["E"]

compras_paises = [450, 720, 310, 1650, 890, 620, 1250, 230]

def menu ():
 print ("Menu: ")
 opcion = int(input("ingrese una opcion: "))
 print (
  "1: Cargar ventas"
  " 2: Mostrar ventas")
 while opcion == 1:
   for i in cantidad_paises :
    copias_vendidas = int(input("ingrese la cantidad de copias vendidas:"))

   match (opcion):
    case 2:  
     for i in len("A"):
      print (i)
     for i in len("B"):
      print (i) 
     for i in len("F"):
      print (i) 
     for i in len("E"):
      print (i) 
    case 3: 
       total_ventas = compras_paises * 0.10
       if copias_vendidas < total_ventas:
        print (cantidad_paises)

    case 4:    
      total_ventas = compras_paises * 0.10
      if copias_vendidas < total_ventas:
        print (cantidad_paises)


    case 6:
     for i in len(compras_paises):
      if compras_paises > 500:
       print(i)
        







  