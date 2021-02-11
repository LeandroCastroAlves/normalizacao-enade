import pandas as pd
from conn import ConexaoDB
c = ConexaoDB()
dados = pd.read_csv('localizacao.csv', sep=";")

def regiao():
    print("Criando tabela REGIAO.")
    c.executa_DML('''CREATE TABLE DBO.REGIAO(
    CO_REGIAO INT PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(100),
    SIGLA VARCHAR(5)
    );''')
    print("Carregando tabela REGIAO.")
    regiao = dados[["CO_REGIAO","DESCRICAO_REGIAO","SIGLA_REGIAO"]].sort_index()
    regiao_drop_duplicates = regiao.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in regiao_drop_duplicates.iterrows():
        c.executa_DML_PR(
            "INSERT INTO dbo.regiao (CO_REGIAO,DESCRICAO,SIGLA) values (?, ?, ?)",
                (row.CO_REGIAO, row.DESCRICAO_REGIAO, row.SIGLA_REGIAO)
        )
    c.executa_DML("INSERT INTO dbo.regiao (CO_REGIAO,DESCRICAO,SIGLA) values (0, 'NA', 'NA')")

def uf():
    print("Criando tabela UF.")
    c.executa_DML('''CREATE TABLE DBO.UF(
    CO_UF INT PRIMARY KEY NOT NULL,
    DESCRICAO VARCHAR(100),
    SIGLA VARCHAR(5), 
    CO_REGIAO INT NOT NULL,
    CONSTRAINT FK_UF_REGIAO FOREIGN KEY(CO_REGIAO) REFERENCES dbo.REGIAO(CO_REGIAO));''')
    print("Carregando tabela UF.")
    uf = dados[["CO_UF","DESCRICAO_UF","SIGLA_UF", "CO_REGIAO"]].sort_index()
    uf_drop_duplicates = uf.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in uf_drop_duplicates.iterrows():
        c.executa_DML_PR(
            '''INSERT INTO dbo.uf (CO_UF,DESCRICAO,SIGLA,CO_REGIAO) values (?, ?, ?, ?)''',
                (row.CO_UF, row.DESCRICAO_UF, row.SIGLA_UF, row.CO_REGIAO)
        )
    c.executa_DML('''INSERT INTO dbo.uf (CO_UF,DESCRICAO,SIGLA,CO_REGIAO) values (0, 'NA', 'NA', 0);
                     INSERT INTO dbo.uf (CO_UF,DESCRICAO,SIGLA,CO_REGIAO) values (99, 'NA', 'NA', 0);''')

def munic():
    print("Criando tabela MUNIC.")
    c.executa_DML('''CREATE TABLE MUNIC(CO_MUNIC INT PRIMARY KEY NOT NULL, 
    DESCRICAO VARCHAR(100), 
    CO_UF INT,
    CONSTRAINT FK_MUNIC_UF FOREIGN KEY (CO_UF) REFERENCES dbo.UF(CO_UF))
    ;''')
    print("Carregando tabela MUNIC.")
    munic = dados[["CO_MUNIC","DESCRICAO_MUNIC","CO_UF"]].sort_index()
    for index, row in munic.iterrows():
        c.executa_DML_PR(
            "INSERT INTO dbo.munic (CO_MUNIC,DESCRICAO,CO_UF) values (?, ?, ?)",
                (row.CO_MUNIC, row.DESCRICAO_MUNIC, row.CO_UF)
        )

