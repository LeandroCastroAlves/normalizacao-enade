import pandas as pd

def replace_questionario():
    arquivo = 'enade2019/microdados_enade_2019/2019/3.DADOS/microdados_enade_2019.txt'
    enade = pd.read_csv(arquivo, sep=";", decimal=".", error_bad_lines=False, index_col=False, dtype='unicode')
    server = 'ESTAGIO1-PC\SQLEXPRESS'
    df = enade[
        ["QE_I01", "QE_I02", "QE_I03", "QE_I04", "QE_I05", "QE_I06", "QE_I07", "QE_I08", "QE_I09", "QE_I10", "QE_I11",
         "QE_I12", "QE_I13", "QE_I14", "QE_I15", "QE_I16", "QE_I17", "QE_I18", "QE_I19", "QE_I20", "QE_I21", "QE_I22",
         "QE_I23", "QE_I24", "QE_I25", "QE_I26"]]
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
    print(df)