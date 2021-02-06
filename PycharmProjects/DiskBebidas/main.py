import psycopg2


con = psycopg2.connect(host='192.168.1.7', database='db',user='postgres', password='123456')

cur = con.cursor()
codigo = input('Codigo: ')
codigo_barras = input('Codigo de barras :')
denominacao = input('denominação: ')
denominacao_reduzida = input('Denominacao Reduzida: ')
categoria_item = int(input('Categoria item: '))
unidade_medida = int(input('Unidade de medida: '))

cur.execute("""
     INSERT INTO db.item (codigo, codigo_barras, denominacao, denominacao_reduzida, id_categoria_item, id_unidade_medida)
     VALUES (%s, %s, %s, %s, %s, %s);
     """,
     (codigo, codigo_barras, denominacao, denominacao_reduzida,categoria_item, unidade_medida)
            )



