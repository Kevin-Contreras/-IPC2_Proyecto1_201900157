from xml.dom import minidom
from Nodo import *
from DATOS import * 
class Proceso():
  lista= Lista()
  lista2 = Lista()
  lista3 = Lista()
  listaDatos = Lista()
  listaFrecuencia = Lista()
  listaFrecuencia2 = Lista()
  listaFrecuencia2 = Lista()
  listaSegunda = Lista()
  listaContae = Lista()
  lsitaDatosFuera = Lista()
  listaFrecuenciaFila=Lista()
  dimensionY= Lista()
  lk=Lista()
  tr= Lista()
  g = Dato()
  todolosDatos = Lista()
  kevin=0
  tyt=0
  def procesar(self,archivo):
  
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
 
  def ordenar(self,archivo):
    
    numeros =""
    datod=1;
    multi=1
    contador=1
    tu=0
    yt=0
    ki=0
    kia=0
    ukk=0
    ss=0
    coka=0

    contadoree=0
    contadoree3=0
    self.g.verificar(archivo)
    iterars = self.g.iterar().getNodo(1)
    
    docs = minidom.parse(archivo)
    items = docs.getElementsByTagName("dato")
    
    for u in range(int(iterars)):
      if(u>0):
        tu = int(self.g.y().getNodo(u))*int(self.g.x().getNodo(u))+tu

      r= int(self.g.x().getNodo(u+1))
      for i in range(r):
        for e in range(int(self.g.y().getNodo(u+1))*int(self.g.x().getNodo(u+1))):
          contadoree=contadoree+1
          contadoree3=contadoree3+1
          if(contadoree3==i+1):
            self.lista3.insertar(self.g.datos().getNodo(contadoree+tu))
          if(contadoree3==int(self.g.y().getNodo(u+1))):
            contadoree3=0
            
        contadoree=0
      if(u>0):
        ki=int(self.g.y().getNodo(u))*int(self.g.x().getNodo(u))+ki
    
      for ud in range(int(self.g.contador().getNodo(u+1))):
          if(int(self.g.datos().getNodo(ud+ki+1)) != 0 ):
            self.lista.insertar(1)
          else:
            self.lista.insertar(self.g.datos().getNodo(ud+ki+1))

      
      o = self.lista.recorrer()
      
      while o.siguinte:
        numeros = numeros + str(o.elemento())+","
        if(datod== multi*int(self.g.y().getNodo(u+1))):
          numero2 = numeros[:-1]
          multi=multi+1
          numeros=""
          self.lista2.insertar(numero2)
          if(datod == int(self.g.contador().getNodo(u+1))):
            break
        o = o.siguinte
        datod = datod+1
        numero2=""
      multi=1
      datod=1    
      yt=yt+1 
      naely = int(self.g.x().getNodo(u+1))
      ss=int(self.g.y().getNodo(u+1))*int(self.g.x().getNodo(u+1))
      
      self.incluir(archivo,yt)
      for fgd in  range(ss):
        self.lista3.eliminar()
        self.lista.eliminar()
      for df in range(int(self.g.x().getNodo(u+1))+1):
        self.lista2.eliminar()
      
    for df in range(ki+ss):
      self.g.lista.eliminar()
    
    
  def incluir(self,archivo,indice):
    
    cut=0
    self.g.verificar(archivo)
    iterars = self.g.iterar().getNodo(1)
    tu=0
    q=0
    op=0
    contadoraxd=0
    filad=0
    frecuenciat=0
    doc = minidom.parse(archivo)
    items = doc.getElementsByTagName("dato")
    matriz = doc.getElementsByTagName("matriz")
    nuevo2 = self.lista2.recorrer()
    contador1 =0
    valor =""
    valor2 = ""
    valor3=""
    contador23=0
    while nuevo2.siguinte:
        valor = valor + nuevo2.elemento()+"*"
        nuevo2 = nuevo2.siguinte
        contador1 = contador1 +1
        if(int(self.g.x().getNodo(indice)) == contador1 ):
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
    uo=0;
    r=0
    frecuencia=0
    orden =reversed( sorted( set(asterisco),key=lambda p: len(p)))
    asterisco = orden
  
    mivida=0
    x=0;
    m=0
    ll=0
    you=0
    me= int(self.g.y().getNodo(indice))
    mi = int(self.g.x().getNodo(indice))
    
    for da in asterisco:
      cut=cut+1
      if(da.find(",")!=-1):
        ll=ll+1
        you=you+1
        filad=filad+1
        frecuencia=frecuencia+1
        self.listaFrecuenciaFila.insertar(filad)
        datos = da.split(",")
        for dae in datos:
          frecuenciat=frecuenciat+1
        self.listaFrecuencia2.insertar(frecuenciat)
        frecuenciat=0
        for item in range(me):
          for y in range(mi):
            x=x+1
            if(da.find(str(x)) != -1):
              m= m+1
              numeror = numeror + int(self.lista3.getNodo(m))
            else:
              m=m+1
              
           
          self.listaDatos.insertar(numeror)
          self.todolosDatos.insertar(numeror)
          numeror=0
          x=0
        m=0
      else:
        mivida=mivida+1
        ll=ll+1
        self.listaFrecuencia2.insertar(1)
        self.listaFrecuenciaFila.insertar(int(da))
       
        if(indice>1):
          self.tyt = int(self.g.y().getNodo(indice-1))*int(self.g.x().getNodo(indice-1))+self.tyt
        for itera in range(int(self.g.contador().getNodo(indice))):
          if(int(da)*int(self.g.y().getNodo(indice))-int(self.g.y().getNodo(indice))<int(itera+1)):
           contador23=contador23+1
           if(contador23<=int(self.g.y().getNodo(indice))):
            self.lsitaDatosFuera.insertar(self.g.datos().getNodo(itera+1+self.tyt))
            self.todolosDatos.insertar(self.g.datos().getNodo(itera+1+self.tyt))

 
    op=op+1
    if(op==1):
      self.listaContae.insertar(int(self.g.y().getNodo(indice))*frecuencia)
    self.listaSegunda.insertar(mivida)
    self.lk.insertar(frecuencia)
    self.tr.insertar(you)
    self.dimensionY.insertar(ll)
    self.listaFrecuencia.insertar(cut)
  def reducida(self):
    return self.listaDatos
  def sobras(self):
    return self.lsitaDatosFuera
  def freMatriz(self):
    return self.listaFrecuencia
  def frecuenciaA(self):
    return self.listaFrecuencia2
  def contador(self):
    return self.listaContae
  def filas(self):
    return self.listaSegunda
  def frecuenciasFilas(self):
    return self.listaFrecuenciaFila
  def dimensiones(self):
    return self.dimensionY
  def fre(self):
    return self.lk
  def uy(self):
    return self.tr
  def todosDatos(self):
    return self.todolosDatos
  