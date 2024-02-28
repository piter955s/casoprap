import mysql.connector

class Animal:
    def __init__(self, tipo_animal, nome, idade, raca, cor, castrado, local_resgate, foto, voluntario_id):
        self.tipo_animal = tipo_animal
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.castrado = castrado
        self.local_resgate = local_resgate
        self.voluntario_id = voluntario_id

    def cadastrar_animal(self, mydb):
        cursor = mydb.cursor()
        query = "INSERT INTO Animais (TipoAnimal, Nome, Idade, Raca,LocalResgate, VoluntarioResponsavelID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.tipo_animal, self.nome, self.idade, self.raca, self.castrado, self.local_resgate, self.voluntario_id)

        try:
            cursor.execute(query, values)
            mydb.commit()
            print("Animal cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar animal: {err}")
        finally:
            cursor.close()

    def listar_gatos(self, mydb):
        cursor = mydb.cursor()
        query = "SELECT * FROM Animais WHERE TipoAnimal = 'gato'"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            for animal in result:
                print(animal)
        except mysql.connector.Error as err:
            print(f"Erro ao listar gatos: {err}")
        finally:
            cursor.close()

    def listar_cachorros(self, mydb):
        cursor = mydb.cursor()
        query = "SELECT * FROM Animais WHERE TipoAnimal = 'cachorro'"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            for animal in result:
                print(animal)
        except mysql.connector.Error as err:
            print(f"Erro ao listar cachorros: {err}")
        finally:
            cursor.close()

    def foi_adotado(self, mydb):
        cursor = mydb.cursor()
        query = "SELECT * FROM Animais WHERE Nome = %s AND VoluntarioResponsavelID IS NOT NULL"  # Supondo que VoluntarioResponsavelID é preenchido quando o animal é adotado
        values = (self.nome,)
        try:
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                print(f"O animal {self.nome} foi adotado!")
            else:
                print(f"O animal {self.nome} ainda está disponível para adoção.")
        except mysql.connector.Error as err:
            print(f"Erro ao verificar se o animal foi adotado: {err}")
        finally:
            cursor.close()
