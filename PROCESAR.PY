from xml.dom import minidom
from Nodo import *
class Proceso():
 
  lista= Lista()
  def procesar(self,archivo):
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    
    for item in items:
      self.lista.insertar(item.firstChild.nodeValue)
      
      
        
  def ordenar(self,archivo):
    numeros =""
    cadena=[]
    dato=0;
    docs = minidom.parse(archivo)
    items = docs.getElementsByTagName("dato")
   
    print(len(items))
    for item in items:
      y = item.attributes["y"].value
    for item in range(int(y)):
      for d in items :
        if(d.attributes["y"].value == items[item].attributes["y"].value):
          if(int(d.firstChild.nodeValue) != 0 ):
            d.firstChild.nodeValue= 1
            print(d.firstChild.nodeValue)
          else:
            
            print(d.firstChild.nodeValue)
            
    
