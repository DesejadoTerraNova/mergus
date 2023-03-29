import navegar
import log_in
from momento import Momento as mo
import getpass
import implant1z
import horaextra

name = input("Digite seu nome para logar no sistema: ")
mykey = getpass.getpass("Digite a chave de entrada: ")
<<<<<<< HEAD
hora = int(mo.horaja())
=======

>>>>>>> b3963a99125423a1a22dc17870daf297958a4a13
if hora <= 12:
    print(f"Bom dia {name}...")
elif hora > 12 and hora <= 17:
    print(f"Boa tarde {name}...")
else:
    print(f"Boa noite {name}...")

# Abrir página
navegar.log_up.abrir_p()
# Loga na conta digitada em name
navegar.log_up.logar(name, mykey)
<<<<<<< HEAD

=======
hora = int(mo.horaja())
>>>>>>> b3963a99125423a1a22dc17870daf297958a4a13

fazer = input("1 p/ reg. 1Z, 2 p/ reg. H.E., 3 p/ realizar pesquisa.")

if fazer == 1:
    implant1z()
elif fazer == 2:
    horaextra()

log_in.sai()
