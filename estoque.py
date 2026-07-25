estoque = []
id_star = 1

while True:
    print('-=-'*20)
    print("\nMENU ESTOQUE: ")
    print("\033[36m1.Cadastrar produto\033[m")
    print("\033[33m2.Excluir produto\033[m")
    print("\033[34m3.Mostrar relatório de produtos\033[m")
    print("\033[35m4.Sair\033[m")
    print('-=-'*20)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n\033[36mCADASTRO DE PRODUTO\033[m")
        nome = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço do produto: "))

        produto = {
            "id": id_star,
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco": preco
        }

        estoque.append(produto)
        id_star += 1 #Prepara o proximo ID
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n\033[33mEXCLUSÃO DE PRODUTO\033[m")
        id_excluir = input("Digite o ID ou Nome do produto a ser excluído: ")
        encontrado = False

        # Cria uma nova lista para guardar os produtos que não serão excluídos,
        # evitando modificar a lista original durante a repetição.
        novo_estoque = []

        for produto in estoque:
            if str(produto["id"]) == str(id_excluir) or produto["nome"].lower() == str(id_excluir).lower():
                print("Produto excluído com sucesso!")
                encontrado = True
            else:
              novo_estoque.append(produto)

        estoque = novo_estoque

        if not encontrado:
            print("Produto não encontrado!")

    elif opcao == "3":
        print("\n\033[34mRELATÓRIO DE PRODUTOS\033[m")
        if not estoque:
            print("Nenhum produto cadastrado!")
        else:
            for produto in estoque:
                print(f"ID: {produto['id']} | Nome: {produto['nome']} | "
                      f"Categoria: {produto['categoria']} | Quantidade: {produto['quantidade']} | Preço: {produto['preco']:.2f}")

                if produto["quantidade"] < 5:
                    print("Estoque baixo!")

    elif opcao == "4":
        print("\033[35mSaindo do programa...\033[m")
        break

    else:
        print("\033[31mOpção inválida.\033[m Tente novamente.")


