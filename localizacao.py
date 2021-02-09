import pandas as pd
import numpy as np
import pyodbc
import requests
import json

server = 'ESTAGIO1-PC\SQLEXPRESS'
database = 'enade'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
dados = pd.read_csv('localizacao.csv', sep=";")

def regiao():
    cursor.execute('''CREATE TABLE DBO.REGIAO(
    CO_REGIAO INT PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(100),
    SIGLA VARCHAR(5)
    );''')
    cnxn.commit()
    regiao = dados[["CO_REGIAO","DESCRICAO_REGIAO","SIGLA_REGIAO"]]
    regiao_drop_duplicates = regiao.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in regiao_drop_duplicates.iterrows():
        cursor.execute(
            "INSERT INTO dbo.regiao (CO_REGIAO,DESCRICAO,SIGLA) values (?, ?, ?)",
                (row.CO_REGIAO, row.DESCRICAO_REGIAO, row.SIGLA_REGIAO)
        )
        cnxn.commit()
    cursor.execute("INSERT INTO dbo.regiao (CO_REGIAO,DESCRICAO,SIGLA) values (0, 'NA', 'NA')")
    cnxn.commit()
def uf():
    cursor.execute('''CREATE TABLE DBO.UF(
    CO_UF INT PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(100),
    SIGLA VARCHAR(5), 
    CO_REGIAO INT NOT NULL,
    CONSTRAINT PK_UF_REGIAO FOREIGN KEY(CO_REGIAO) REFERENCES dbo.REGIAO(CO_REGIAO));''')
    cnxn.commit()
    uf = dados[["CO_UF","DESCRICAO_UF","SIGLA_UF", "CO_REGIAO"]]
    uf_drop_duplicates = uf.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in uf_drop_duplicates.iterrows():
        cursor.execute(
            '''INSERT INTO dbo.uf (CO_UF,DESCRICAO,SIGLA,CO_REGIAO) values (?, ?, ?, ?)''',
                (row.CO_UF, row.DESCRICAO_UF, row.SIGLA_UF, row.CO_REGIAO)
        )
        cnxn.commit()
    cursor.execute('''INSERT INTO dbo.uf (CO_UF,DESCRICAO,SIGLA,CO_REGIAO) values (0, 'NA', 'NA', 0)''')
    cnxn.commit()
def munic():
    cursor.execute('''CREATE TABLE MUNIC(CO_MUNIC INT PRIMARY KEY NOT NULL, 
    DESCRICAO VARCHAR(100), 
    CO_UF INT,
    CONSTRAINT PK_MUNIC_UF FOREIGN KEY (CO_UF) REFERENCES dbo.UF(CO_UF))
    ;''')
    cnxn.commit()
    munic = dados[["CO_MUNIC","DESCRICAO_MUNIC","CO_UF"]]
    for index, row in munic.iterrows():
        cursor.execute(
            "INSERT INTO dbo.munic (CO_MUNIC,DESCRICAO,CO_UF) values (?, ?, ?)",
                (row.CO_MUNIC, row.DESCRICAO_MUNIC, row.CO_UF)
        )
        cnxn.commit()

