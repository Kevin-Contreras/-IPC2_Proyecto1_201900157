from xml.dom import minidom
from Nodo import *
class Dato:
  lista = Lista()
  def verificar(self,archivo):
    mayork=""
    mayorz =""
    datosMayoresy=""
    datosMayorx=""
    contadorParaX =0
    contadorParaXs =0
    contadorParay=0
    contador=0;
    mini = minidom.parse(archivo)
    nombres = mini.getElementsByTagName("matriz")
    y = mini.getElementsByTagName("dato")
    for xml in nombres:
      for dato in xml.childNodes:
        if(str(dato).find("dato")!=-1):
          mayork=mayork+dato.attributes["y"].value+","
          mayorz=mayorz+dato.attributes["x"].value+","
      Y = max(mayork[:-1].split(","),key=int)
      X = max(mayorz[:-1].split(","),key=int)
      datosMayoresy=datosMayoresy+str(Y)+","
      splity = datosMayoresy[:-1].split(",")
      datosMayorx = datosMayorx+str(X)+","
      splitx= datosMayorx[:-1].split(",")
      mayork=""
      mayorz=""
    datosMayoresy=""
    datosMayorx=""
    
    for matriz in splity:
      if(int(nombres[contador].attributes["n"].value)*int(nombres[contador].attributes["m"].value)== int(matriz)*int(splitx[contador])):
          for dato in range(int(matriz)*int(splitx[contador])):
            if(int(matriz)==contadorParaX):
              contadorParaXs=contadorParaXs+1
              print(str(contadorParaXs) +" FD")
            
            if(contadorParay==int(matriz)):
              contadorParay=0
            if(contadorParaX==int(matriz)):
              contadorParaX=0
            contadorParay=contadorParay+1
            contadorParaX=contadorParaX+1
           
          
            for interna2 in nombres[contador].childNodes:
              if(str(interna2).find("dato")!=-1):
                
                if(str(interna2.toxml()).find("x=\""+str(contadorParaXs)+"\""+" y=\""+str(contadorParay)+"\"")!=-1):
                    print(interna2.firstChild.nodeValue)
          contadorParaXs=0
          contadorParaX=0
          contadorParay=0
          
          
            
          
      else:
        print("LA MATRIZ " + nombres[contador].attributes["nombre"].value+" ES INCORRECTA SUS DIMENSIONES NO COINCIDEN")
      contador=contador+1

     
         
          
    
    