from snautomata.SnOido import SnOidoGoogle
from snautomata.SnBoca import SnBocaWindows
import webbrowser

#CLASE MENTE
class SnMente(object):
	def __init__(self, oido, boca):
		self.oido=oido
		self.boca=boca
	def atender(self):
		while self.despierto==1:
			texto=self.oido.escuchar().upper()
			if "HOLA" in texto:
				self.boca.decir("Hola, qué tal?")
			elif "A DORMIR" in texto:
				self.boca.decir("OK")
				self.dormir()
			elif "ABRIR" in texto and "." in texto:
				webbrowser.open_new_tab(texto.replace("ABRIR ",""))
	def dormir(self):
		self.despierto=0
		self.boca.decir("Me voy a dormir. Buenas noches...")
	def despertar(self):
		self.despierto=1
		self.boca.decir("He despertado. Buenos días...")

