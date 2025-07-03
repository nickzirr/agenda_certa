import sqlite3

def criar_conexao():
    return sqlite3.connect("agenda.db")

def criar_tabela():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_contato(nome, telefone, cpf, endereco):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO contatos (nome, telefone, cpf, endereco) VALUES (?, ?, ?, ?)",
        (nome, telefone, cpf, endereco)
    )
    conexao.commit()
    conexao.close()

def listar_contatos():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    if contatos:
        for contato in contatos:
            print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, CPF: {contato[3]}, Endereço: {contato[4]}")
    else:
        print("Nenhum contato encontrado.")
    conexao.close()

def buscar_contato_por_nome(nome):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"Nome: {resultado[1]}, Telefone: {resultado[2]}, CPF: {resultado[3]}, Endereço: {resultado[4]}")
    else:
        print("Contato não encontrado.")
    conexao.close()

def remover_contato_por_id(contato_id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (contato_id,))
    conexao.commit()
    conexao.close()
    print("Contato removido com sucesso.")

def menu():
    criar_tabela()
    while True:
        print("\n  Menu da Agenda")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato por nome")
        print("4 - Remover contato por ID")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            adicionar_contato(nome, telefone, cpf, endereco)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            nome = input("Nome para busca: ")
            buscar_contato_por_nome(nome)
        elif opcao == "4":
            try:
                contato_id = int(input("ID do contato a remover: "))
                remover_contato_por_id(contato_id)
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
