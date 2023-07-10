#creativos.cl

menu = int(input(""""
1.comprar entradas
2.mostrar ubicaciones disponibles 
3. ver listado de asistentes 
4.mostrar ganancias totales 
5.salir
  selecciona una opcion:
"""))



asientosplatinum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
asientosgold = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
asientossilver = [51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
listaasientosdisponibles =[asientosplatinum , asientosgold, asientossilver]
listaasientosnodisponibles = []
listaasistentes = []



#1
def comprar_entradas():
    while True:
            try:
                if menu == 1:
                    print(f"asientos disponibles {listaasientosdisponibles}")
                    print("--------------------------------------------------")
                    print("""valor por entrada:
                      platinum  del 1 al 20  $120.000
                      gold del 21 al 50 $80.000
                      silver del 51 al 100 $50.000
                      ----------------------------------------------------
                      """)
                    entrada = input("eliga numero de entradas")
                if entrada == listaasientosdisponibles:
                    listaasientosdisponibles = listaasientosnodisponibles
                    break
            except:("a ocurrido un error ")

#2
def mostrar_ubicacion():
    while True:
            try:
                print(f"asientos disponibles{listaasientosdisponibles}")
                print("----------------------------------------------------")
                print(f"asientos no disponibles{listaasientosnodisponibles}")
                break
            except:("ocurrio un problema")
#3
def listado_asistentes():
     while True:
            try:
                 print ({listaasistentes},{listaasientosnodisponibles})
                 
            except:("a ocurrido un error")
#4   
def ganancias_totales(menu):
     while True:
          try: 
               if menu == 4:
                    print (listaasientosnodisponibles)
               print ( "ganancias platinum "),(20* 120000 )
               print ("ganancias gold " ),(30 * 80000)
               print ("ganancias silver "),(50 * 50000)
          except:("a ocurrido un error")
   
#menu
def menu(opc):
    while True:
        try:
            if opc == 1:
                comprar_entradas()
                break
            elif opc == 2:
                mostrar_ubicacion()
                break
            elif  opc == 3:
                listado_asistentes()
                break
            elif  opc == 4:
                ganancias_totales()
                break
            elif opc == 5:
                print("cristian caceres 10/07/2023")
                break
            else:("a ocurrido un error ")
        except:("a ocurrido una exepcion")


