from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class log_up:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def abrir_p(self):
        self.driver.get("http://mergus.recife:8080/hr3411/awi/obj?objid=")
    
    def logar(self, name, mykey):
        self.name = name
        self.key = mykey
        self.driver.find_element(
            by=By.XPATH, value='//*[@id="opcoes"]/table/tbody/tr[1]/td/a/img').click()
        self.driver.switch_to.frame("DF")
        self.driver.find_element(
            By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').click()
        self.driver.find_element(
            By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td[2]/input').send_keys(self.name)
        self.driver.find_element(
            By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').click()
        self.driver.find_element(
            By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td[2]/input').send_keys(
                self.key + Keys.ENTER)
