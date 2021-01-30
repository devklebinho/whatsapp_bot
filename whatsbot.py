#Importar bibliotecas
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver.exe"
#Navegar até o whatsapp web
driver = webdriver.Chrome(PATH)
#driver.get("https://web.whatsapp.com/")
#driver.get("https://www.convertte.com.br/gerador-link-whatsapp/")
driver.get("https://www.invertexto.com/gerador-link-whatsapp")
driver.maximize_window()
time.sleep(5)
#Definir contato e mensagem para enviar
#campo de pesquisa 'copyable-text selectable-text'
#campo de mensagem privada 'copyable-text selectable-text'
contatos = []#apenas (DDD) + 9 + número
mensagem = 'VAMOS AUTOMATIZAR TUDO DOIDO!'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

def criar_link(contato):
    #campo_numero_celular = driver.find_elements_by_xpath('//input[contains(@class, "form__input")]')
    campo_numero_celular = driver.find_elements_by_xpath('//input[contains(@class, "form-control")]')
    campo_numero_celular[0].click()
    time.sleep(3)
    campo_numero_celular[0].send_keys(contato)
    campo_numero_celular[0].send_keys(Keys.ENTER)
    #form__submit form__input--copy 

    #copiar_link = driver.find_elements_by_xpath('//input[contains(@class, "fform__input form__input--text")]')
    copiar_link = driver.find_elements_by_xpath('//button[contains(@class, "btn btn-classic")]')
    copiar_link.click()
    #copiar_link.copy()
    copiar_link.send_keys(Keys.CONTROL + 't')
    
    


#Buscar o contato
for contato in contatos:
    criar_link(contato)
    #buscar_contato(contato)
    #enviar_mensagem(mensagem)

