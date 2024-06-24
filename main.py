from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#Coloque a url para a execução do webscraping
url = ''

# Configuração do Selenium para carregar a página dinamicamente
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

# Espera até que pelo menos um elemento com a classe "nome_da_classe" seja carregado
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '')))

# Captura o HTML após a página ser completamente carregada
html = driver.page_source

# Fechar o navegador Selenium
driver.quit()

# Usar BeautifulSoup para analisar o HTML capturado
soup = BeautifulSoup(html, 'html.parser')

# Classes que quer verificar
classes_a_verificar = ('', '', '')

for classe in classes_a_verificar:
    elementos_com_classe = soup.find_all(class_=classe)
    num_elementos = len(elementos_com_classe)
    
    if num_elementos > 0:
        print(f'Elementos com a classe "{classe}" foram encontrados: {num_elementos}')
    else:
        print(f'Nenhum elemento com a classe "{classe}" foi encontrado.')
