import os
os.system("cls")



SelecUB = []
UbicacionE = range (1,101)
ListaAsistente = []
ListaEntrada = []
ListaEscenario = 1,2,3,4,'x',6,7,'x',9,10
11,12,13,14,15,16,17,18,19
20,21,22,23,24,25,26,27,28,29
30,31,32,33,34,35,36,37,38,39 
40,41,42,43,44,45,46,47,48,49
50,51,52,53,54,55,56,57,58,59
60,61,62,63,64,65,66,67,68,69
70,71,72,73,74,75,76,77,78,79
80,81,82,83,84,85,86,87,88,89
90,91,92,93,94,95,96,97,98,99,100


from datetime import date
fecha_actual = date.today()         
nombre = (input("Ingrese su nombre: "))
apellido = input("Ingrese su apellido: ")

precio = '''
----------------------------------------------
Precio de Entrada                            |
---------------------------------------------|
-Platinum $120.000 [Asientos del 1 al 20]    |
-Gold     $80.000  [Asientos del 21 al 50]   |
-Silver   $50.000  [Asientos del 51 al 100]  |
---------------------------------------------|
'''



escenario = """
###########ESCENARIO###########
1  2  3  4  x  6  7  x  9 10
11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 
40 41 42 43 44 45 46 47 48 49
50 51 52 53 54 55 56 57 58 59
60 61 62 63 64 65 66 67 68 69
70 71 72 73 74 75 76 77 78 79
80 81 82 83 84 85 86 87 88 89
90 91 92 93 94 95 96 97 98 99 100
#################################"""



menu = """
Menu
1) Comprar Entradas
2) Mostrar ubicaciones disponibles
3) Ver listado de asistentes
4) Mostrar ganancias totales
5) Salir
Digite Opcion: """



def comprarE ():
    while True:
        try:
            entrada = int(input('Ingrese cantidad de entradas: '))
            for i in range (1,101):
               print(i)
            if i in UbicacionE:
                print(f"Asiento {i}: Disponible")
            elif i in UbicacionE:
                print(f"Asiento {i}: No Disponible")
            if entrada <= 3 and entrada >= 1:
                for i in range (entrada):
                    SelecUB = int(input("Selecioe Ubicacion: "))
                break
        except:
            print("Ocurrio una expecion")
       

def UbicacionesD ():
     print(escenario)


def listadoA ():
     print("")


while True:
    try:
        opc = int(input(menu))
        if opc == 5:
            print(f'''
            Hasta Luego {nombre} {apellido}
            Fecha de Salida del sistema {fecha_actual}''')
            break
        elif opc == 1:
            comprarE()
        elif opc == 2:
            UbicacionesD()    
        elif opc == 3:
            listadoA()
        elif opc == 4:         
            print = (f""" 
                |Tipo Entrada       | Cantidad |    Total   |
                |-------------------------------------------|
                | Platinum $120.000 |        |          |
                |-------------------------------------------|              
                | Gold $80.000      |        |          |
                |-------------------------------------------|               
                | Silver $50.000    |        |          | 
                |-------------------------------------------|
                |  TOTAL            |        |          |
                |-------------------------------------------|
                """)
            break
    except:
        print("Ocurrio una excepcion")

