#Importar bibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "chromedriver.exe"
#Navegar até o whatsapp web
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(30)
#Definir contato e mensagem para enviar
contatos = ['Evandro', 'Bianca']
#Buscar o contato
#Enviar mensagem