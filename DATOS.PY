from xml.dom import minidom
from Nodo import *
from COLOCAR import *
class Dato:
  lista = Lista()
  lista2 = Lista()
  listaY = Lista()
  listaX = Lista()
  listaContador = Lista()
  listal = Lista()
  sinRepetir = Colocar()
  def verificar(self,archivo):
    mayork=""
    mayorz =""
    datosMayoresy=""
    datosMayorx=""
    contadorParaX =0
    contadorParaXs =0
    contadorParay=0
    contador=0;
    contadore=0
    iterar=0
    mini = minidom.parse(archivo)
    nombres = mini.getElementsByTagName("matriz")
   
    y = mini.getElementsByTagName("dato")
  
    for sin in self.sinRepetir.ordenarMatriz(archivo):
      for dato in nombres[int(sin)].childNodes:
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
      if(int(nombres[contador].attributes["n"].value)*int(nombres[contador].attributes["m"].value) == int(matriz)*int(splitx[contador])):
          iterar=iterar+1
          self.listaY.insertar(matriz)
          self.listaX.insertar(splitx[contador])
          for dato in range(int(matriz)*int(splitx[contador])+int(matriz)):
            if(int(matriz)==contadorParaX):
              contadorParaXs=contadorParaXs+1
          
            
            if(contadorParay==int(matriz)):
              contadorParay=0
            if(contadorParaX==int(matriz)):
              contadorParaX=0
            contadorParay=contadorParay+1
            contadorParaX=contadorParaX+1
            for interna2 in nombres[contador].childNodes:
              if(str(interna2).find("dato")!=-1):
                if(str(interna2.toxml()).find("x=\""+str(contadorParaXs)+"\""+" y=\""+str(contadorParay)+"\"")!=-1):
                    
                    self.lista.insertar(interna2.firstChild.nodeValue)
                    contadore=contadore+1
          
          self.listaContador.insertar(contadore)
          contadore=0
          contadorParaXs=0
          contadorParaX=0
          contadorParay=0
          contador=contador+1
 
      else:
        print("LA MATRIZ " + nombres[contador].attributes["nombre"].value+" ES INCORRECTA SUS DIMENSIONES NO COINCIDEN")
        contador=contador+1

    self.listal.insertar(iterar)
    
          
    
  def y(self):
    return self.listaY
  def x(self):
    return self.listaX 
  def contador(self):
    return self.listaContador
  def iterar (self):
    return self.listal
  def datos(self):
    return self.lista
  def datosEliminar(self):
    self.lista.eliminar()
  def contadorEliminar(self):
    self.listaContador.eliminar()
  def iterarEliminar(self):
    self.listal.eliminar()
  def xeliminar(self):
    self.listaX.eliminar()