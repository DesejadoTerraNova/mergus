from datetime import datetime
# entrega data e hora em suas partes individuais
class Momento:
    def diaja():
        diaja = datetime.now().day
        if diaja < 10:
            diaja = "0" + str(diaja)
        else:
            pass
        return diaja
    
    def mesja():
        mes = datetime.now().month
        if mes < 10:
            mes = "0" + str(mes)
        else:
            pass
        return mes
    def anoja():
        ano = datetime.now().year
        return ano
    def horaja():
        horagora = datetime.now().hour
        if horagora < 10:
            horagora = "0" + str(horagora)
        else:
            pass
        return horagora
    def min_ja():
        minutoja = int(datetime.now().minute)
        if minutoja < 10:
            minutoja = "0" + str(minutoja)
        else:
            pass
        return minutoja
# Bom resultado