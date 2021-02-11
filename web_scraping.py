# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd
from io import BytesIO
import zipfile

def carrega_dados_bruto():
    enade_html = requests.get('https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade')
    print("Extraindo Link de ", enade_html.url)
    soup = BeautifulSoup(enade_html.text, 'html.parser')
    classe_ex_lk = soup.find_all(class_="external-link")
    if os.path.isfile('links_dowload.csv'):
        print('Links ok')
    else:
        f = csv.writer(open('links_dowload.csv', 'w', newline='', encoding='utf-8'))
        f.writerow(['Name', 'Link'])
        for i in classe_ex_lk:
            nome = i.contents[0]
            link = i.get('href')
            f.writerow([nome, link])

def extrai_link_zip():
    print("extrindo links .zip")
    df = pd.read_csv('links_dowload.csv', sep=',')
    df_link = df["Link"]
    l = csv.writer(open('links_zip.csv', 'w', newline='', encoding='utf-8'))
    l.writerow(['Link'])
    for i in range(len(df_link)):
        if df_link.loc[i].endswith(".zip"):
            l.writerow([df_link.loc[i]])
    os.remove('links_dowload.csv')

def verifica_arquivo_diretorio():
    print("Verificando diretorio e concluindo dowload de arquivos. Aguarde...")
    diretorio = './dados/enade2019'
    arquivo = './dados/enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
    if os.path.isdir(diretorio):
        print('Diretorio', diretorio, 'já existe')
    else:
        os.makedirs('./dados/enade2019')
    if os.path.isfile(arquivo):
        print('Arquivo', arquivo,' já existe')
    else:
        df = pd.read_csv('links_zip.csv')
        url = df[df['Link'].str.contains("2019")].values
        arquivo = BytesIO(requests.get(url.item()).content)
        zip = zipfile.ZipFile(arquivo)
        zip.extractall(diretorio)
        print("Dowload de arquivos concluido com sucesso!")



