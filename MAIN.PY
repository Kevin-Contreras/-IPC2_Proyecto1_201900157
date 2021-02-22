class Menu:

  def menus():
    numero = 0;
    fichero="";
    while(True):
      print("*********************MENU********************")
      print("1) CARGAR ARCHIVO DE ENTRADA 2) PROCESAR ARCHIVO DE ENTRADA 3) ESCRIBIR ARCHIVO DE ENTRADA 4) DATOS DEL ESTUDIANTE 5) GENERAR GRAFICA 6) SALIR")
      print("SELECCIONE UNA OPCION DEL MENU")
      numeroMenu = input()
      casteoNumero = int(numeroMenu)
      if(casteoNumero == 1 ):
        print("opcion1")
      elif (casteoNumero == 2 ):
        print("opcion 2")
      elif(casteoNumero == 3):
        print("opcion 3")
      elif (casteoNumero == 4):
        
        
        print("NOMBRE: KEVIN ALEXIS LOPEZ CONTRERAS")
        print("CARNET: 201900157")
        print("CURSO: INTRODUCCION A LA PROGRAMACION 2")
        print("INGENIERIA EN CIENCIAS Y SISTEMAS")
        print("4TO SEMESTRE")

       
        
      elif casteoNumero ==5 :
        print("-----------------------DATOS INGRESADOS AL HTML ------------------------")
     
        print("------------------------------------------")
      elif casteoNumero == 6 :
        
        break

Menu.menus()



