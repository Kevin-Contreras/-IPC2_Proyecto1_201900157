from CARGAR import *
from PROCESAR import *
from ARCA import *
from COLOCAR import *
from DATOS import *
from Nombres import *
from GRAFICA import *

class Menu:
 
  def menus():
    m = Proceso()
    numero = 0;
    fichero="";
    while(True):
      print("*********************MENU********************")
      print("1) CARGAR ARCHIVO DE ENTRADA 2) PROCESAR ARCHIVO DE ENTRADA 3) ESCRIBIR ARCHIVO DE SALIDA 4) DATOS DEL ESTUDIANTE 5) GENERAR GRAFICA 6) SALIR")
      print("SELECCIONE UNA OPCION DEL MENU")
      numeroMenu = input()
      
      casteoNumero = int(numeroMenu)
      if(casteoNumero == 1 ):
        print("INGRESA EL NOMBRE DEL ARCHIVO ")
        documento = input()
        CargarDatos.cargar(documento)
        print("SE HA CARGADO EL ARCHIVO CON EXITO")
      elif (casteoNumero == 2 ):
        print("REALIZANDO LA MATRIZ BINARIA...........")
        print("REALIZANDO SUMA DE DUPLAS...........")
        Colocar().ordenarMatriz(CargarDatos.cargar(documento))
        m.ordenar(CargarDatos.cargar(documento))
       
      elif(casteoNumero == 3):
        print("INGRESA LA DIRECCION DEL ARCHIVO DE SALIDA ")
        salidaS = input()
        archivo().final(CargarDatos.cargar(documento),salidaS)

      elif (casteoNumero == 4):
        
        print("NOMBRE: KEVIN ALEXIS LOPEZ CONTRERAS")
        print("CARNET: 201900157")
        print("CURSO: INTRODUCCION A LA PROGRAMACION 2")
        print("INGENIERIA EN CIENCIAS Y SISTEMAS")
        print("4TO SEMESTRE")
      elif casteoNumero == 5 :
        Nombre().ordenarMatriz(CargarDatos.cargar(documento))
        Nombre().nombres()
        print("COLOQUE EL NUMERO DE LA MATRIZ QUE DESEA GRAFICAR")
        grafica = input()
        print("INGRESE LA RUTA DE SALIDA")
        ar = input()
        graf().graficas(CargarDatos.cargar(documento),grafica)
        graf().graficarMatriz(ar)

      elif casteoNumero == 6 :
        break

Menu.menus()

