import abc #Para hacer uso de la clase abstracta
from abc import ABCMeta
from abc import abstractmethod

#CLASE ABSTRACTA, HEREDAR TODOS DE AQUI
class SnBoca(object):
	__metaclass__=ABCMeta

	@abstractmethod
	def decir(self, texto):
		dummy=1 #No hace nada

#CLASE QUE HEREDA DE LA ABSTRACTA PARA ESCRIBIR POR EL TERMINAL
class SnBocaTerminal(SnBoca):
	def __init__(self):
		SnBoca.__init__(self)
	def decir(self, texto):
		super(SnBocaTerminal,self).decir(texto)
		print(texto)

from espeak import espeak

class SnBocaEspeak(SnBoca):
	def __init__(self):
		SnBoca.__init__(self)
	def decir(self, texto):
		super(SnBocaTerminal,self).decir(texto)
		espeak.set_parameter(espeak.Parameter.Pitch, 6)                                                                                                               
  espeak.set_parameter(espeak.Parameter.Rate, 150) #velocidad                                                                                                   
  espeak.set_parameter(espeak.Parameter.Range, 600)                                                                                                             
  espeak.set_voice('spanish')                                                                                                                                   
  espeak.synth(texto)                                                                                                                                                                                                                                                                             
  while espeak.is_playing():                                                                                                                                    
    pass
#boca=SnBocaTerminal()
#boca.decir("Alllll")
