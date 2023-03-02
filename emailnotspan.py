import getpass

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys

loginup = input("NickName >  ")
keykey = getpass.getpass(prompt='Palavra passe >  ', stream=None)
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/")

def email(endmail, tema, corpo):
    try:
        # Criar o e-mail
        driver.find_element(by=By.XPATH, value='//*[@id="gb"]/div[2]/div[1]/div[1]/svg').click()
        driver.find_element(
            by=By.XPATH, value='/html/body/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div').click()
        # Endereço do e-mail.
        driver.find_element(by=By.XPATH, value='//*[@id=":tg"]').click()
        driver.find_element(by=By.XPATH, value='//*[@id=":tg"]').send_keys(endmail)
        # Assunto do e-mail..
        driver.find_element(by=By.XPATH, value='//*[@id=":pi"]').click()
        driver.find_element(by=By.XPATH, value='//*[@id=":pi"]').send_keys(tema)
        # Corpo do e-mail...
        driver.find_element(by=By.XPATH, value='//*[@id=":qr"]').click()
        driver.find_element(by=By.XPATH, value='//*[@id=":qr"]').send_keys(corpo)
        # clicar em enviar a mensagem...
        driver.find_element(by=By.XPATH, value='//*[@id=":p8"]').click()
    except Exception as ex:
        with open('registro_email.txt', "a", encoding="utf-8") as arquivo:
            arquivo.write(f"\n{ex} do tipo {type(ex)}")

    print("Ocorreu um erro, consulte arquivo de registro de falhas.")

acountg = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]'
acountg = str(acountg)

if driver.find_element(by=By.XPATH, value=acountg) is True:
    driver.find_element(
        by=By.XPATH, value=acountg).click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input').send_keys(keykey)
    driver.find_element(
        by=By.XPATH, value='//*[@id="passwordNext"]/div/button/div[3]').click()
else:
    driver.find_element(
        by=By.XPATH, value='//*[@id="identifierId"]').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="identifierId"]').send_keys(loginup)

 # botão AVANÇAR do login.

driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]").click()


grupo = pd.read_excel("grupoemail.xls", sheet_name='mail')
i = 0
for i, o_endmail in enumerate(grupo["endmail"]):
    o_tema = str(grupo.loc[i, "tema"])
    # tema = str(tema)
    o_corpo = str(grupo.loc[i, "corpo"])
    # corpo = str(corpo)
# Coletar os dados da planilha dos receptores das mensagens.
    email(o_endmail, o_tema, o_corpo)
