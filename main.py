class Fila(object):
   # """Clase base de fila"""

    def __init__(self):
        # """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
   # """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
    #    """Inserta un nuevo cliente en la fila preferencial"""
              self.enfila += 1
	      self.fila.append(cliente)
    def atender(self):
     #   """Atiende al proximo cliente preferencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
      #  """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if (self.enfila > maxenfila) :
           self.fila.append()
    
    
    
class FilaGeneral(Fila):
   # """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
   #     """Inserta un nuevo cliente en la fila no preferencial"""
           if cliente.categoria == general :
              self.enfila += 1

    def atender(self):
    #    """Atiende al proximo cliente prederencial"""
        self.enfila-=1

    

class cliente(object):
    # """clase cliente """
    def __init__(self,dni):
     #    """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
      #  """modifica el atributo categoria del cliente """
      self.categoria = categoria 
    
if __name__ == "__main__":
#    """ simular una fila en una entidad bancaria"""
     c1=cliente(3156789)
     print c1.dni
     fp=FilaPreferencial()
     fp.insertar(c1)
     print fp.enfila
     c1.modificarcategoria("preferencial")
     print c1.categoria
