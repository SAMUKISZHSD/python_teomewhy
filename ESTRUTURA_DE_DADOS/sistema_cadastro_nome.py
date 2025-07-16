nomes = []

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome para adicionar: ")
        nomes.append(nome)
        print(f"'{nome}' foi adicionado à lista.")

    elif opcao == "2":
        if not nomes:
            print("A lista está vazia.")
        else:
            print("Nomes cadastrados:")
            for nome in nomes:
                print("-", nome)

    elif opcao == "3":
        nome = input("Digite o nome que deseja remover: ")
        if nome in nomes:
            nomes.remove(nome)
            print(f"'{nome}' foi removido da lista.")
        else:
            print(f"'{nome}' não foi encontrado na lista.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
