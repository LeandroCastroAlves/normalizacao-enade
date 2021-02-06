import pandas as pd
import pyodbc

arquivo = 'enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
enade = pd.read_csv(arquivo, sep=";", decimal=".", error_bad_lines=False, index_col=False, dtype='unicode')
server = 'ESTAGIO1-PC\SQLEXPRESS'
database = 'enade'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

def replace_questionario():
    enade_replace_q = enade[["QE_I01", "QE_I02", "QE_I03", "QE_I04", "QE_I05", "QE_I06", "QE_I07", "QE_I08", "QE_I09", "QE_I10", "QE_I11", "QE_I12", "QE_I13", "QE_I14", "QE_I15", "QE_I16", "QE_I17", "QE_I18", "QE_I19", "QE_I20", "QE_I21", "QE_I22", "QE_I23", "QE_I24", "QE_I25", "QE_I26"]]
    a = {'A' : 'Solteiro(a)', 'B' : 'Casado(a)', 'C' : '(a) judicialmente/divorciado(a)', 'D' : 'Viúvo(a)','E' : 'Outro'}
    enade_replace_q["QE_I01"] = enade_replace_q["QE_I01"].map(a).fillna(0)
    print(enade_replace_q.head())

def presenca():
    enade_pres = enade[["TP_PRES","TP_PR_GER","TP_PR_OB_FG","TP_PR_DI_FG","TP_PR_OB_CE","TP_PR_DI_CE"]]
    for index, row in enade_pres.iterrows():
        cursor.execute(
            "INSERT INTO dbo.presenca (ID_ALUNO, TP_PRES, TP_PR_GER, TP_PR_OB_FG, TP_PR_DI_FG, TP_PR_OB_CE, TP_PR_DI_CE) values (?, ?, ?, ?, ?, ?, ?)",
                (index, row.TP_PRES, row.TP_PR_GER, row.TP_PR_OB_FG, row.TP_PR_DI_FG, row.TP_PR_OB_CE, row.TP_PR_DI_CE)
        )
        cnxn.commit()


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

def aluno():
    enade_aluno = enade[["NU_IDADE", "TP_SEXO", "ANO_FIM_EM", "ANO_IN_GRAD", "CO_TURNO_GRADUACAO", "TP_INSCRICAO_ADM", "TP_INSCRICAO", "CO_CURSO"]]
    enade_aluno = enade_aluno.fillna(0) # trocando valores nulos por 0
    for index, row in enade_aluno.iterrows():
        cursor.execute(
            "INSERT INTO dbo.aluno (ID_ALUNO, NU_IDADE, TP_SEXO, ANO_FIM_EM, ANO_IN_GRAD, CO_TURNO_GRADUACAO, TP_INSCRICAO_ADM, TP_INSCRICAO, CO_CURSO) values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (index, row.NU_IDADE, row.TP_SEXO, row.ANO_FIM_EM, row.ANO_IN_GRAD, row.CO_TURNO_GRADUACAO, row.TP_INSCRICAO_ADM, row.TP_INSCRICAO, row.CO_CURSO)
        )
        cnxn.commit()


replace_questionario()



#enade_ies = enade[["CO_IES","CO_CATEGAD","CO_ORGACAD","CO_GRUPO","CO_CURSO","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"]]
#print(enade_ies.head())
#enade_ies_drop_duplicates = enade_ies.drop_duplicates(subset=["CO_IES", "CO_CATEGAD","CO_ORGACAD","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"])
#print(enade_ies_drop_duplicates.head())

#enade_ies = enade[["CO_GRUPO","CO_CURSO","CO_MODALIDADE","CO_MUNIC_CURSO","CO_UF_CURSO","CO_REGIAO_CURSO"]]
#print(enade_ies)
#enade_ies_d = enade_ies.drop_duplicates()
#print(enade_ies_d)