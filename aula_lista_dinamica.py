"""Aula 2 — Cadastro dinâmico de tipos de frutas, sem duplicatas.

Situação-problema: uma feira deseja cadastrar os tipos de frutas disponíveis.
O usuário pode adicionar novos tipos enquanto desejar; um nome já cadastrado
não deve ser inserido novamente. Ao final, exiba a lista e seu tamanho.
"""

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

# Começamos com 'sim' para permitir a primeira execução do while.
# O while testa a condição antes de cada repetição.
continuar = "sim"
while continuar == "sim":
    # input() retorna texto. strip() remove espaços das extremidades.
    # title() padroniza a capitalização: 'banana' e 'BANANA' viram 'Banana'.
    # Não corrige acentos: 'maca' continua diferente de 'maçã'.
    novo_item = input("Informe uma fruta para adicionar à lista: ").strip().title()

    # Texto vazio ('') significa que nenhum nome foi informado.
    if novo_item == "":
        print("Informe um nome de fruta. Nenhum item foi adicionado.")
    elif novo_item in frutas:
        # Só usamos index() depois de confirmar que o valor está na lista.
        posicao = frutas.index(novo_item)
        print(f"{frutas[posicao]} já está cadastrada no índice {posicao}.")
    else:
        # append() altera a lista, adicionando a fruta ao final.
        frutas.append(novo_item)
        # Depois da adição, o índice -1 corresponde à fruta recém-cadastrada.
        print(f"A fruta {frutas[-1]} foi adicionada com sucesso.")

    # lower() converte para minúsculas: ' SIM ' passa a ser 'sim'.
    # Apenas 'sim' mantém o laço; 'não' ou qualquer outra resposta encerra.
    continuar = input("Deseja continuar? [sim ou não]: ").strip().lower()

# A ausência de indentação indica que estas linhas estão fora do while.
# Elas executam uma única vez, depois que o cadastro termina.
print(f"Lista final de frutas: {frutas}")
print(f"A feira tem {len(frutas)} tipos de frutas cadastrados.")
print("Programa encerrado.")
