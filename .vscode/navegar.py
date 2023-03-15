from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def navega():
    driver = webdriver.Chrome()
    driver.get("http://mergus.recife:8080/hr3411/awi/obj?objid=")
