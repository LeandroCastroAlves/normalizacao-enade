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


def tabela_aluno():
    tabela_aluno = '''CREATE TABLE DBO.ALUNO(
    ID_ALUNO    int NOT NULL,
    ANO_PROVA int,
    NU_IDADE    int,
    TP_SEXO varchar(2),
    ANO_FIM_EM  int,
    ANO_IN_GRAD int,
    CO_TURNO_GRADUACAO  int,
    TP_INSCRICAO_ADM    int,
    TP_INSCRICAO    int,
    CO_CURSO int,
    ESTADO_CIVIL VARCHAR(200),
    COR_RACA VARCHAR(200),
    NACIONALIDADE VARCHAR(200),
    ESCOLARIDADE_PAI VARCHAR(200),
    ESCOLARIDADE_MAE VARCHAR(200),
    MORADIA VARCHAR(200),
    QTD_MORADORES VARCHAR(200),
    RENDA_FAMILIAR VARCHAR(200),
    SITUACAO_FINANCEIRA VARCHAR(200),
    SITUACAO_TRABALHO VARCHAR(200),
    BOLSA_ESTUDO VARCHAR(200),
    BOLSA_PERMANENCIA VARCHAR(200),
    BOLSA_ACADEMICA VARCHAR(200),
    BOLSA_PROGRAMA_EXTERIOR VARCHAR(200),
    INGRESSO_ACAO_AFIRMATIVA VARCHAR(200),
    UF_CONCLUSAO_EM int,
    TIPO_ESCOLA_EM VARCHAR(200),
    MODALIDADE_EM VARCHAR(200),
    QE_I19 VARCHAR(200),
    QE_I20 VARCHAR(200),
    FAMILIARES_EN_SUP VARCHAR(200),
    LIVROS_LIDO_ANO VARCHAR(200),
    H_SEMANA_ESTUDO VARCHAR(200),
    IDIOMA_ESTRANGEIRO_IES VARCHAR(200),
    MOTIVO_ESCOLHA_CURSO VARCHAR(200),
    RAZAO_ESCOLHA_IES VARCHAR(200),
    NT_GER varchar(10),
    NT_FG varchar(10),
    NT_OBJ_FG varchar(10),
    NT_DIS_FG varchar(10),
    NT_FG_D1 varchar(10),
    NT_FG_D1_PT varchar(10),
    NT_FG_D1_CT varchar(10),
    NT_FG_D2 varchar(10),
    NT_FG_D2_PT varchar(10),
    NT_FG_D2_CT varchar(10),
    NT_CE varchar(10),
    NT_OBJ_CE varchar(10),
    NT_DIS_CE varchar(10),
    NT_CE_D1 varchar(10),
    NT_CE_D2 varchar(10),
    NT_CE_D3 varchar(10),
    CONSTRAINT PK_ALUNO PRIMARY KEY (ID_ALUNO),
    CONSTRAINT CK_TP_SEXO CHECK (TP_SEXO IN ('M', 'F')),
    CONSTRAINT CK_TURNO_GRADUACAO CHECK (CO_TURNO_GRADUACAO IN (1,2,3,4)),
    CONSTRAINT FK_CO_CURSO FOREIGN KEY (CO_CURSO) REFERENCES dbo.CURSO (CO_CURSO),
    CONSTRAINT FK_UF_CONCLUSAO_EM FOREIGN KEY (UF_CONCLUSAO_EM) REFERENCES dbo.UF (CO_UF)
    );'''
    cursor.execute(tabela_aluno)
    cnxn.commit()
    enade_pres = enade[
        ["NU_ANO", "NU_IDADE", "TP_SEXO", "ANO_FIM_EM", "ANO_IN_GRAD", "CO_TURNO_GRADUACAO", "CO_CURSO", "QE_I01", "QE_I02",
         "QE_I03", "QE_I04", "QE_I05", "QE_I06", "QE_I07", "QE_I08", "QE_I09", "QE_I10", "QE_I11", "QE_I12", "QE_I13",
         "QE_I14", "QE_I15", "QE_I16", "QE_I17", "QE_I18", "QE_I19", "QE_I20", "QE_I21", "QE_I22", "QE_I23", "QE_I24",
         "QE_I25", "QE_I26", "NT_GER", "NT_FG", "NT_OBJ_FG", "NT_DIS_FG", "NT_FG_D1", "NT_FG_D1_PT", "NT_FG_D1_CT",
         "NT_FG_D2", "NT_FG_D2_PT", "NT_FG_D2_CT", "NT_CE", "NT_OBJ_CE", "NT_DIS_CE", "NT_CE_D1", "NT_CE_D2",
         "NT_CE_D3"]].fillna(0)
    for index, row in enade_pres.iterrows():
        cursor.execute(
            "INSERT INTO DBO.ALUNO (ID_ALUNO,ANO_PROVA,NU_IDADE,TP_SEXO,ANO_FIM_EM,ANO_IN_GRAD,CO_TURNO_GRADUACAO,CO_CURSO,ESTADO_CIVIL,COR_RACA,NACIONALIDADE,ESCOLARIDADE_PAI,ESCOLARIDADE_MAE,MORADIA,QTD_MORADORES,RENDA_FAMILIAR,SITUACAO_FINANCEIRA,SITUACAO_TRABALHO,BOLSA_ESTUDO,BOLSA_PERMANENCIA,BOLSA_ACADEMICA,BOLSA_PROGRAMA_EXTERIOR,INGRESSO_ACAO_AFIRMATIVA,"
            "UF_CONCLUSAO_EM,TIPO_ESCOLA_EM,MODALIDADE_EM,QE_I19,QE_I20,FAMILIARES_EN_SUP,LIVROS_LIDO_ANO,H_SEMANA_ESTUDO,IDIOMA_ESTRANGEIRO_IES,MOTIVO_ESCOLHA_CURSO,RAZAO_ESCOLHA_IES,NT_GER,NT_FG,NT_OBJ_FG,NT_DIS_FG,NT_FG_D1,NT_FG_D1_PT,NT_FG_D1_CT,NT_FG_D2,NT_FG_D2_PT,NT_FG_D2_CT,NT_CE,NT_OBJ_CE,NT_DIS_CE,NT_CE_D1,NT_CE_D2,NT_CE_D3)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (index, row.NU_ANO, row.NU_IDADE, row.TP_SEXO, row.ANO_FIM_EM, row.ANO_IN_GRAD,
                row.CO_TURNO_GRADUACAO, row.CO_CURSO, row.QE_I01, row.QE_I02, row.QE_I03, row.QE_I04, row.QE_I05, row.QE_I06, row.QE_I07,
                row.QE_I08, row.QE_I09, row.QE_I10, row.QE_I11, row.QE_I12, row.QE_I13, row.QE_I14, row.QE_I15, row.QE_I16,
                row.QE_I17, row.QE_I18, row.QE_I19, row.QE_I20, row.QE_I21, row.QE_I22, row.QE_I23, row.QE_I24, row.QE_I25,
                row.QE_I26, row.NT_GER, row.NT_FG, row.NT_OBJ_FG, row.NT_DIS_FG, row.NT_FG_D1, row.NT_FG_D1_PT,
                row.NT_FG_D1_CT, row.NT_FG_D2, row.NT_FG_D2_PT, row.NT_FG_D2_CT, row.NT_CE, row.NT_OBJ_CE, row.NT_DIS_CE,
                row.NT_CE_D1, row.NT_CE_D2, row.NT_CE_D3))
        cnxn.commit()


tabela_aluno()