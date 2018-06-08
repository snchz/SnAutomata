import SnOido, SnBoca
from SnOido import SnOidoTerminal
from SnBoca import SnBocaEspeak

#CLASE MENTE
class SnMente(object):
	def __init__(self, oido, boca):
		self.oido=oido
		self.boca=boca
		self.despertar()
		self.bucle()
	def bucle(self):
		while self.despierto==1:
			texto=self.oido.escuchar()
			if texto=="Hola":
				self.boca.decir("Hola, qué tal?")
			elif texto=="Vete a dormir":
				self.boca.decir("OK")
				self.dormir()
	def dormir(self):
		self.despierto=0
		self.boca.decir("Me voy a dormir. Buenas noches...")
	def despertar(self):
		self.despierto=1
		self.boca.decir("He despertado. Buenos días...")

oido=SnOidoTerminal()
boca=SnBocaEspeak()
mente=SnMente(oido,boca)
