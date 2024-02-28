import mysql.connector

class Mantimento:
    def __init__(self, descricao, preco, voluntario_id):
        self.descricao = descricao
        self.quantidade = preco
        self.voluntario_id = voluntario_id

    def cadastrar_mantimento(self, mydb):
        cursor = mydb.cursor()
        query = "INSERT INTO Mantimentos (Descricao, preco, VoluntarioID) VALUES (%s, %s, %s, %s)"
        values = (self.descricao, self.preco, self.voluntario_id)

        try:
            cursor.execute(query, values)
            mydb.commit()
            print("Mantimento cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar mantimento: {err}")
        finally:
            cursor.close()
