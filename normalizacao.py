import pandas as pd
from conn import ConexaoDB
from aluno import tabela_aluno
c = ConexaoDB()

arquivo = 'dados/enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
enade = pd.read_csv(arquivo, sep=";", decimal=".", error_bad_lines=False, index_col=False, dtype='unicode')
dados_grupo_curso = pd.read_csv('grupo_cursos.csv', sep=";")
server = 'ESTAGIO1-PC\SQLEXPRESS'


def categ_adm_ies():
    c.executa_DML('''CREATE TABLE DBO.CATEG_ADM_IES(
    CO_CATEG_ADM_IES INT NOT NULL PRIMARY KEY,
    DESCRICAO VARCHAR(100),
    ENTIDADE VARCHAR(100),
    ORGANIZACAO VARCHAR(100),
    ADM_EST VARCHAR(50)
    );
    INSERT INTO DBO.CATEG_ADM_IES VALUES (93,'Pessoa Jurídica de Direito Público','NA','NA','Federal');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (115,'Pessoa Jurídica de Direito Público','NA','NA','Estadual');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (116,'Pessoa Jurídica de Direito Público','NA','NA','Municipal');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (118,'Pessoa Jurídica de Direito Privado','Com fins lucrativos','Sociedade Civil','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (120,'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Associação de Utilidade Pública',  'NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (121,'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Fundação','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10001,'Pessoa Jurídica de Direito Público','NA','NA','Estadual');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10002,'Pessoa Jurídica de Direito Público','NA','NA','Federal');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10003,'Pessoa Jurídica de Direito Público','NA','NA','Municipal');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10005,'Privada','Com fins lucrativos','NA','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10006,'Pessoa Jurídica de Direito Privado','Com fins lucrativos','Sociedade Mercantil ou Comercial','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10007,'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Associação de Utilidade Pública','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10008,'Privada','Sem fins lucrativos','NA','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (10009,'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Sociedade','NA');
    INSERT INTO DBO.CATEG_ADM_IES VALUES (17634,'Fundação Pública de Direito Privado Municipal','NA','NA','NA');
    ''')

def org_ac_ies():
    c.executa_DML('''
    CREATE TABLE ORG_AC_IES(
    CO_ORG_AC_IES INT NOT NULL PRIMARY KEY,
    DESCRICAO VARCHAR(100) 
    );
    INSERT INTO ORG_AC_IES VALUES (10019,'Centro Federal de Educação Tecnológica');
    INSERT INTO ORG_AC_IES VALUES (10020,'Centro Universitário');
    INSERT INTO ORG_AC_IES VALUES (10022,'Faculdade');
    INSERT INTO ORG_AC_IES VALUES (10026,'Instituto Federal de Educação, Ciência e Tecnologia');
    INSERT INTO ORG_AC_IES VALUES (10028,'Universidade');
    ''')

def ies():
    c.executa_DML('''CREATE TABLE DBO.IES(
    CO_IES INT NOT NULL PRIMARY KEY,
    CO_CATEG_ADM_IES INT NOT NULL,
    CO_ORG_AC_IES INT NOT NULL,
    CONSTRAINT FK_IES_CATEG FOREIGN KEY (CO_CATEG_ADM_IES) REFERENCES dbo.CATEG_ADM_IES(CO_CATEG_ADM_IES),
    CONSTRAINT FK_IES_ORG FOREIGN KEY (CO_ORG_AC_IES) REFERENCES dbo.ORG_AC_IES(CO_ORG_AC_IES)
        );
        ''')
    ies = enade[["CO_IES","CO_CATEGAD","CO_ORGACAD"]]
    ies_drop_duplicates = ies.drop_duplicates()  # valores duplicados por causa de outras colunas, retirados
    for index, row in ies_drop_duplicates.iterrows():
        c.executa_DML_PR(
            '''INSERT INTO dbo.ies (CO_IES,CO_CATEG_ADM_IES,CO_ORG_AC_IES) values (?, ?, ?)''',
                (row.CO_IES, row.CO_CATEGAD, row.CO_ORGACAD)
        )
def grupo_curso():
    c.executa_DML('''CREATE TABLE DBO.GRUPO_CURSO(
    CO_GRUPO INT NOT NULL,
    DESCRICAO VARCHAR (100),
    );''')
    for index, row in dados_grupo_curso.iterrows():
        c.executa_DML_PR(
            "INSERT INTO dbo.grupo_curso (CO_GRUPO, DESCRICAO) values (?, ?)",
            (row.CO_GRUPO, row.DESCRICAO)
        )


def curso():
    c.executa_DML('''CREATE TABLE DBO.CURSO(
    CO_CURSO INT NOT NULL,
    CO_GRUPO_CURSO INT NOT NULL,
    CO_IES INT NOT NULL,
    CO_MUNIC	int NOT NULL,
    CO_MODALIDADE  INT NOT NULL,
    CONSTRAINT PK_CO_CURSO PRIMARY KEY (CO_CURSO),
    CONSTRAINT FK_CURSO_GRUPO FOREIGN KEY (CO_GRUPO_CURSO) REFERENCES dbo.GRUPO_CURSO (CO_GRUPO_CURSO),
    CONSTRAINT FK_CURSO_IES FOREIGN KEY (CO_IES) REFERENCES dbo.IES (CO_IES),
    CONSTRAINT FK_CURSO_MUNIC FOREIGN KEY (CO_MUNIC) REFERENCES dbo.MUNIC (CO_MUNIC),
    CONSTRAINT CK_MODALIDADE CHECK (CO_MODALIDADE IN (0 , 1)) -- 0 = EaD , 1 = Presencial
    );''')
    enade_ies = enade[["CO_CURSO", "CO_GRUPO","CO_IES", "CO_MUNIC_CURSO", "CO_MODALIDADE"]]
    enade_ies_drop_duplicates = enade_ies.drop_duplicates().sort_index() # valores duplicados por causa de outras colunas, retirados
    for index, row in enade_ies_drop_duplicates.iterrows():
        c.executa_DML_PR(
            "INSERT INTO dbo.curso (CO_CURSO, CO_GRUPO,CO_IES, CO_MUNIC, CO_MODALIDADE) values (?, ?, ?, ?, ?)",
                (row.CO_CURSO, row.CO_GRUPO, row.CO_IES, row.CO_MUNIC_CURSO, row.CO_MODALIDADE)
        )


