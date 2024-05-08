from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
import datetime

data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
nome_arquivo = f'resultado_teste_{data_hora_atual}.txt'
driver = webdriver.Chrome()


# Cenário: Pesquisar na barra de pesquisa

# Dado que o usuario deseja pesquisar um produto na barra de pesquisa
# Quando ele digita a palavra-chave na mesma
# Então será retornado todos os produtos que contenham "TV" ou "Televisão" no nome.

def teste_barra_de_busca():

    try:
        driver.get('https://mercadolivre.com.br')
        sleep(5)


        driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys('televisão')
        driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys(Keys.ENTER)
    
        resultado = driver.find_element(By.XPATH, '//*[@id=":R26l5e6:"]/div[2]').text
    
        if 'TV'.casefold() in resultado or 'Televisão'.casefold() in resultado:
            status = "OK"
            res = '1 - Teste (Barra de busca) bem-sucedido: O resultado exibido é o esperado. Status: '
         
        else:
            status = "Fail"
            res = '1 - Teste (Barra de busca) falhou: O resultado exibido (' + resultado + ') não corresponde ao esperado. Status: '

        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(res + ' ' + status + '\n')
            print(f'1 - Resultado do teste salvo em "{nome_arquivo}" com status: {status}')
  
    
    except TimeoutException:
        print('Tempo limite excedido ao aguardar elementos na página.')
    
    except NoSuchElementException as erro:
        print(f'Elemento não encontrado: {erro}')



# Cenário: Comprar um produto utilizando o botão comprar
        
# Dado que o usuario deseja comprar um produto no site
# Quando ele clica no botão "Comprar" na pagina
# Então ele será redirecionado ao checkout ou o fluxo de compra irá continuar.

def teste_botao_comprar():
    try:
        driver.get('https://www.mercadolivre.com.br/smart-tv-lg-32-led-hd-32lq621-bivolt-preta-experincia-visual-incrivel/p/MLB19470425?pdp_filters=item_id:MLB2761589264#is_advertising=true&searchVariation=MLB19470425&position=2&search_layout=grid&type=pad&tracking_id=633e2f49-4bb9-48b2-8d53-8ace6307f557&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=YWJmMzgxNDQtNGY2MS00MzkwLWE4YzItNWQxZWRmODY5MWM1')
        sleep(5)

        driver.find_element(By.XPATH, '//*[@id=":R15d3a6c4um:"]').click()
    
        resultado = driver.find_element(By.XPATH, '//*[@id="registration-link"]')
    
        if resultado.is_displayed():
            status = "OK"
            res = '2 - Teste (Botão comprar) bem-sucedido: O resultado exibido é o esperado. Status: '
         
        else:
            status = "Fail"
            res = '2 - Teste (Botão comprar) falhou: O resultado exibido não corresponde ao esperado. Status: '

        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(res + ' ' + status + '\n')
            print(f'2 - Resultado do teste salvo em "{nome_arquivo}" com status: {status}')

  
    
    except TimeoutException:
        print('Tempo limite excedido ao aguardar elementos na página.')
    
    except NoSuchElementException as erro:
        print(f'Elemento não encontrado: {erro}')
    
    finally:
        driver.quit()

teste_barra_de_busca()
teste_botao_comprar()