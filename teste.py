import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://trello.com/b/uLxYR5nA/rotina")

def get_by_id(term):
  elem = driver.find_element_by_id(term)
  time.sleep(1)
  return elem 

def gets_by_css_selector(term):
  elements = driver.find_elements_by_css_selector(term)
  time.sleep(1)
  return elements 

elems = driver.find_elements_by_tag_name("a")

for x in elems:
  if x.text == 'Log In':
    login = x

login.click()

email = get_by_id("user")
email.send_keys(os.environ['TRELLO_USER'])
login2 = get_by_id("login")
login2.click()
password = get_by_id("password")
password.send_keys(os.environ['ATLASSIAN_PW'])
entrar = get_by_id("login-submit")
print ('entrar encontrado')

entrar.click()
time.sleep(30)

listas = gets_by_css_selector('div.list')

print (len(listas))

driver.close()
