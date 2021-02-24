class Nodo:
  def __init__(self,datos):
    self.__datos = datos
    self.__siguinte=None
  def elemento(self) :
    return self.__datos
class Lista:
  inicio=None
  final=None
  def getValor(self):

    if(self.inicio==None):

      return True
    else:
      return False

  def insertar(self,numero):
    nodoTemporal = Nodo(numero)
    if(self.getValor() == True):
      self.inicio=nodoTemporal
      self.final = self.inicio
      self.final.siguinte = self.inicio
    
    else:
      nodoTemporal = self.final
      self.final = nodoTemporal.siguinte= Nodo(numero)  
      self.final.siguinte = self.inicio
      

  def mostrar (self): 
    if(self.getValor() == True):
      print("esta vacio")
    else:
      aux = self.inicio
      while aux.siguinte != self.inicio:
        print(aux.elemento())
        aux = aux.siguinte
      
      print(aux.elemento())
      
  def recorrer (self): 
      aux = self.inicio
      return aux
  def recorrers (self): 
      auxr = self.inicio
      return auxr
  
