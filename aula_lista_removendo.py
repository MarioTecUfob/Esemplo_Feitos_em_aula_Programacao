"""Aula 4 — Menu para cadastrar, consultar e remover registros.
Situação-problema: uma feira precisa manter uma lista de registros de frutas.
O programa deve permitir adicionar nomes (inclusive repetidos), consultar as
ocorrências, remover uma ocorrência pelo nome e sair pelo menu.
"""

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

# True mantém o menu em repetição; a opção 4 executa break para encerrá-lo.
while True:
    # Multiplicar uma string por um inteiro repete seu conteúdo.
    print("=" * 35)
    # center() centraliza o título usando espaços até a largura informada.
    print("MENU DA FEIRA".center(35))
    print("-" * 35)
    print("1 - Cadastrar fruta")
    print("2 - Consultar registros")
    print("3 - Remover uma ocorrência")
    print("4 - Sair")
    print("=" * 35)

    # A opção fica como texto: digitar uma letra não causa erro de conversão.
    # Por isso, as comparações abaixo usam '1', '2', '3' e '4', com aspas.
    opcao = input("O que você deseja fazer? ").strip()
    if opcao == "1":
        novo_item = input("Informe uma fruta para cadastrar: ").strip().title()
        if novo_item == "":
            print("Informe um nome de fruta. Nenhum item foi adicionado.")
        else:
            # Repetições são permitidas: cada adição representa outro registro.
            frutas.append(novo_item)
            print(f"A fruta {frutas[-1]} foi cadastrada com sucesso.")

    elif opcao == "2":
        print(f"Lista atual: {frutas}")
        print(f"Total de registros: {len(frutas)}")
        if len(frutas) == 0:
            print("Nenhuma fruta cadastrada.")
        else:
            # A auxiliar é reiniciada a CADA consulta, pois o cadastro pode mudar.
            frutas_contadas = []
            for fruta in frutas:
                if fruta not in frutas_contadas:
                    quantidade = frutas.count(fruta)
                    print(f"{fruta}: {quantidade} ocorrência(s)")
                    frutas_contadas.append(fruta)
            print(f"Total de tipos de frutas: {len(frutas_contadas)}")

    elif opcao == "3":
        if len(frutas) == 0:
            print("A lista está vazia. Não há frutas para remover.")
        else:
            print(f"Frutas cadastradas: {frutas}")
            removida = input("Informe a fruta que deseja remover: ").strip().title()
            # Sem esta verificação, remove() causaria ValueError se o nome faltasse.
            if removida in frutas:
                # remove() altera a lista e retorna None; não atribuímos seu retorno.
                # Se houver nomes repetidos, apenas a primeira ocorrência é removida.
                frutas.remove(removida)
                print(f"Uma ocorrência de {removida} foi removida.")
                print(f"Lista atualizada: {frutas}")
            else:
                print(f"A fruta '{removida}' não está cadastrada.")

    elif opcao == "4":
        # break sai do while imediatamente, sem pedir confirmação de continuidade.
        print("Programa encerrado.")
        break

    else:
        # Uma opção inválida não altera a lista; o menu é apresentado novamente.
        print("Opção inválida. Digite 1, 2, 3 ou 4.")
