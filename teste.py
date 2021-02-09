import pandas as pd
import numpy as np
import pyodbc


data = np.array(
    [[118,   'Pessoa Jurídica de Direito Privado','Com fins lucrativos', 'Sociedade Civil',' '],
    [120,   'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Associação de Utilidade Pública',' '],
    [121,   'Pessoa Jurídica de Direito Privado','Sem fins lucrativos','Fundação',' '],
    [10005, 'Privada','Com fins lucrativos', ' ', ' '],
    [10006, 'Pessoa Jurídica de Direito Privado','Com fins lucrativos','Sociedade Mercantil ou Comercial',' '],
    [10007, 'Pessoa Jurídica de Direito Privado', 'Sem fins lucrativos','Associação de Utilidade Pública', ' '],
    [10008, 'Privada','Sem fins lucrativos', ' ',' '],
    [10009, 'Pessoa Jurídica de Direito Privado', 'Sem fins lucrativos','Sociedade',' '],
    [17634, 'Fundação Pública de Direito Privado Municipal', ' ',' ',' '],
    [93,    'Pessoa Jurídica de Direito Público',' ',' ','Federal'],
    [115,   'Pessoa Jurídica de Direito Público',' ',' ','Estadual'],
    [116,   'Pessoa Jurídica de Direito Público',' ',' ','Municipal'],
    [10001, 'Pessoa Jurídica de Direito Público',' ',' ','Estadual'],
    [10002, 'Pessoa Jurídica de Direito Público',' ',' ','Federal'],
    [10003, 'Pessoa Jurídica de Direito Público',' ',' ','Municipal']]
    )
df = pd.DataFrame(data)
print(df)



def imprimir_lista(lista):
    for elemento in lista:
        if isinstance(elemento, list): # se este elemento é uma lista, chama a mesma funçao
            imprimir_lista(elemento)
        else: # caso contrário imprime normalmente
            print(elemento)
imprimir_lista(lista)