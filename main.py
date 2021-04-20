# -*- encoding: utf-8 -*-
from localizacao import regiao, uf, munic
from normalizacao import categ_adm_ies, org_ac_ies, ies, grupo_curso, curso
from aluno import tabela_aluno
from web_scraping_link_enade import carrega_dados_bruto, extrai_link_zip, verifica_arquivo_diretorio
resposta = input("executar processo de normalização: (sim/nao)")
if resposta == "sim":
    carrega_dados_bruto()
    extrai_link_zip()
    verifica_arquivo_diretorio()
    regiao()
    uf()
    munic()
    categ_adm_ies()
    org_ac_ies()
    ies()
    grupo_curso()
    curso()
    tabela_aluno()
elif resposta == "nao":
    print(";)")







