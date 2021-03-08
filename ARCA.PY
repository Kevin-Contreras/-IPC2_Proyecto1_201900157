from DATOS import*
from PROCESAR import *
from COLOCAR import *
from xml.dom import minidom
class archivo:
  nombre = Colocar()
  datosDeIteracion = Dato()
  todos = Proceso()
  def final(self,archivoInicial,archivoFinal):
    ty=0
    nae=0
    rt=0
    yu=0
    o=0
    contador=0
    doc = minidom.Document()
    
    root = doc.createElement("matrices")
   
 
    doc.appendChild(root)
 
    for value in range(self.datosDeIteracion.iterar().getNodo(1)):
   # Create Element
      tempChild = doc.createElement("matriz")
     
        
      
      for erw in range(int(self.nombre.cantidad().getNodo(1))):
         tempChild.setAttribute("nombre",str(self.nombre.nombres().getNodo(value+1)+"_salida"))
      for y in range(int(self.todos.dimensiones().getNodo(value+1))):
        for x in range(int(self.datosDeIteracion.y().getNodo(value+1))):
          tempChild.setAttribute("n",str(y+1))
          tempChild.setAttribute("m",str(x+1))
      root.appendChild(tempChild)
      nodeText = doc.createTextNode(str(value) )
      tempChild.setAttribute("g",str(self.todos.freMatriz().getNodo(value+1)))
      for x in range(int(self.todos.dimensiones().getNodo(value+1))):
        for y in range(int(self.datosDeIteracion.y().getNodo(value+1))):
          contador=contador+1
          dato = doc.createElement("dato")
          dato.setAttribute("x",str(x+1))
          dato.setAttribute("y",str(y+1))
          tempChild.appendChild(dato)
          nodeText2= doc.createTextNode(str(self.todos.todosDatos().getNodo(contador)))
          dato.appendChild(nodeText2)
          
      
      for t in range( int(self.todos.freMatriz().getNodo(value+1))):
        yu=yu+1
        datoF = doc.createElement("frecuencia")
        datoF.setAttribute("g",str(self.todos.frecuenciasFilas().getNodo(yu)))
        tempChild.appendChild(datoF)
        nodeText3= doc.createTextNode(str(self.todos.frecuenciaA().getNodo(yu)))
        datoF.appendChild(nodeText3)
        
      
    doc.writexml( open(archivoFinal, 'w'),
               indent="  ",
               addindent="  ",
               newl='\n')
 
    doc.unlink()
