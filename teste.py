import pandas as pd
import numpy as np
import pyodbc


import pyodbc
import pandas as pd

class ConexaoDB():
    def __init__(self, host = 'ESTAGIO1-PC\SQLEXPRESS', user = '',
                 pwd = '', db = 'enade'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def conecta(self):
        self.con = pyodbc.connect('DRIVER={SQL Server};SERVER='+ self.host +
                                  ';DATABASE=' + self.db +
                                  ';UID=' + self.user +
                                  ';PWD=' + self.pwd)
        self.cursor = self.con.cursor()

    def desconecta(self):
        self.con.close()

    def executa_DQL(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        print(res)
        self.desconecta()
        return res

    def executa_DML(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        self.cursor.commit()
        res = self.cursor.fechall()
        self.desconecta()
        return res

c = ConexaoDB()
c.conecta()
c.executa_DQL("select * from ies")
