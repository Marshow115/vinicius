escola = {}


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ").strip()

    if any(nome_cadastrado.casefold() == nome.casefold() for nome_cadastrado in escola):
        print(f"\nO aluno '{nome}' já está cadastrado. Não foi adicionado novamente.")
        return

    idade = input("Digite a idade do aluno: ")
    sexo = input("Digite o seu sexo (M/F): ")
    endereço = input("Digite o endereço do aluno: ")

    escola[nome] = {"idade": idade, "sexo": sexo, "endereço": endereço}
    print(f"Aluno {nome} adicionado com sucesso!")


def turma():
    if escola:
        print("\nAlunos cadastrados:")

        for nome, info in escola.items():
            print(f"ALUNO:{nome} - IDADE:{info ['idade']} anos, SEXO:{info['sexo']}, ENDEREÇO:{info['endereço']}")
    else:
        print("Não há alunos cadastrados.")


while True:
    print("\n--- ESCOLA ---")
    print("1. Adicionar um aluno")
    print("2. Ver turma")
    print("5. Fechar turma")

    escolha = input("Escolha uma opção: ")
   
    if escolha == "1":
        adicionar_aluno()

    elif escolha == "2":
        turma()

    elif escolha == "5":
            print("Até a próxima!")
            break
    else:
            print("Opção inválida.")