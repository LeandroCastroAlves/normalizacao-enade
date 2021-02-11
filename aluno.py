import pandas as pd
import pyodbc
from conn import ConexaoDB


c = ConexaoDB()


def tabela_aluno():
    print("Criando tabela ALUNO.")
    c.executa_DML('''CREATE TABLE DBO.ALUNO(
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
    CONSTRAINT CK_TURNO_GRADUACAO CHECK (CO_TURNO_GRADUACAO IN (1,2,3,4,0)),
    CONSTRAINT FK_CO_CURSO FOREIGN KEY (CO_CURSO) REFERENCES dbo.CURSO (CO_CURSO),
    CONSTRAINT FK_UF_CONCLUSAO_EM FOREIGN KEY (UF_CONCLUSAO_EM) REFERENCES dbo.UF (CO_UF)
    );'''
                  )
    arquivo = 'dados/enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
    enade = pd.read_csv(arquivo, sep=";", decimal=".", error_bad_lines=False, index_col=False, dtype='unicode')
    df = enade[
        ["NU_ANO", "NU_IDADE", "TP_SEXO", "ANO_FIM_EM", "ANO_IN_GRAD", "CO_TURNO_GRADUACAO", "CO_CURSO", "QE_I01", "QE_I02",
         "QE_I03", "QE_I04", "QE_I05", "QE_I06", "QE_I07", "QE_I08", "QE_I09", "QE_I10", "QE_I11", "QE_I12", "QE_I13",
         "QE_I14", "QE_I15", "QE_I16", "QE_I17", "QE_I18", "QE_I19", "QE_I20", "QE_I21", "QE_I22", "QE_I23", "QE_I24",
         "QE_I25", "QE_I26", "NT_GER", "NT_FG", "NT_OBJ_FG", "NT_DIS_FG", "NT_FG_D1", "NT_FG_D1_PT", "NT_FG_D1_CT",
         "NT_FG_D2", "NT_FG_D2_PT", "NT_FG_D2_CT", "NT_CE", "NT_OBJ_CE", "NT_DIS_CE", "NT_CE_D1", "NT_CE_D2",
         "NT_CE_D3"]].fillna(0)
    print("Executando Replace tabela ALUNO | Questionarios.")
    a = {'A': 'Solteiro(a)', 'B': 'Casado(a)', 'C': 'Separado(a) judicialmente/divorciado(a)', 'D': 'Viúvo(a)',
         'E': 'Outro'}
    df["QE_I01"] = df["QE_I01"].map(a).fillna(0)
    a = {'A': 'Branca', 'B': 'Preta', 'C': 'Amarela', 'D': 'Parda', 'E': 'Indígena', 'F': 'Não quero declarar'}
    df["QE_I02"] = df["QE_I02"].map(a).fillna(0)
    a = {'A': 'Brasileira', 'B': 'Brasileira naturalizada', 'C': 'Estrangeira'}
    df["QE_I03"] = df["QE_I03"].map(a).fillna(0)
    a = {'A': 'Nenhuma', 'B': 'Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série)',
         'C': 'Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série)', 'D': 'Ensino Médio',
         'E': 'Ensino Superior - Graduação', 'F': 'Pós-graduação'}
    df["QE_I04"] = df["QE_I04"].map(a).fillna(0)
    a = {'A': 'Nenhuma', 'B': 'Ensino Fundamental: 1º ao 5º ano (1ª a 4ª série)',
         'C': 'Ensino Fundamental: 6º ao 9º ano (5ª a 8ª série)', 'D': 'Ensino médio',
         'E': 'Ensino Superior - Graduação', 'F': 'Pós-graduação'}
    df["QE_I05"] = df["QE_I05"].map(a).fillna(0)
    a = {'A': 'Em casa ou apartamento, sozinho', 'B': 'Em casa ou apartamento, com pais e/ou parentes',
         'C': 'Em casa ou apartamento, com cônjuge e/ou filhos',
         'D': 'Em casa ou apartamento, com outras pessoas (incluindo república)',
         'E': 'Em alojamento universitário da própria instituição',
         'F': 'Em outros tipos de habitação individual ou coletiva (hotel, hospedaria, pensão ou outro)'}
    df["QE_I06"] = df["QE_I06"].map(a).fillna(0)
    a = {'A': 'Nenhuma', 'B': 'Uma', 'C': 'Duas', 'D': 'Três', 'E': 'Quatro', 'F': 'Cinco', 'G': 'Seis',
         'H': 'Sete ou mais'}
    df["QE_I07"] = df["QE_I07"].map(a).fillna(0)
    a = {'A': 'Até 1,5 salário mínimo (até R$ 1431,00)', 'B': 'De 1,5 a 3 salários mínimos (R$ 1431,01 a R$ 2862,00)',
         'C': 'De 3 a 4,5 salários mínimos (R$ 2862,01 a R$ 4293,00)',
         'D': 'De 4,5 a 6 salários mínimos (R$ 4293,01 a R$ 5724,00)',
         'E': 'De 6 a 10 salários mínimos (R$ 5724,01 a R$ 9540,00)',
         'F': 'De 10 a 30 salários mínimos (R$ 9540,01 a R$ 28620,00)',
         'G': 'Acima de 30 salários mínimos (mais de R$ 28620,00)'}
    df["QE_I08"] = df["QE_I08"].map(a).fillna(0)
    a = {'A': 'Não tenho renda e meus gastos são financiados por programas governamentais',
         'B': 'Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas',
         'C': 'Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos',
         'D': 'Tenho renda e não preciso de ajuda para financiar meus gastos',
         'E': 'Tenho renda e contribuo com o sustento da família',
         'F': 'Sou o principal responsável pelo sustento da família'}
    df["QE_I09"] = df["QE_I09"].map(a).fillna(0)
    a = {'A': 'Não estou trabalhando', 'B': 'Trabalho eventualmente', 'C': 'Trabalho até 20 horas semanais',
         'D': 'Trabalho de 21 a 39 horas semanais', 'E': 'Trabalho 40 horas semanais ou mais'}
    df["QE_I10"] = df["QE_I10"].map(a).fillna(0)
    a = {'A': 'Nenhum, pois meu curso é gratuito', 'B': 'Nenhum, embora meu curso não seja gratuito',
         'C': 'ProUni integral', 'D': 'ProUni parcial, apenas', 'E': 'FIES, apenas', 'F': 'ProUni Parcial e FIES',
         'G': 'Bolsa oferecida por governo estadual, distrital ou municipal',
         'H': 'Bolsa oferecida pela própria instituição',
         'I': 'Bolsa oferecida por outra entidade (empresa, ONG, outra)',
         'J': 'Financiamento oferecido pela própria instituição', 'K': 'Financiamento bancário'}
    df["QE_I11"] = df["QE_I11"].map(a).fillna(0)
    a = {'A': 'Nenhum', 'B': 'Auxílio moradia', 'C': 'Auxílio alimentação', 'D': 'Auxílio moradia e alimentação',
         'E': 'Auxílio Permanência', 'F': 'Outro tipo de auxílio'}
    df["QE_I12"] = df["QE_I12"].map(a).fillna(0)
    a = {'A': 'Nenhum', 'B': 'Bolsa de iniciação científica', 'C': 'Bolsa de extensão',
         'D': 'Bolsa de monitoria/tutoria', 'E': 'Bolsa PET', 'F': 'Outro tipo de bolsa acadêmica'}
    df["QE_I13"] = df["QE_I13"].map(a).fillna(0)
    a = {'A': 'Não participei', 'B': 'Sim, Programa Ciência sem Fronteiras',
         'C': 'Sim, programa de intercâmbio financiado pelo Governo Federal (Marca; Brafitec; PLI; outro)',
         'D': 'Sim, programa de intercâmbio financiado pelo Governo Estadual',
         'E': 'Sim, programa de intercâmbio da minha instituição', 'F': 'Sim, outro intercâmbio não institucional'}
    df["QE_I14"] = df["QE_I14"].map(a).fillna(0)
    a = {'A': 'Não', 'B': 'Sim, por critério étnico-racial', 'C': 'Sim, por critério de renda',
         'D': 'Sim, por ter estudado em escola pública ou particular com bolsa de estudos',
         'E': 'Sim, por sistema que combina dois ou mais critérios anteriores',
         'F': 'Sim, por sistema diferente dos anteriores'}
    df["QE_I15"] = df["QE_I15"].map(a).fillna(0)
    a = {'A': 'Todo em escola pública', 'B': 'Todo em escola privada (particular)', 'C': 'Todo no exterior',
         'D': 'A maior parte em escola pública', 'E': 'A maior parte em escola privada (particular)',
         'F': 'Parte no Brasil e parte no exterior'}
    df["QE_I17"] = df["QE_I17"].map(a).fillna(0)
    a = {'A': 'Ensino médio tradicional',
         'B': 'Profissionalizante técnico (eletrônica, contabilidade, agrícola, outro)',
         'C': 'Profissionalizante magistério (Curso Normal)', 'D': 'Educação de Jovens e Adultos (EJA) e/ou Supletivo',
         'E': 'Outro modalidade'}
    df["QE_I18"] = df["QE_I18"].map(a).fillna(0)
    a = {'A': 'Ninguém', 'B': 'Pais', 'C': 'Outros membros da família que não os pais', 'D': 'Professores',
         'E': 'Líder ou representante religioso', 'F': 'Colegas/Amigos', 'G': 'Outras pessoas'}
    df["QE_I19"] = df["QE_I19"].map(a).fillna(0)
    a = {'A': 'Não tive dificuldade', 'B': 'Não recebi apoio para enfrentar dificuldades', 'C': 'Pais', 'D': 'Avós',
         'E': 'Irmãos, primos ou tios', 'F': 'Líder ou representante religioso', 'G': 'Colegas de curso ou amigos',
         'H': 'Professores do curso', 'I': 'Profissionais do serviço de apoio ao estudante da IES',
         'J': 'Colegas de trabalho', 'K': 'Outro grupo'}
    df["QE_I20"] = df["QE_I20"].map(a).fillna(0)
    a = {'A': 'Sim', 'B': 'Não'}
    df["QE_I21"] = df["QE_I21"].map(a).fillna(0)
    a = {'A': 'Nenhum', 'B': 'Um ou dois', 'C': 'De três a cinco', 'D': 'De seis a oito', 'E': 'Mais de oito'}
    df["QE_I22"] = df["QE_I22"].map(a).fillna(0)
    a = {'A': 'Nenhuma, apenas assisto às aulas', 'B': 'De uma a três', 'C': 'De quatro a sete', 'D': 'De oito a doze',
         'E': 'Mais de doze'}
    df["QE_I23"] = df["QE_I23"].map(a).fillna(0)
    a = {'A': 'Sim, somente na modalidade presencial', 'B': 'Sim, somente na modalidade semipresencial',
         'C': 'Sim, parte na modalidade presencial e parte na modalidade semipresencial',
         'D': 'Sim, na modalidade a distância', 'E': 'Não'}
    df["QE_I24"] = df["QE_I24"].map(a).fillna(0)
    a = {'A': 'Inserção no mercado de trabalho', 'B': 'Influência familiar', 'C': 'Valorização profissional',
         'D': 'Prestígio Social', 'E': 'Vocação', 'F': 'Oferecido na modalidade a distância',
         'G': 'Baixa concorrência para ingresso', 'H': 'Outro motivo'}
    df["QE_I25"] = df["QE_I25"].map(a).fillna(0)
    a = {'A': 'Gratuidade', 'B': 'Preço da mensalidade', 'C': 'Proximidade da minha residência',
         'D': 'Proximidade do meu trabalho', 'E': 'Facilidade de acesso', 'F': 'Qualidade/reputação',
         'G': 'Foi a única onde tive aprovação', 'H': 'Possibilidade de ter bolsa de estudo', 'I': 'Outro motivo'}
    df["QE_I26"] = df["QE_I26"].map(a).fillna(0)
    # FIM ALTERACAO VALOR QUESTIONARIO
    print("Carregando tabela ALUNO.")
    for index, row in df.iterrows():
        c.executa_DML_PR(
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
    print("Normalização Concluida Com Sucesso!")


