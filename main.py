from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

# Cenário: Pesquisar na barra de tarefas
# Dado que o usuario deseja pesquisar um produto na barra de pesquisa
# Quando ele digita a palavra-chave na mesma
# Então será retornado todos os produtos que contenham "TV" ou "Televisão no nome"

try:
    driver.get('https://mercadolivre.com.br')
    sleep(5)


    driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys('televisão')
    driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys(Keys.ENTER)
    
    resultado = driver.find_element(By.XPATH, '//*[@id=":R26l5e6:"]/div[2]').text
    
    if 'TV' or 'Televisão' or 'televisão' in resultado:
        status = "OK"
        print(f'Teste bem-sucedido: O resultado exibido é o esperado. Status: {status}')
    else:
        status = "Fail"
        print(f'Teste falhou: O resultado exibido ({resultado}) não corresponde ao esperado. Status: {status}')
    
except TimeoutException:
    print('Tempo limite excedido ao aguardar elementos na página.')
    
except NoSuchElementException as erro:
    print(f'Elemento não encontrado: {erro}')
    
finally:
    driver.quit()