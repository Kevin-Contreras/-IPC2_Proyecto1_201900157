from xml.dom import minidom
from Nodo import *
class Proceso():
 
  lista= Lista()
  lista2 = Lista()
  def procesar(self,archivo):
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    
  def ordenar(self,archivo):
    numeros =""
    cadena=[]
    dato=1;
    multi=1
    docs = minidom.parse(archivo)
    items = docs.getElementsByTagName("dato")
    print(len(items))
    for item in items:
      y = item.attributes["y"].value
      x = item.attributes["x"].value
    for item in range(int(y)):
      for d in items :
        if(d.attributes["y"].value == items[item].attributes["y"].value):
          if(int(d.firstChild.nodeValue) != 0 ):
            d.firstChild.nodeValue= 1
            self.lista.insertar(d.firstChild.nodeValue)
          else:
            self.lista.insertar(d.firstChild.nodeValue)
    o = self.lista.recorrer()
    while o.siguinte :
      numeros = numeros + str(o.elemento())+","
      if(dato == multi*int(x) ):
        numero2 = numeros[:-1]
        multi=multi+1
        
        numeros=""
        self.lista2.insertar(numero2)
        if(dato == len(items)):
          break
      o = o.siguinte
      dato = dato+1      
    
  def incluir(self):
    nuevo = self.lista2.recorrer()
    nuevo2 = self.lista2.recorrer()
    contador1 =0
    valor =""
    valor2 = ""
    valor3=""
    while nuevo2.siguinte:
        valor = valor + nuevo2.elemento()+"*"
        nuevo2 = nuevo2.siguinte
        contador1 = contador1 +1
        if(4 == contador1 ):
          break
    separado1 = valor.split("*")
    sin=separado1.pop(len(separado1)-1)
    print(sin)
    n =0;
    for sepa in separado1:
      for sepa2 in separado1:
        if(sepa2==sepa):
          n=n+1 
          valor2 = valor2 +str(n)+","
        else:
          n=n+1
      n=0
      valor2=valor2[:-1]+"*"
    print(valor2)
    asterisco = valor2.split("*")
    asterisco.pop(len(asterisco)-1)
    print(asterisco)
    orden =sorted( set(asterisco))
    asterisco = orden
    print(asterisco)

    
   