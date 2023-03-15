import getpass
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

# geckodriver_autoinstaller.install()

loginup = input("NickName >  ")
keykey = getpass.getpass("Palavra passe >  ")

# Acessar o MERGUS
# driver = Firefox()
driver = webdriver.Chrome()
driver.get("http://mergus.recife:8080/hr3411/awi/obj?objid=")
# Efetuar log on no portal. Botão para logar
# wait.until(expected_conditions.alert_is_present())
driver.find_element(
    by=By.XPATH, value='//*[@id="opcoes"]/table/tbody/tr[1]/td/a/img').click()


def click_entrega(ender, conteudo):
    driver.find_element(By.XPATH, ender).click()
    driver.find_element(By.XPATH, ender).send_keys(conteudo)


# Campo usuario

driver.switch_to.frame("DF")

driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').send_keys(loginup)
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').send_keys(
        keykey + Keys.ENTER)
# driver.find_element(By.XPATH, '/html/body/form/table[4]/tbody/tr/td/input').click()

# Acessar 1Z
time.sleep(1)
driver.switch_to.frame("DF")
driver.find_element(By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').send_keys(
        "1Z" + Keys.ENTER)

# Click na seta de entrada do ambiente 1Z.
time.sleep(0.5)
driver.switch_to.frame("DF")
driver.find_element(By.XPATH, '//*[@id="Anchor3"]/img').click()

# time.sleep(1)
# Coletar dados da planilha
tabela = pd.read_excel("AUTOMATIZAR1Z.xls", sheet_name="1Z")
tabela['linha2'].fillna('', inplace=True)
tabela['linha3'].fillna('', inplace=True)
tabela['linha4'].fillna('', inplace=True)
tabela['linha5'].fillna('', inplace=True)
tabela['linha6'].fillna('', inplace=True)
# print(tabela)
i = 0
for i, matricula in enumerate(tabela["matricula"]):
    codigo = tabela.loc[i, "codigo"]
    codigo = int(codigo)
    diadom = tabela.loc[i, "diadom"]
    diadom = int(diadom)
    mesdom = tabela.loc[i, "mesdom"]
    mesdom = int(mesdom)
    anodom = tabela.loc[i, "anodom"]
    anodom = int(anodom)
    legalidade = tabela.loc[i, "legalidade"]
    legalidade = str(legalidade)
    dia1 = tabela.loc[i, "dia1"]
    dia1 = int(dia1)
    mes1 = tabela.loc[i, "mes1"]
    mes1 = int(mes1)
    ano1 = tabela.loc[i, "ano1"]
    ano1 = int(ano1)
    dia2 = tabela.loc[i, "dia2"]
    dia2 = int(dia2)
    mes2 = tabela.loc[i, "mes2"]
    mes2 = int(mes2)
    ano2 = tabela.loc[i, "ano2"]
    ano2 = int(ano2)
    linha1 = tabela.loc[i, "linha1"]
    linha1 = str(linha1)
    linha2 = tabela.loc[i, "linha2"]
    linha2 = str(linha2)
    linha3 = tabela.loc[i, "linha3"]
    linha3 = str(linha3)
    linha4 = tabela.loc[i, "linha4"]
    linha4 = str(linha4)
    linha5 = tabela.loc[i, "linha5"]
    linha5 = str(linha5)
    linha6 = tabela.loc[i, "linha6"]
    linha6 = str(linha6)
    # confirmar = tabela.loc[i, "confirmar"]
    # confirmar = str(confirmar)

    # Registrar ocorrencias no 1Z.
    # Registrar matricula e codigo
    # Campo matricula
    time.sleep(1)
    driver.switch_to.frame("DF")
    driver.find_element(
        By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[2]/input').clear()
    driver.find_element(
        By.XPATH, '/html/body/form/table[1]/tbody/tr[2]/td[2]/input').send_keys(matricula)
    # click_entrega('/html/body/form/table[1]/tbody/tr[2]/td[2]/input', matricula)
    # Campo codigo
    driver.find_element(
        By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td[2]/input').send_keys(codigo)
    # click_entrega('/html/body/form/table[1]/tbody/tr[3]/td[2]/input', codigo)
    # Clique no botao criar
    driver.find_element(by=By.XPATH, value='//*[@id="Anchor3"]/img').click()

    # Registrar conteudo da ocorrencia
    # Dia do DOM
    time.sleep(1)
    driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[2]/td[2]/input', diadom)
    # Mes do DOM
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[2]/td[4]/input', mesdom)
    # Ano do DOM
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[2]/td[6]/input', anodom)
    # Base Legal
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[2]/td[8]/input', legalidade)
    # Dia 01
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[2]/input', dia1)
    # Mes 01
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[4]/input', mes1)
    # Ano 01
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[6]/input', ano1)
    # Dia 02
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[8]/input', dia2)
    # Mes 02
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[10]/input', mes2)
    # Ano 02
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[3]/tbody/tr[3]/td[12]/input', ano2)
    # Linha 01
    # A INCERÇÃO P/ AS LINHAS APRESENTOU COMPORTAMENTO DE QUANDO SUPERAR O LIMITE
    # DEFINIDO PELO SITE ELE RESERVA OS DEMAIS CARACTERES PARA A APRÓXIMA LINHA, 
    # EMPURRANDO A COLETA PROSTERIOR PARA FRENTE, MESMO QUE A PRÓXIMA VARIÁVEL POSSUA CONTEÚDO
    # PARA SEREM INCERIDOS.
    click_entrega('/html/body/form/table[4]/tbody/tr[2]/td[2]/input', linha1)
    # Linha 02
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[3]/td/input', linha2)
    # Linha 03
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[4]/td/input', linha3)
    # Linha 04
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[5]/td/input', linha4)
    # Linha 05
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[6]/td/input', linha5)
    # Linha 06
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[7]/td/input', linha6)
    # Confirmar com S
    # driver.switch_to.frame("DF")
    click_entrega('/html/body/form/table[4]/tbody/tr[9]/td[2]/input', "S")
    # Clica em Executar.
    # driver.switch_to.frame("DF")
    driver.find_element(By.XPATH, '/html/body/form/table[6]/tbody/tr/td/input').click()
