import pandas as pd
import pyodbc


arquivo = 'dados/enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
enade = pd.read_csv(arquivo, sep=";", decimal=".", error_bad_lines=False, index_col=False, dtype='unicode')
server = 'ESTAGIO1-PC\SQLEXPRESS'

database = 'enade'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()


def ies():
    enade_ies = enade[["CO_IES","CO_CATEGAD","CO_ORGACAD"]]
    enade_ies_drop_duplicates = enade_ies.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in enade_ies_drop_duplicates.iterrows():
        cursor.execute(
            "INSERT INTO dbo.ies (CO_IES,CO_CATEGAD,CO_ORGACAD) values (?, ?, ?)",
                (row.CO_IES, row.CO_CATEGAD, row.CO_ORGACAD)
        )
        cnxn.commit()

def curso():
    enade_ies = enade[["CO_CURSO", "CO_GRUPO","CO_IES", "CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO", "CO_MODALIDADE"]]
    enade_ies_drop_duplicates = enade_ies.drop_duplicates() # valores duplicados por causa de outras colunas, retirados
    for index, row in enade_ies_drop_duplicates.iterrows():
        cursor.execute(
            "INSERT INTO dbo.curso (CO_CURSO, CO_GRUPO,CO_IES, CO_MUNIC_CURSO,CO_UF_CURSO,CO_REGIAO_CURSO, CO_MODALIDADE) values (?, ?, ?, ?, ?, ?, ?)",
                (row.CO_CURSO, row.CO_GRUPO, row.CO_IES, row.CO_MUNIC_CURSO, row.CO_UF_CURSO, row.CO_REGIAO_CURSO, row.CO_MODALIDADE)
        )
        cnxn.commit()






