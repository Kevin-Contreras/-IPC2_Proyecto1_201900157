from xml.dom import minidom
from Nodo import *
class Colocar :
  letras=""
  def ordenarMatriz(self,datow):
    n ="";
    h=0;
    h2=0
    po=0
    contador=0
    m=""
    mini = minidom.parse(datow)
    nombres = mini.getElementsByTagName("matriz")
    datos = mini.getElementsByTagName("dato")
    nombres2 = mini.getElementsByTagName("matriz")
    for nom in range(len(nombres)):
     n = n+nombres[nom].attributes["nombre"].value+","
     d = n[:-1]
     y = d.split(",")
    y = list(dict.fromkeys(y))
    for u in y :
      for nomd in nombres:
        if(u == nomd.attributes["nombre"].value):
          if(h == 0):
            m=m+str(h2)+","
          po=po+1
          h=h+1;
        else:
          h2=h2+1
        
      h=0
      h2=0
      i=0;
    letras = m[:-1].split(",")
    return letras
  
    

    
    