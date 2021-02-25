from CARGAR import *
from PROCESAR import *
class Menu:

  def menus():
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
        Proceso().procesar(CargarDatos.cargar(documento))
        Proceso().ordenar(CargarDatos.cargar(documento))
        Proceso().incluir(CargarDatos.cargar(documento))
      elif(casteoNumero == 3):
        print("opcion 3")
      elif (casteoNumero == 4):
        
        print("NOMBRE: KEVIN ALEXIS LOPEZ CONTRERAS")
        print("CARNET: 201900157")
        print("CURSO: INTRODUCCION A LA PROGRAMACION 2")
        print("INGENIERIA EN CIENCIAS Y SISTEMAS")
        print("4TO SEMESTRE")
      elif casteoNumero == 5 :
        print("D")
      elif casteoNumero == 6 :
        break

Menu.menus()

"""
cod = cod + int(dato)
            d = cod-1
            numeror = numeror+str(self.lista3.getNodo(d))+"*"
"""