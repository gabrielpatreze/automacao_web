pip install selenium
baixar o driver do navegador
chromedrive
colocar aonde esta instalado o python

----

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#abrindo navegador
nav = webdriver.Chrome()
nav.get('https://google.com/')

#inspecionar, clica na seta pra selecionar
#botao direito e copia o xpath
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')
#enter
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dolar = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print('o valor atual do dólar é:',dolar)

######################################################
nav.get('https://google.com/')

nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')
#enter
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

euro = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print('o valor atual do euro é:',euro)

######################################################

nav.get('https://www.melhorcambio.com/ouro-hoje')

ouro = nav.find_element_by_xpath('//*[@id="comercial"]').get_attribute("value")
ouro = ouro.replace(",", ".")
print('o valor atual do ouro é:',ouro)

nav.quit()

######################################################

import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')
display('TABELA ORIGINAL', tabela)
#linha, coluna
tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(dolar)
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(euro)
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(ouro)

display('TABELA COM COTAÇÃO ATUALIZADA',tabela)

tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Cotação"]
tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Margem"]

display('TABELA FINAL', tabela)

----

exportar para excel

tabela.to_excel('Produtos_Novos.xlsx')
#tabela.to_excel('Produtos_Novos.xlsx', index=False)


----








