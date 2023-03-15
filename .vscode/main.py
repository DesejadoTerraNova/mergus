# import time
import getpass
import log_in
import implant1z
import horaextra

fazer = input("1 p/ reg. 1Z, 2 p/ reg. H.E., 3 p/ realizar pesquisa.")
log_in.guia()
if fazer == 1:
    implant1z()
elif fazer == 2:
    horaextra()

log_in.sai()
