import pandas as pd
import zipfile
import requests
from io import BytesIO
import os
import pyodbc



diretorio = './enade2017'
arquivo = 'enade2017/microdados_enade_2017/2017/3.DADOS/microdados_Enade_2017_portal_2018.10.09.zip'

def verifica_arquivo_diretorio():
    diretorio = './enade2017'
    arquivo = 'enade2017/microdados_enade_2017/2017/3.DADOS/microdados_Enade_2017_portal_2018.10.09.zip'
    if os.path.isdir(diretorio):
        print('Diretorio', diretorio, 'já existe')
    else:
        os.makedirs('./enade2017')
    if os.path.isfile(arquivo):
        print('Arquivo', arquivo,' já existe')
    else:
        url = "https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2017.zip"
        arquivo = BytesIO(requests.get(url).content)
    # extrai conteudo do do arquivo
        zip = zipfile.ZipFile(arquivo)
        zip.extractall(diretorio)

def conex():
    try:
        server = 'ESTAGIO1-PC\SQLEXPRESS'
        database = 'enade'
        username = ''
        password = ''
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        cursor = cnxn.cursor()
        print("ok")
    except pyodbc.Error as r:
        print(r)