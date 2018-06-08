import abc #Para hacer uso de la clase abstracta
from abc import ABCMeta
from abc import abstractmethod

#CLASE ABSTRACTA, HEREDAR TODOS DE AQUI
class SnOido(object):
	__metaclass__=ABCMeta

	@abstractmethod
	def escuchar(self):
		dummy=1 #No hace nada

#CLASE QUE HEREDA DE LA ABSTRACTA PARA ESCRIBIR POR EL TERMINAL
class SnOidoTerminal(SnOido):
	def __init__(self):
		SnOido.__init__(self)
	def escuchar(self):
		super(SnOidoTerminal,self).escuchar()
		return input("Estoy a la escucha: ")

#oido=SnOidoTerminal()
#texto=oido.escuchar()
#print(texto)
