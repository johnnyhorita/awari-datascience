# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:21:51 2021

@author: johnny.horita
"""

## Todas as Importações
from selenium import webdriver
from time import sleep

## Todos os parametros, variáveis e constantes (fixos)
LINKEDIN_URL = 'https://br.linkedin.com/jobs/search?keywords=Ci%C3%AAncia%20Dos%20Dados&location=S%C3%A3o%20Paulo%2C%20S%C3%A3o%20Paulo%2C%20Brasil&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'
NOME_ARQUIVO = 'descricao_vagas_linkedin.txt'

## Todas as Funções e classes

## Execução do código
if __name__ == '__main__':
    # Criar instância do Google Chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    # Acessar o endereço da URL LINKEDIN_URL
    driver.get(LINKEDIN_URL)
    
    # Aguarda X segundos para execução do próximo comando
    sleep(2)
    
    # Lista os elementos (vagas) da página pela classe result-card
    #resultado_vagas = driver.find_elements_by_class_name('result-card')
    resultado_vagas = driver.find_elements_by_class_name('jobs-search__results-list')

    # lista das descrições das vagas
    lista_descricoes = []

    # Condição ciclica para leitura das vagas
    while True:
        # Le item por item da lista resultado_vagas
        for vaga in resultado_vagas[len(lista_descricoes):]:
            # Clica na vaga referente a lista resultado
            vaga.click()
            # Aguarda X segundos para execução do próximo comando
            sleep(2)
            try:
                descricao = driver.find_element_by_class_name('description')
                # Adiciona um item na lista com a descrição da vaga
                lista_descricoes.append(descricao.text)
            except:
                # Retorna exceção
                print ('erro')
                pass
    
        # Lista os elementos (vagas) da página pela classe result-card
        resultado_vagas = driver.find_elements_by_class_name('result-card')
        
        print ('Pesquisa de vagas:', len(resultado_vagas))
        print ('Descrições adicionadas:', len(lista_descricoes))
        
        #Critério de saída para a condição do While
        if (len(lista_descricoes) == len(resultado_vagas)):
           break

#    # Trecho de leitura para os 25 itens da lista
#    # Le a lista de resultado_vagas
#    for vaga in resultado_vagas:
#        # Clica na vaga referente a lista resultado
#        vaga.click()
#        # Aguarda X segundos para execução do próximo comando
#        sleep(2)
#        # Captura a descrição da vaga na página
#        descricao = driver.find_element_by_class_name('description')
#        # Adiciona item a lista com a descrição da vaga
#        lista_descricoes.append(descricao.text)
#        # Transforma lista em texto
#        texto_descricao = '\n'.join(lista_descricoes)

    # Transforma lista em texto
    texto_descricao = '\n'.join(lista_descricoes)

    # Grava a variável texto_descricao em arquivo
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        f.write(texto_descricao)

    # Fecha o Google Chrome
    driver.quit()
    