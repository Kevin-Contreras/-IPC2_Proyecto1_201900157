from xml.dom import minidom
from Nodo import *
class Dato:
  lista = Lista()
  def verificar(self,archivo):
    contador=0
    contador2=0
    contador3=0
    atri=""
    v=0
    atri2=""
    f=""
    contador3 =0
    mini = minidom.parse(archivo)
    nombres = mini.getElementsByTagName("matriz")
    y = mini.getElementsByTagName("dato")
    for xml in nombres:
      for dato in xml.childNodes:
        if(str(dato).find("dato")!=-1):
          contador=contador+1
      contador2=contador2+1
      contador=0
    
    for nombre in nombres:
      for n in nombre.childNodes:
        if(str(n).find("dato")!=-1):
            
          atri = atri+n.attributes["y"].value+","
      dd =max(atri[:-1].split(","))
      f=f+dd+","
      pi=f[:-1].split(",")
      atri=""
    print(pi)
    for nombre in nombres:
      for r in range(6):
        for n in nombre.childNodes:
          if(str(n).find("dato")!=-1):
            cadena = "y=\""+str(r+1)+"\""
            if(str(n.toxml()).find(cadena)!=-1):
              """print(n.firstChild.nodeValue)"""
              