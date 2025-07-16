alunos = {}

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar aluno")
    print("2 - Ver todos os alunos")
    print("3 - Atualizar nota de um aluno")
    print("4 - Remover aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        if nome in alunos:
            print(f"{nome} já está cadastrado.")
        else:
            nota = float(input("Digite a nota do aluno: "))
            alunos[nome] = nota
            print(f"{nome} cadastrado com nota {nota}.")

    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("Alunos cadastrados:")
            for nome, nota in alunos.items():
                print(f"- {nome}: {nota}")

    elif opcao == "3":
        nome = input("Digite o nome do aluno que deseja atualizar: ")
        if nome in alunos:
            nova_nota = float(input("Digite a nova nota: "))
            alunos[nome] = nova_nota
            print(f"Nota de {nome} atualizada para {nova_nota}.")
        else:
            print(f"{nome} não foi encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome do aluno que deseja remover: ")
        if nome in alunos:
            del alunos[nome]
            print(f"{nome} foi removido.")
        else:
            print(f"{nome} não está cadastrado.")

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
