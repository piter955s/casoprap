import mysql.connector

class Voluntario:
    def __init__(self, nome_completo, endereco, cpf, rg, foto):
        self.nome_completo = nome_completo
        self.endereco = endereco
        self.cpf = cpf
        self.rg = rg
        self.foto = foto

    def cadastrar_voluntario(self, mydb):
        cursor = mydb.cursor()
        query = "INSERT INTO Voluntarios (NomeCompleto, Endereco, CPF, RG, Foto) VALUES (%s, %s, %s, %s, %s)"
        values = (self.nome_completo, self.endereco, self.cpf, self.rg, self.foto)

        try:
            cursor.execute(query, values)
            mydb.commit()
            print("Voluntário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar voluntário: {err}")
        finally:
            cursor.close()

