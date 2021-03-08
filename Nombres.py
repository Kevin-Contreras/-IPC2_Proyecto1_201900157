from xml.dom import minidom
from Nodo import *
class Nombre :
  letras=""
  listaCircular = Lista()
  numero=Lista()
  def ordenarMatriz(self,datow):
    n ="";
    h=0;
    h2=0
    po=0
    r=0
    contador=0
    m=""
    mini = minidom.parse(datow)
    nombres = mini.getElementsByTagName("matriz")
    datos = mini.getElementsByTagName("dato")
    for u in nombres:
      r=r+1
      self.listaCircular.insertar(u.attributes["nombre"].value)
    self.numero.insertar(r)
  def nombres(self):
    for u in range(int(self.numero.getNodo(1))):
       print(str(u+1) +") " + str(self.listaCircular.getNodo(u+1))+"--"+ str(u+1) )
    for y in range(int(self.numero.getNodo(1))):
        self.listaCircular.eliminar()

  def cantidad(self):
    return self.numero
    