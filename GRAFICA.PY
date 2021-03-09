from graphviz import Digraph
from xml.dom import minidom
from Nodo import *
class graf():
  listaCircular = Lista()
  listaNombre = Lista()
  dimensiones = Lista()
  def graficas(self,archivo,indice):
    mini=minidom.parse(archivo)
    matrices = mini.getElementsByTagName("matriz")
    self.listaNombre.insertar(matrices[int(indice)-1].attributes["nombre"].value)
    self.dimensiones.insertar(matrices[int(indice)-1].attributes["n"].value)
    self.dimensiones.insertar(matrices[int(indice)-1].attributes["m"].value)
    for matriz in matrices[int(indice)-1].childNodes:
      if(str(matriz).find("dato")!=-1):
        self.listaCircular.insertar(matriz.firstChild.nodeValue)
  def graficarMatriz(self,final):
    dot = Digraph(comment='MATRIZ')
    dot.format='png'
    dot.node("M","Matrices",)
    nombre=dot.node('A',self.listaNombre.getNodo(1),)
    dot.edge("M","A")
    dot.node('x',"n = "+str(self.dimensiones.getNodo(1)))
    dot.node('y',"m = "+self.dimensiones.getNodo(2))
    dot.edges(['Ax','Ay'])
    
   
    for re in range(int(self.dimensiones.getNodo(2))*int(self.dimensiones.getNodo(1))):
      dot.node(str(re+1),self.listaCircular.getNodo(re+1),shape="circle",color="green")
      if(re<int(self.dimensiones.getNodo(2))):
        dot.edge('A',str(re+1))
      else:
        dot.edge(str(int(re+1)-int(self.dimensiones.getNodo(2))),str(int(re+1)),constraint='true')
    for e in range(int(self.dimensiones.getNodo(2))*int(self.dimensiones.getNodo(1))):
      self.listaCircular.eliminar()
    self.dimensiones.eliminar()
    self.dimensiones.eliminar()
    self.listaNombre.eliminar()
    dot.render(final)


  



