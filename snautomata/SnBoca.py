import abc #Para hacer uso de la clase abstracta
from abc import ABCMeta
from abc import abstractmethod
import os, time

from gtts import gTTS #pip install gTTS

from pygame import mixer



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

#CLASE QUE HEREDA DE LA ABSTRACTA PARA SONAR POR EL ALTAVOZ DE WINDOWS
class SnBocaWindows(SnBoca):
	def __init__(self):
		SnBoca.__init__(self)
	def decir(self, texto):
		fichero='temp'+str(int(time.time()))+'.mp3'
		ruta=os.path.dirname(os.path.abspath(__file__))+"\\"+fichero
		tts = gTTS(text=texto, lang='es')
		tts.save(ruta)
		mixer.init()
		mixer.music.load(ruta)
		mixer.music.play()

#boca=SnBocaWindows()
#boca.decir("Hola")
#boca.decir("que tal")
