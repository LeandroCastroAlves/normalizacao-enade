CREATE DATABASE DB;

-- CRIAÇÃO TABELA DO TIPO DE PRESENÇA
CREATE TABLE DB.DBO.TIPO_PRESENCA(
CODIGO varchar(3),
DESCRICAO varchar(100)
/*222  Não se aplica (estudante ausente)**
333  Prova em branco (estudante presente)*
555  Prova com resultado considerado válido*
556  Prova com resultado desconsiderado pela Aplicadora**
Nota: (*) resultado considerado para o cálculo da nota do estudante; (**) resultado desconsiderado para o cálculo da nota do estudante.*/
);
INSERT INTO TIPO_PRESENCA VALUES ('222', 'Não se aplica (estudante ausente)');
INSERT INTO TIPO_PRESENCA VALUES ('333', 'Prova em branco (estudante presente)');
INSERT INTO TIPO_PRESENCA VALUES ('555', 'Prova com resultado considerado válido');
INSERT INTO TIPO_PRESENCA VALUES ('556', 'Prova com resultado desconsiderado pela Aplicadora');

-- CRIAÇÃO TIPO DE TABELA TIPO DE PRESENÇA ENADE
CREATE TABLE DB.DBO.TIPO_PRESENCA_ENADE(
CODIGO varchar(3),
DESCRICAO varchar(100)
/*222  Ausente
333  Inscrição indevida
334  Eliminado por participação indevida
444  Ausente devido a dupla graduação
555  Presente com resultado válido
556  Presente com resultado desconsiderado pela Aplicadora*/
);
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('222', 'Ausente');
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('333', 'Inscrição indevida');
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('334', 'Eliminado por participação indevida');
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('444', 'Ausente devido a dupla graduação');
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('555', 'Presente com resultado válido');
INSERT INTO TIPO_PRESENCA_ENADE VALUES ('556', 'Presente com resultado desconsiderado pela Aplicadora');

-- CRIAÇÃO DA TABELA DE PRESENÇA
CREATE TABLE DB.DBO.PRESENCA(
ID_ALUNO int NOT NULL PRIMARY KEY,
TP_PRES	varchar(3),
TP_PR_GER	varchar(3),
TP_PR_OB_FG	varchar(3),
TP_PR_DI_FG	varchar(3),
TP_PR_OB_CE	varchar(3),
TP_PR_DI_CE	varchar(3)
);


/*SELECT p.id_aluno, 
tp.descricao, 
tp1.descricao, 
tp2.descricao,
tp2.descricao,
tp2.descricao,
tp2.descricao 
FROM presenca p 
INNER JOIN tipo_presenca tp on p.tp_pres  tp.codigo
INNER JOIN tipo_presenca tp1 on p.tp_pr_ger  tp1.codigo
INNER JOIN tipo_presenca tp2 on p.tp_pr_ob_fg  tp2.codigo
INNER JOIN tipo_presenca tp3 on p.tp_pr_di_fg  tp3.codigo
INNER JOIN tipo_presenca tp4 on p.tp_pr_ob_ce  tp4.codigo
INNER JOIN tipo_presenca tp5 on p.tp_pr_di_ce  tp5.codigo*/

-- CRIAÇÃO TABELA DA CATEGORIA ADMINISTRATIVA DA IES
CREATE TABLE DB.DBO.CATEGAD(
CO_CATEGAD INT PRIMARY KEY NOT NULL,
DESCRICAO VARCHAR(100),
ENTIDADE VARCHAR(50),
ORGANIZACAO VARCHAR(50),
ADM_EST VARCHAR(50)
);
INSERT INTO DB.DBO.CATEGAD VALUES (118,   'Pessoa Jurídica de Direito Privado', 			'Com fins lucrativos', 'Sociedade Civil', 				   NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (120,   'Pessoa Jurídica de Direito Privado', 			'Sem fins lucrativos', 'Associação de Utilidade Pública',  NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (121,   'Pessoa Jurídica de Direito Privado', 			'Sem fins lucrativos', 'Fundação', 						   NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (10005, 'Privada', 				  		   				'Com fins lucrativos', NULL, 							   NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (10006, 'Pessoa Jurídica de Direito Privado', 			'Com fins lucrativos', 'Sociedade Mercantil ou Comercial', NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (10007, 'Pessoa Jurídica de Direito Privado', 			'Sem fins lucrativos', 'Associação de Utilidade Pública',  NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (10008, 'Privada', 				  		   				'Sem fins lucrativos', NULL,							   NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (10009, 'Pessoa Jurídica de Direito Privado', 			'Sem fins lucrativos',  'Sociedade', 					       NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (17634, 'Fundação Pública de Direito Privado Municipal', NULL, 				   NULL, 							   NULL);
INSERT INTO DB.DBO.CATEGAD VALUES (93,    'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Federal');
INSERT INTO DB.DBO.CATEGAD VALUES (115,   'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Estadual');
INSERT INTO DB.DBO.CATEGAD VALUES (116,   'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Municipal');
INSERT INTO DB.DBO.CATEGAD VALUES (10001, 'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Estadual');
INSERT INTO DB.DBO.CATEGAD VALUES (10002, 'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Federal');
INSERT INTO DB.DBO.CATEGAD VALUES (10003, 'Pessoa Jurídica de Direito Público', 			NULL, 				   NULL, 							   'Municipal');

-- CRIAÇÃO DO CODIGO DA ORGANIZAÇÃO ACADEMICA
CREATE TABLE DB.DBO.ORGACAD(
CO_ORGACAD INT PRIMARY KEY NOT NULL,
DESCRICAO VARCHAR(100)
);
INSERT INTO DB.DBO.ORGACAD VALUES (10019, 'Centro Federal de Educação Tecnológica');
INSERT INTO DB.DBO.ORGACAD VALUES (10020, 'Centro Universitário');
INSERT INTO DB.DBO.ORGACAD VALUES (10022, 'Faculdade');
INSERT INTO DB.DBO.ORGACAD VALUES (10026, 'Instituto Federal de Educação, Ciência e Tecnologia');
INSERT INTO DB.DBO.ORGACAD VALUES (10028, 'Universidade');


-- CRIAÇÃO DA TABELA DO CODIGO DO GRUPO
CREATE TABLE DB.DBO.GRUPO(
CO_GRUPO INT NOT NULL,
DESCRICAO VARCHAR (100),
ANO int 
);

INSERT INTO DB.DBO.GRUPO VALUES (5, 'MEDICINA VETERINÁRIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6, 'ODONTOLOGIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (12, 'MEDICINA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (17, 'AGRONOMIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (19, 'FARMÁCIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (21, 'ARQUITETURA E URBANISMO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (23, 'ENFERMAGEM', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (27, 'FONOAUDIOLOGIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (28, 'NUTRIÇÃO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (36, 'FISIOTERAPIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (51, 'ZOOTECNIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (55, 'BIOMEDICINA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (69, 'TECNOLOGIA EM RADIOLOGIA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (90, 'TECNOLOGIA EM AGRONEGÓCIOS', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (91, 'TECNOLOGIA EM GESTÃO HOSPITALAR', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (92, 'TECNOLOGIA EM GESTÃO AMBIENTAL', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (95, 'TECNOLOGIA EM ESTÉTICA E COSMÉTICA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (3501, 'EDUCAÇÃO FÍSICA (BACHARELADO)', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (4003, 'ENGENHARIA DA COMPUTAÇÃO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (5710, 'ENGENHARIA CIVIL', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (5806, 'ENGENHARIA ELÉTRICA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (5814, 'ENGENHARIA DE CONTROLE E AUTOMAÇÃO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (5902, 'ENGENHARIA MECÂNICA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6002, 'ENGENHARIA DE ALIMENTOS', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6008, 'ENGENHARIA QUÍMICA', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6208, 'ENGENHARIA DE PRODUÇÃO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6307, 'ENGENHARIA AMBIENTAL', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6405, 'ENGENHARIA FLORESTAL', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (6410, 'TECNOLOGIA EM SEGURANÇA NO TRABALHO', 2019);
INSERT INTO DB.DBO.GRUPO VALUES (1, 'ADMINISTRAÇÃO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (2, 'DIREITO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (13, 'CIÊNCIAS ECONÔMICAS', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (18, 'PSICOLOGIA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (22, 'CIÊNCIAS CONTÁBEIS', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (26, 'DESIGN', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (29, 'TURISMO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (38, 'SERVIÇO SOCIAL', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (67, 'SECRETARIADO EXECUTIVO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (81, 'RELAÇÕES INTERNACIONAIS', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (83, 'TECNOLOGIA EM DESIGN DE MODA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (84, 'TECNOLOGIA EM MARKETING', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (85, 'TECNOLOGIA EM PROCESSOS GERENCIAIS', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (86, 'TECNOLOGIA EM GESTÃO DE RECURSOS HUMANOS', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (87, 'TECNOLOGIA EM GESTÃO FINANCEIRA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (88, 'TECNOLOGIA EM GASTRONOMIA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (93, 'TECNOLOGIA EM GESTÃO COMERCIAL', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (94, 'TECNOLOGIA EM LOGÍSTICA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (100, 'ADMINISTRAÇÃO PÚBLICA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (101, 'TEOLOGIA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (102, 'TECNOLOGIA EM COMÉRCIO EXTERIOR', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (103, 'TECNOLOGIA EM DESIGN DE INTERIORES', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (104, 'TECNOLOGIA EM DESIGN GRÁFICO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (105, 'TECNOLOGIA EM GESTÃO DA QUALIDADE', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (106, 'TECNOLOGIA EM GESTÃO PÚBLICA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (803, 'COMUNICAÇÃO SOCIAL - JORNALISMO', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (804, 'COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA', 2018);
INSERT INTO DB.DBO.GRUPO VALUES (21, 'Arquitetura e Urbanismo', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (72, 'Tecnologia em Análise e Desenvolvimento de Sistemas', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (76, 'Tecnologia em Gestão da Produção Industrial', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (79, 'Tecnologia em Redes de Computadores', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (701, 'Matemática (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (702, 'Matemática (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (903, 'Letras-Português (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (904, 'Letras-Português (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (905, 'Letras-Português e Inglês (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (906, 'Letras-Português e Espanhol (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1401, 'Física (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1402, 'Física (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1501, 'Química (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1502, 'Química (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1601, 'Ciências Biológicas (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (1602, 'Ciências Biológicas (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (2001, 'Pedagogia (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (2401, 'História (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (2402, 'História (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (2501, 'Artes Visuais (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (3001, 'Geografia (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (3002, 'Geografia (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (3201, 'Filosofia (Bacharelado)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (3202, 'Filosofia (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (3502, 'Educação Física (Licenciatura)', 2017);
INSERT INTO DB.DBO.GRUPO VALUES (5, 'MEDICINA VETERINÁRIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (6, 'ODONTOLOGIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (12, 'MEDICINA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (17, 'AGRONOMIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (19, 'FARMÁCIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (23, 'ENFERMAGEM', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (27, 'FONOAUDIOLOGIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (28, 'NUTRIÇÃO', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (36, 'FISIOTERAPIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (38, 'SERVIÇO SOCIAL', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (51, 'ZOOTECNIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (55, 'BIOMEDICINA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (69, 'TECNOLOGIA EM RADIOLOGIA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (90, 'TECNOLOGIA EM AGRONEGÓCIOS', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (91, 'TECNOLOGIA EM GESTÃO HOSPITALAR', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (92, 'TECNOLOGIA EM GESTÃO AMBIENTAL', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (95, 'TECNOLOGIA EM ESTÉTICA E COSMÉTICA', 2016);
INSERT INTO DB.DBO.GRUPO VALUES (3501, 'EDUCAÇÃO FÍSICA (BACHARELADO)', 2016)

-- CRIACAO DA TABELA CURSO
CREATE TABLE DB.DBO.CURSO(
CO_CURSO INT NOT NULL,
CO_GRUPO INT NOT NULL,
CO_IES INT NOT NULL,
CO_MUNIC	int NOT NULL,
CO_MODALIDADE  INT NOT NULL,
CONSTRAINT PK_CO_CURSO PRIMARY KEY (CO_CURSO),
CONSTRAINT FK_CO_IES FOREIGN KEY (CO_IES) REFERENCES dbo.IES (CO_IES),
CONSTRAINT FK_CO_MUNIC FOREIGN KEY (CO_MUNIC) REFERENCES dbo.MUNIC (CO_MUNIC),
CONSTRAINT CK_MODALIDADE CHECK (CO_MODALIDADE IN (0 , 1)) -- 0 = EaD , 1 = Presencial
);

-- CRIACAO DA TABELA ALUNO 
CREATE TABLE DB.DBO.ALUNO(
ID_ALUNO 	int NOT NULL,
NU_IDADE	int,
TP_SEXO	varchar(2),
ANO_FIM_EM	int,
ANO_IN_GRAD	int,
CO_TURNO_GRADUACAO	int,
TP_INSCRICAO_ADM	int,
TP_INSCRICAO	int,
CO_CURSO int,
CONSTRAINT PK_ALUNO PRIMARY KEY (ID_ALUNO),
CONSTRAINT CK_TP_SEXO CHECK (TP_SEXO IN ('M', 'F')),
CONSTRAINT CK_TP_INSCRICAO_ADM CHECK (TP_INSCRICAO_ADM = 1),
CONSTRAINT CK_TP_INSCRICAO CHECK (TP_INSCRICAO = 0),
CONSTRAINT CK_TURNO_GRADUACAO CHECK (CO_TURNO_GRADUACAO IN (1,2,3,4)),
CONSTRAINT FK_CO_CURSO FOREIGN KEY (CO_CURSO) REFERENCES dbo.CURSO (CO_CURSO)
/*
1 = Matutino
2 = Vespertino
3 = Integral
4 = Noturno
*/
);

-- TABELA FORMACAO GERAL DO COMPONENTE EXPECIFICO

CREATE TABLE DB.DBO.ALUNO(
ID_ALUNO    int NOT NULL,
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
UF_CONCLUSAO_EM INT,
CONSTRAINT PK_ALUNO PRIMARY KEY (ID_ALUNO),
CONSTRAINT CK_TP_SEXO CHECK (TP_SEXO IN ('M', 'F')),
CONSTRAINT CK_TP_INSCRICAO_ADM CHECK (TP_INSCRICAO_ADM = 1),
CONSTRAINT CK_TP_INSCRICAO CHECK (TP_INSCRICAO = 0),
CONSTRAINT CK_TURNO_GRADUACAO CHECK (CO_TURNO_GRADUACAO IN (1,2,3,4)),
CONSTRAINT FK_CO FOREIGN KEY (CO_CURSO) REFERENCES dbo.CURSO (CO_CURSO),
CONSTRAINT FK_CO_ALUNO_EM FOREIGN KEY (CO_UF) REFERENCES dbo.CURSO (CO_UF)


TSCODS.ODS_INDCLIEND_GRL
TSCODS.ODS_INDCLIEND_CTT
TSCODS.ODS_INDCLIEND_FRQ




J_CLIEND_DADGRL OK obs: job filho do J_CLIEND_IND
J_DIMCNTCTB OK


J_DIMTETVND erro de conexão


19103
013
00050969-0