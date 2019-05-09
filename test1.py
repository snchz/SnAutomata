from snautomata.SnMente import SnMente
from snautomata.SnOido import SnOidoGoogle
from snautomata.SnBoca import SnBocaWindows

oido=SnOidoGoogle()
boca=SnBocaWindows()
mente=SnMente(oido,boca)

mente.despertar()
mente.atender()
mente.dormir()