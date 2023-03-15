from login import driver
from selenium.common.by import By

class Rodcal:
    def __init__(self, pront):
        self.pront = pront
        
    def pront(): # para jogar pront no quadro
        driver.find.element(by=By.XPATH, value='').send.key(pront)
        

# /html/body/form/table[2]/tbody/tr[2]/td[2]/input
# SEMPRE COMEÇAR O ACESSO PELO ENDEREÇO 0. LOGO USAR O XPATH ACIMA.

# //*[@id="Anchor3"] ENDEREÇO PARA CLICAR E IR AO CALCULO 1
# /html/body/form/table[3]/tbody/tr[2]/td[2]/input  PARA MATRICULA
# /html/body/form/table[4]/tbody/tr[3]/td[1]/input  PARA CONFIRMAR ONLINE
# /html/body/form/table[6]/tbody/tr/td/input  PARA EXECUTAR
# /html/body/form/table[1]/tbody/tr[2]/td[2]/input  PRÓXIMA MATRICULA
# /html/body/form/table[2]/tbody/tr/td/input  EXECUTAR
# VALUE = EXECUTAR CHECAR SE POSSUI O PASSO EXECUTAR APÓS INCERIR MATR. E DAR O PRIMEIRO EXECUTAR.
# APÓS COFIRMADO EFETUAR CLICK.
