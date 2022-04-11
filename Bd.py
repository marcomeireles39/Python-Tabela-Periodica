# Arquivo : Bd.py
# Criador : Marco Aurélio
# Data 06/04/2022
import sqlite3

from matplotlib.pyplot import table

# Classe Bd_sql
# Classe responsável por realizar operações com banco de dados sqlite

class Bd_sql:    
    Nome = ""
    Tabela = ""
    
    def __init__(self, nome, tabela):
        self.Nome = nome
        self.Tabela = tabela
        
    def Criar_bd(self, indice):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            codig = "CREATE TABLE {} ({})".format(self.Tabela, indice)
            cursor.execute(codig)
            bd.commit()
            bd.close()

        except sqlite3.Error as error:
                print('Erro :', error)
                return 0
    
    def Incluir_dados(self, dados):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            codi = "INSERT INTO {} VALUES({})".format(self.Tabela, dados)
            cursor.execute(codi)
            bd.commit()
            bd.close()
    
        except sqlite3.Error as error:
            print('Erro :', error)
            return 0
    
    
    def Apaga(self, condicao):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            codigo = "DELETE from {} WHERE {}".format(self.Tabela, condicao)
            cursor.execute(codigo)
            bd.commit()
    
        except sqlite3.Error as error:
            print('Erro :', error)
            return 0

    def Modificar(self, ca_valor, condicao):
        try:
            codigo = "UPDATE {} SET {} WHERE {}".format(self.Tabela, ca_valor, condicao)
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            cursor.execute(codigo)
            bd.commit()
        except sqlite3.Error as error:
            print('Erro :', error)
            return 0
        
            
    def Mostrar(self):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            cod = "SELECT * FROM {}".format(self.Tabela)
            cursor.execute(cod)
            for cur in cursor:
                print(cur)
            bd.close()
            
        except sqlite3.Error as error:
                print('Erro :', error)
                return 0
    
    def Sql_Command(self,codigo):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            cursor.execute(codigo)
            bd.commit()
        except sqlite3.Error as error:
            print('Erro :', error)
            return 0
        
    def Apaga_Tabela(self, tabela):
        try:
            bd = sqlite3.connect('{}'.format(self.Nome))
            cursor = bd.cursor()
            codigo = "DROP TABLE {};".format(tabela)
            cursor.execute(codigo)
            bd.commit()
    
        except sqlite3.Error as error:
            print('Erro :', error)
            return 0


