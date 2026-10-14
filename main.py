import os
from dotenv import load_dotenv

from database import conectar
load_dotenv()


def adicionar_registro(nome, idade, email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)",
        (nome, idade, email)
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Registro adicionado com sucesso!")

def listar_registros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pessoas")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    return registros


def deletar_registro(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pessoas WHERE id = %s", (id,))

    conexao.commit()
    cursor.close()
    conexao.close()


def modificar_registro(id, nome, idade, email):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE pessoas SET nome = %s, idade = %s, email = %s WHERE id = %s",
        (nome, idade, email, id)
    )

    conexao.commit()
    cursor.close()
    conexao.close()




def pedir_idade():
    while True:
        try:
            return int(input("Digite a idade: "))
        except ValueError:
            print("Idade inválida. Digite apenas números.")


def menu():
    print("Bem-vindo ao sistema de gerenciamento de pessoas!")

    while True:
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Modificar")
        print("4 - Deletar")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = pedir_idade()
            email = input("Digite o email: ")
            adicionar_registro(nome, idade, email)
        elif opcao == "2":
            for registro in listar_registros():
                print(registro)
        elif opcao == "3":
            id_pessoa = int(input("ID da pessoa: "))
            nome = input("Novo nome: ")
            idade = pedir_idade()
            email = input("Novo email: ")
            modificar_registro(id_pessoa, nome, idade, email)
        elif opcao == "4":
            id_pessoa = int(input("ID da pessoa: "))
            deletar_registro(id_pessoa)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        

if __name__ == "__main__":
    menu()
