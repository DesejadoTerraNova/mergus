# import getpass
# import time
from momento import Momento as mo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.support.webdriver.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://mergus.recife:8080/hr3411/awi/obj?objid=")
def guia(name, keys):
    loginup = name
    keykey = keys
    hora = int(mo.horaja())
    if hora <= 12:
        print(f"Bom dia {loginup}...")
    else:
        print(f"Boa tarde {loginup}...")
    driver.find_element(
        by=By.XPATH, value='//*[@id="opcoes"]/table/tbody/tr[1]/td/a/img').click()
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
def sai():
    driver.close()
