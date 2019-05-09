from snautomata.SnMente import SnMente
from snautomata.SnOido import SnOidoOffline
from snautomata.SnBoca import SnBocaWindows

oido=SnOidoOffline()
boca=SnBocaWindows()
mente=SnMente(oido,boca)

mente.despertar()
mente.atender()
mente.dormir()