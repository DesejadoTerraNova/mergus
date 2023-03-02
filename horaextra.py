import datetime
import getpass
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

loginup = input("NickName >  ")
keykey = getpass.getpass("Palavra passe >  ")

# Aceessar o MERGUS
driver = webdriver.Chrome()
driver.get("http://mergus.recife:8080/hr3411/awi/obj?objid=")
time.sleep(2)
# Efetuar log on no portal. Botao para logar
# wait.until(expected_conditions.alert_is_present())
driver.find_element(
    by=By.XPATH, value='//*[@id="opcoes"]/table/tbody/tr[1]/td/a/img').click()
# time.sleep(1)

# Campo usuario
driver.switch_to.frame("DF")

driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').send_keys(loginup)
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').send_keys(keykey)
driver.find_element(
    By.XPATH, '/html/body/form/table[4]/tbody/tr/td/input').click()

# Acessar pagina para Lote
driver.switch_to.frame("DF")
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').click()
driver.find_element(
    By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').send_keys(
        "221" + Keys.ENTER)

# Registrar Lote
year = int(datetime.datetime.now().year)
month = int(datetime.datetime.now().month)

driver.switch_to.frame("DF")
if month < 10:
    driver.find_element(
        By.XPATH, "/html/body/form/table[1]/tbody/tr[1]/td[2]/input").send_keys(
            f"{year}/0{month}NB-HE160")
else:
    driver.find_element(
        By.XPATH, "/html/body/form/table[1]/tbody/tr[1]/td[2]/input").send_keys(
            f"{year}/{month}NB-HE160")

driver.find_element(
    By.XPATH, "/html/body/form/table[1]/tbody/tr[1]/td[2]/input").send_keys(
        f"{year}/{month}NB-HE160")
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="Anchor3"]').click()

# Configurar Lote
driver.switch_to.frame("DF")
driver.find_element(
    By.XPATH, "/html/body/form/table[2]/tbody/tr[6]/td[2]/input").send_keys('1')
driver.find_element(
    By.XPATH, "/html/body/form/table[2]/tbody/tr[4]/td[4]/input").send_keys('160')
driver.find_element(
    By.XPATH, '/html/body/form/table[4]/tbody/tr/td/input').click()
wait = WebDriverWait(driver, timeout=5, poll_frequency=0.2)
# Coletar dados da planilha
linha = 0
i = 0
c = 4
# driver.switch_to.default_content()
driver.switch_to.frame("DF")
tabela = pd.read_excel("HORAEXTRA.xls", sheet_name="HE")
for i, matricula in enumerate(tabela["matricula"]):
    horaextra1 = tabela.loc[i, "horaextra"]
    horaextra = int(horaextra1)
    # Registrar conteudo da ocorrencia
    # Registrar Carga Horaria
    d = 2
    time.sleep(0.5)
    # print(f"Em i = {i} teve que esperar 0.5 segundos")
    driver.find_element(
        By.XPATH, f"/html/body/form/table[2]/tbody/tr[{c}]/td[{d}]/input").click()
    driver.find_element(
        By.XPATH, f"/html/body/form/table[2]/tbody/tr[{c}]/td[{d}]/input").send_keys(
            matricula)
    d += 2
    time.sleep(0.5)
    # print(f"Em i = {i} teve que esperar 0.5 segundos")
    driver.find_element(
        By.XPATH, f"/html/body/form/table[2]/tbody/tr[{c}]/td[{d}]/input").click()
    driver.find_element(
        By.XPATH, f"/html/body/form/table[2]/tbody/tr[{c}]/td[{d}]/input").send_keys(
            horaextra)
    c += 1
    linha += 1
    if c == 18:
        c = c - 13
        # ENTREGA PARA A ULTIMA LINHA DE TRABALHO REALIZADA
        driver.find_element(
            By.XPATH, "/html/body/form/table[3]/tbody/tr[2]/td[2]/input").click()
        driver.find_element(
            By.XPATH, "/html/body/form/table[3]/tbody/tr[2]/td[2]/input").send_keys(linha)

        # Buton Executa.
        driver.find_element(
            By.XPATH, "/html/body/form/table[4]/tbody/tr/td/input").click()
        # time.sleep(1.5)

        # wait.until(driver.find_element(By.TAG_NAME, "DF"))
        driver.switch_to.frame("DF")

# Fecha o Lote.
# Click no botão EXECUTAR
driver.find_element(
    By.XPATH, "/html/body/form/table[4]/tbody/tr/td/input").click()
time.sleep(2)
# wait.until(driver.find_element(By.TAG_NAME, "FF"))
driver.switch_to.frame("FF")
driver.find_element(
    By.XPATH, "/html/body/form/table[2]/tbody/tr[7]/td/a").click()
# Exception /html/body/form/table[2]/tbody/tr/td/font
