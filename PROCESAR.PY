from xml.dom import minidom
from Nodo import *
class Proceso():
  lista= Lista()
  lista2 = Lista()
  lista3 = Lista()
  def procesar(self,archivo):
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    

  def ordenar(self,archivo):
    numeros =""
    dato=1;
    multi=1
    docs = minidom.parse(archivo)
    items = docs.getElementsByTagName("dato")
    
    for item in items:
      y = item.attributes["y"].value
      x = item.attributes["x"].value
      self.lista3.insertar(int(item.firstChild.nodeValue))
  
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
   
  def incluir(self,archivo):
   
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    nuevo = self.lista2.recorrer()
    nuevo2 = self.lista2.recorrer()
    contador1 =0
    valor =""
    valor2 = ""
    valor3=""
    
    for id4 in items:
      w=id4.attributes["y"].value
    
    while nuevo2.siguinte:
        valor = valor + nuevo2.elemento()+"*"
        nuevo2 = nuevo2.siguinte
        contador1 = contador1 +1
        if(int(w) == contador1 ):
            break
    separado1 = valor.split("*")
    sin=separado1.pop(len(separado1)-1)
    
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
   
    asterisco = valor2.split("*")
    asterisco.pop(len(asterisco)-1)
    contadors=1
    contadors2=0
    numeror=0
    frecuencia=0
    orden =sorted( set(asterisco))
    asterisco = orden
 
 
    x=0;
    m=0
    for item in items:
      ds = item.attributes["x"].value
      dl=item.attributes["y"].value
      
    for da in asterisco:
      if(da.find(",")!=-1):
        datos = da.split(",")
        for item in range(int(ds)):
          for y in range(int(dl)):
            x=x+1
            if(da.find(str(x)) != -1):
              m =m+1
              
              numeror = numeror + int(self.lista3.getNodo(m))
              
            else:
              m=m+1;
          print(numeror)
          numeror=0;  
          x=0;
        m=0;
      else:
        print("")
          
              
              
          
          


   