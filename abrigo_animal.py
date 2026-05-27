from conexao import conectar
import os

def limpar_tela():
    os.system('cls')

def pausar():
    input("\nPressione ENTER para continuar...")

# ---------------- ANIMAIS ----------------
def cadastrar_animal(nome, raca, especie, sexo, porte):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_animal
    (nome_animal, especie_animal, raca_animal, sexo_animal, porte_animal, status_animal)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (nome, especie, raca, sexo, porte, 0)

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()

    print("Animal cadastrado com sucesso!")

def buscar_animal(id_animal):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM tbl_animal WHERE id_animal = %s"

    cursor.execute(sql, (id_animal,))

    animal = cursor.fetchone()

    cursor.close()
    conexao.close()

    return animal

def listar_animais():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM tbl_animal"

    cursor.execute(sql)

    dados = cursor.fetchall()

    if not dados:
        print("Nenhum animal cadastrado.")

    for animal in dados:
        print(f"""
ID: {animal[0]}
Nome: {animal[1]}
Espécie: {animal[2]}
Raça: {animal[3]}
Data Nascimento: {animal[4]}
Sexo: {animal[5]}
Porte: {animal[6]}
Status: {"Adotado" if animal[7] == 1 else "Disponível"}
=================================
""")

    cursor.close()
    conexao.close()

# ---------------- ADOTANTE ----------------
def cadastrar_adotante(nome, cpf, telefone, email, cep, logradouro, complemento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO tbl_adotante
    (nome_adotante, cpf_adotante, telefone_adotante, email_adotante,
    cep_adotante, logradouro_adotante, complemento_adotante)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (nome, cpf, telefone, email, cep, logradouro, complemento)

    cursor.execute(sql, valores)

    conexao.commit()

    cursor.close()
    conexao.close()

    print("Adotante cadastrado com sucesso!")

def listar_adotantes():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM tbl_adotante"

    cursor.execute(sql)

    dados = cursor.fetchall()

    if not dados:
        print("Nenhum adotante cadastrado.")

    for adotante in dados:
        print(f"""
ID: {adotante[0]}
Nome: {adotante[1]}
Telefone: {adotante[2]}
CPF: {adotante[3]}
Email: {adotante[4]}
CEP: {adotante[5]}
Logradouro: {adotante[6]}
Complemento: {adotante[7]}
=================================
""")

    cursor.close()
    conexao.close()

# ---------------- ADOÇÃO ----------------
def solicitar_adocao(id_adotante, id_animal):
    conexao = conectar()
    cursor = conexao.cursor()

    sql_animal = "SELECT * FROM tbl_animal WHERE id_animal = %s"

    cursor.execute(sql_animal, (id_animal,))

    animal = cursor.fetchone()

    if not animal:
        print("Erro: Animal não existe.")
        cursor.close()
        conexao.close()
        return

    if animal[7] == 1:
        print("Erro: Este animal já foi adotado.")
        cursor.close()
        conexao.close()
        return

    sql_update = """
    UPDATE tbl_animal
    SET status_animal = 1,
        id_adotante = %s
    WHERE id_animal = %s
    """

    cursor.execute(sql_update, (id_adotante, id_animal))

    conexao.commit()

    print("Adoção solicitada com sucesso!")

    cursor.close()
    conexao.close()

def listar_adocoes():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        tbl_adotante.nome_adotante,
        tbl_animal.nome_animal
    FROM tbl_animal
    INNER JOIN tbl_adotante
    ON tbl_animal.id_adotante = tbl_adotante.id_adotante
    WHERE tbl_animal.status_animal = 1
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    if not dados:
        print("Nenhuma adoção registrada.")

    for adocao in dados:
        print(f"""
Adotante: {adocao[0]}
Animal: {adocao[1]}
=================================
""")

    cursor.close()
    conexao.close()

# ---------------- MENU PRINCIPAL ----------------
opcao = None

while opcao != "0":
    limpar_tela()

    print("========================================")
    print("        SISTEMA DE ADOÇÃO DE ANIMAIS")
    print("========================================")
    print("1 - Listar Animais")
    print("2 - Cadastrar Animal")
    print("3 - Cadastrar Adotante")
    print("4 - Solicitar Adoção")
    print("5 - Listar Adoções")
    print("6 - Listar Adotantes")
    print("0 - Sair")
    print("========================================")

    opcao = input("Opção desejada: ")

    limpar_tela()

    if opcao == "1":
        print("LISTA DE ANIMAIS =======================\n")
        listar_animais()
        pausar()

    elif opcao == "2":
        print("CADASTRAR ANIMAL =======================\n")

        nome = input("Nome: ")
        raca = input("Raça: ")

        print("\nEspécie:")
        print("1 - Cachorro")
        print("2 - Gato")

        opcao_especie = input("Escolha: ")

        if opcao_especie == "1":
            especie = "Cachorro"
        elif opcao_especie == "2":
            especie = "Gato"
        else:
            print("Opção inválida.")
            pausar()
            continue

        print("\nSexo:")
        print("1 - Macho")
        print("2 - Fêmea")

        opcao_sexo = input("Escolha: ")

        if opcao_sexo == "1":
            sexo = "Macho"
        elif opcao_sexo == "2":
            sexo = "Fêmea"
        else:
            print("Opção inválida.")
            pausar()
            continue

        print("\nPorte:")
        print("1 - Pequeno")
        print("2 - Médio")
        print("3 - Grande")

        opcao_porte = input("Escolha: ")

        if opcao_porte == "1":
            porte = "Pequeno"
        elif opcao_porte == "2":
            porte = "Médio"
        elif opcao_porte == "3":
            porte = "Grande"
        else:
            print("Opção inválida.")
            pausar()
            continue

        cadastrar_animal(nome, raca, especie, sexo, porte)

        pausar()

    elif opcao == "3":
        print("CADASTRAR ADOTANTE =====================\n")

        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        cep = input("CEP: ")
        logradouro = input("Logradouro: ")
        complemento = input("Complemento: ")

        cadastrar_adotante(
            nome,
            cpf,
            telefone,
            email,
            cep,
            logradouro,
            complemento
        )

        pausar()

    elif opcao == "4":
        print("SOLICITAR ADOÇÃO =======================\n")

        try:
            id_adotante = int(input("ID do adotante: "))
            id_animal = int(input("ID do animal: "))

            print()

            solicitar_adocao(id_adotante, id_animal)

        except ValueError:
            print("\nErro: Os IDs devem ser números inteiros.")

        pausar()

    elif opcao == "5":
        print("LISTA DE ADOÇÕES =======================\n")
        listar_adocoes()
        pausar()

    elif opcao == "6":
        print("LISTA DE ADOTANTES =====================\n")
        listar_adotantes()
        pausar()

    elif opcao == "0":
        print("Saindo do sistema...")

    else:
        print("Opção inválida!")
        pausar()