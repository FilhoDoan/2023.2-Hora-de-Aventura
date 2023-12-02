import psycopg2
from .Database import Database

class Inventario:
    def __init__(self):
        self.db=Database()

    def inserirInventario(self, IDinv:int, QTD_de_itens:int, Personagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""INSERT INTO Inventario VALUES({IDinv}, '{QTD_de_itens}', {Personagem});""")
            conexao.commit()
            return print("Inventario Inserido")
        except psycopg2.Error as e:
            print("Erro ao inserir Inventario", e)
        finally:
            cursor.close()
    
    def consultarInventario(self):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Inventario;""")
            conexao.commit()
            resultado=cursor.fetchall()
            for i in resultado:
                print(i)
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()

    def deletarInventario(self, IDinv:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""DELETE FROM Inventario WHERE IDinv = {IDinv};""")
            conexao.commit()
            return print("Inventario Deletada")
        except psycopg2.Error as e:
            print("Erro ao deletar Inventario", e)
        finally:
            cursor.close()

    def consultarInventarioEspecifico(self, IDinv:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT * FROM Inventario WHERE IDinv = {IDinv};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()
            
    def verItensInventario(self, IDpersonagem:int):
        try:
            conexao=self.db.conexao
            cursor=conexao.cursor()
            cursor.execute(f"""SELECT I.IDitem  FROM Item I """
                       f"""JOIN InstanciaItem Ia ON I.IDitem = Ia.IDitem """
                       f"""JOIN Inventario Inv ON Ia.IDinv = Inv.IDinv """
                       f"""JOIN Personagem P ON Inv.Personagem = P.IDpersonagem """  # Adicionando um espaço aqui
                       f"""WHERE P.IDpersonagem = {IDpersonagem};""")
            conexao.commit()
            resultado=cursor.fetchall()
            if resultado:
                print(resultado[0])
        except psycopg2.Error as e:
            print("Erro ao consultar Inventario", e)
        finally:
            cursor.close()
    