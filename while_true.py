while True:
    print("\n===== MENU DA FEIRA =====")
    print("1 - Cadastrar fruta")
    print("2 - Consultar frutas")
    print("3 - Remover fruta")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError as erro:
        # Executa se a entrada não puder ser convertida em inteiro.
        print("Entrada inválida. Digite um número inteiro de 1 a 4.")
        print(erro)#Pega o erro
        continue  # Volta ao início do while e apresenta o menu novamente.

    if opcao == 1:
        print("Cadastrando fruta...")
    elif opcao == 2:
        print("Consultando frutas...")
    elif opcao == 3:
        print("Removendo fruta...")
    elif opcao == 4:
        print("Encerrando o programa.")
        break  # Encerra o laço.
    else:
        # A entrada é um inteiro, mas não corresponde a uma opção.
        print("Opção inválida. Escolha um número de 1 a 4.")

print("Você saiu do menu.")