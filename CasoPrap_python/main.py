import tkinter as tk
from tkinter import messagebox
from voluntario import Voluntario
from mantimento import Mantimento
from animal import Animal

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123pedro",
    database="animais4"
)

def cadastrar_voluntario():
    def submit_voluntario():
        nome_completo = nome_completo_entry.get()

        voluntario = Voluntario(nome_completo, "", "", "", "")
        voluntario.cadastrar_voluntario(mydb)
        messagebox.showinfo("Cadastro de Voluntário", "Voluntário cadastrado com sucesso!")

    voluntario_window = tk.Toplevel(root)
    voluntario_window.title("Cadastro de Voluntário")

    tk.Label(voluntario_window, text="Nome completo:").grid(row=0, column=0)

    nome_completo_entry = tk.Entry(voluntario_window)

    nome_completo_entry.grid(row=0, column=1)

    submit_button = tk.Button(voluntario_window, text="Cadastrar", command=submit_voluntario)
    submit_button.grid(row=1, columnspan=2)

def cadastrar_mantimento():
    def submit_mantimento():
        descricao = descricao_entry.get()
        quantidade = quantidade_entry.get()
        voluntario_id = voluntario_id_entry.get()

        mantimento = Mantimento(tipo_mantimento, descricao, quantidade, voluntario_id)
        mantimento.cadastrar_mantimento(mydb)
        messagebox.showinfo("Cadastro de Mantimento", "Mantimento cadastrado com sucesso!")

    mantimento_window = tk.Toplevel(root)
    mantimento_window.title("Cadastro de Mantimento")

    tk.Label(mantimento_window, text="Descrição:").grid(row=1, column=0)
    tk.Label(mantimento_window, text="Quantidade:").grid(row=2, column=0)
    tk.Label(mantimento_window, text="ID do voluntário associado:").grid(row=3, column=0)

    descricao_entry = tk.Entry(mantimento_window)
    quantidade_entry = tk.Entry(mantimento_window)
    voluntario_id_entry = tk.Entry(mantimento_window)

    descricao_entry.grid(row=1, column=1)
    quantidade_entry.grid(row=2, column=1)
    voluntario_id_entry.grid(row=3, column=1)

    submit_button = tk.Button(mantimento_window, text="Cadastrar", command=submit_mantimento)
    submit_button.grid(row=4, columnspan=2)

def cadastrar_animal():
    def submit_animal():
        tipo_animal = tipo_animal_entry.get()
        nome = nome_entry.get()
        idade = idade_entry.get()
        raca = raca_entry.get()
        castrado = castrado_entry.get()
        local_resgate = local_resgate_entry.get()
        voluntario_id = voluntario_id_entry.get()

        animal = Animal(tipo_animal, nome, idade, raca, "", castrado, local_resgate, "", voluntario_id)
        animal.cadastrar_animal(mydb)
        messagebox.showinfo("Cadastro de Animal", "Animal cadastrado com sucesso!")

    animal_window = tk.Toplevel(root)
    animal_window.title("Cadastro de Animal")

    tk.Label(animal_window, text="Tipo de animal (Cachorro ou Gato):").grid(row=0, column=0)
    tk.Label(animal_window, text="Nome:").grid(row=1, column=0)
    tk.Label(animal_window, text="Idade:").grid(row=2, column=0)
    tk.Label(animal_window, text="Raça:").grid(row=3, column=0)
    tk.Label(animal_window, text="Castrado (True ou False):").grid(row=4, column=0)
    tk.Label(animal_window, text="Local de resgate:").grid(row=5, column=0)
    tk.Label(animal_window, text="ID do voluntário responsável:").grid(row=6, column=0)

    tipo_animal_entry = tk.Entry(animal_window)
    nome_entry = tk.Entry(animal_window)
    idade_entry = tk.Entry(animal_window)
    raca_entry = tk.Entry(animal_window)
    castrado_entry = tk.Entry(animal_window)
    local_resgate_entry = tk.Entry(animal_window)
    voluntario_id_entry = tk.Entry(animal_window)

    tipo_animal_entry.grid(row=0, column=1)
    nome_entry.grid(row=1, column=1)
    idade_entry.grid(row=2, column=1)
    raca_entry.grid(row=3, column=1)
    castrado_entry.grid(row=4, column=1)
    local_resgate_entry.grid(row=5, column=1)
    voluntario_id_entry.grid(row=6, column=1)

    submit_button = tk.Button(animal_window, text="Cadastrar", command=submit_animal)
    submit_button.grid(row=7, columnspan=2)

root = tk.Tk()
root.title("Sistema de Cadastro de Animais")

menu_frame = tk.Frame(root)
menu_frame.pack(pady=20)

tk.Button(menu_frame, text="Cadastrar Voluntário", command=cadastrar_voluntario).grid(row=0, column=0)
tk.Button(menu_frame, text="Cadastrar Mantimento", command=cadastrar_mantimento).grid(row=0, column=1)
tk.Button(menu_frame, text="Cadastrar Animal", command=cadastrar_animal).grid(row=0, column=2)
tk.Button(menu_frame, text="Sair", command=root.quit).grid(row=0, column=3)

root.mainloop()
mydb.close()
