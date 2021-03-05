from xml.dom import minidom
from Nodo import *
from DATOS import * 
class Proceso():
 
  lista= Lista()
  lista2 = Lista()
  lista3 = Lista()
  g = Dato()
  def procesar(self,archivo):
    print(self.g.contador().mostrar())
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
 
  def ordenar(self,archivo):
    numeros =""
    datod=1;
    multi=1
    contador=1
    contadoree=0
    contadoree3=0
    self.g.verificar(archivo)
    iterars = self.g.iterar().getNodo(1)
    docs = minidom.parse(archivo)
    items = docs.getElementsByTagName("dato")
    
    for u in range(int(iterars)):
      for i in range(self.g.contador().getNodo(u)+1):
        self.lista3.insertar(self.g.datos().getNodo(i))
      print(self.lista3.mostrar())
      
      for de in range(int(self.g.y().getNodo(u))):
        for ud in range(int(self.g.y().getNodo(u))*int(self.g.x().getNodo(u))):
          contadoree=contadoree+1
          contadoree3=contadoree3+1
          if(contadoree3 == de+1):
            if(int(self.g.datos().getNodo(contadoree)) != 0 ):
              self.lista.insertar(1)
            else:
              self.lista.insertar(self.g.datos().getNodo(contadoree))
          
          if(contadoree3==int(self.g.y().getNodo(u))):
            contadoree3=0
          
        contadoree=0
        
      o = self.lista.recorrer()
      while o.siguinte :
        numeros = numeros + str(o.elemento())+","
        if(datod == multi*int(self.g.x().getNodo(u)) ):
          numero2 = numeros[:-1]
          multi=multi+1
        
          numeros=""
          self.lista2.insertar(numero2)
          if(datod == self.g.contador().getNodo(u+1)):
            break
        o = o.siguinte
        datod = datod+1      
      self.lista2.mostrar()


  def incluir(self,archivo):
    self.g.verificar(archivo)
    iterars = self.g.iterar().getNodo(1)
   
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    nuevo = self.lista2.recorrer()
    nuevo2 = self.lista2.recorrer()
    contador1 =0
    valor =""
    valor2 = ""
    valor3=""
    for i in range(int(iterars)): 
     
    
      while nuevo2.siguinte:
          valor = valor + nuevo2.elemento()+"*"
          nuevo2 = nuevo2.siguinte
          contador1 = contador1 +1
          if(int(self.g.y().getNodo(i)) == contador1 ):
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
 
      print(asterisco)
      x=0;
      m=0
      for da in asterisco:
        if(da.find(",")!=-1):
          datos = da.split(",")
          for item in range(int(self.g.x().getNodo(i))):
            for y in range(int(self.g.y().getNodo(i))):
              x=x+1
              if(da.find(str(x)) != -1):
                m =m+1
                numeror = numeror + int(self.lista3.getNodo(m+1))
              
              else:
                m=m+1;
            print(numeror)
            numeror=0;  
            x=0;
          m=0;
        
  

   