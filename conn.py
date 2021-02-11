import pyodbc

class ConexaoDB():

    def __init__(self, host=input("Host: "), user=input("User: "),
                 pwd=input("Senha: "), db=input("Banco: ")):
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

    def executa_DML_PR(self, sql, pr):
        self.conecta()
        self.cursor.execute(sql, pr)
        self.con.commit()

    def executa_DML(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        self.con.commit()

