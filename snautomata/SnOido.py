import abc #Para hacer uso de la clase abstracta
from abc import ABCMeta
from abc import abstractmethod

import speech_recognition as sr

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

class SnOidoGoogle(SnOido):
	def __init__(self):
		SnOido.__init__(self)
	def escuchar(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Escuchando...")
			audio = r.listen(source)
			#try:
			text = r.recognize_google(audio, language = "es-ES", show_all=True) #show_all para que muestre algo aunque sea con poca coincidencia
			print("He oido lo siguiente: "+str(text))
			primerResultado=""
			if len(text)>0:
				if len(text['alternative'])>0:
					primerResultado=text['alternative'][0]['transcript']
			print("Y esto es lo mas probable: "+primerResultado)
			return primerResultado
			#except:
			#	print("Sorry could not recognize your voice")

class SnOidoOffline(SnOido):
	def __init__(self):
		SnOido.__init__(self)
	def escuchar(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=5) 
			print("Escuchando...")
			audio = r.listen(source)
			#try:
			text = r.recognize_sphinx(audio, language = "es-ES")
			print("He oido lo siguiente: "+str(text))
			return str(text)
			#except:
			#	print("Sorry could not recognize your voice")
