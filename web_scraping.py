from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd

enade_html = requests.get('https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enade')
soup = BeautifulSoup(enade_html.text, 'html.parser')
classe_ex_lk = soup.find_all(class_="external-link")
def carrega_dados_bruto():
    if os.path.isfile('links_dowload.csv'):
        print('Links ok')
    else:
        f = csv.writer(open('links_dowload.csv', 'w', newline='', encoding='utf-8'))
        f.writerow(['Name', 'Link'])
        for i in classe_ex_lk:
            nome = i.contents[0]
            link = i.get('href')
            f.writerow([nome, link])


def extrai_link_zip:
    df = pd.read_csv('links_dowload.csv', sep=',')
    df_link = df["Link"]
    l = csv.writer(open('links_zip.csv', 'w', newline='', encoding='utf-8'))
    for i in range(len(df_link)):
        if df_link.loc[i].endswith(".zip"):
            l.writerow([df_link.loc[i]])
    os.remove('links_dowload.csv')

print()
