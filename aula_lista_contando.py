"""Aula 3 — Cadastro com repetições e contagem de ocorrências.

Situação-problema: a feira deseja registrar entradas de frutas e saber quantas
vezes cada nome aparece. Diferentemente da Aula 2, repetições são permitidas.
Cada elemento representa um registro, não uma medida de peso ou de estoque.
"""
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
continuar = "sim"

while continuar == "sim":
    # Padronizamos o texto para evitar separar 'Banana' de 'banana' na contagem.
    novo_item = input("Informe uma fruta para adicionar à lista: ").strip().title()
    if novo_item == "":
        print("Informe um nome de fruta. Nenhum item foi adicionado.")
    else:
        # Não verificamos duplicatas: nesta atividade elas são desejadas.
        frutas.append(novo_item)
        print(f"A fruta {frutas[-1]} foi adicionada com sucesso.")
    continuar = input("Deseja continuar? [sim ou não]: ").strip().lower()

print(f"Lista final: {frutas}")
# len() conta TODOS os registros, inclusive os nomes repetidos.
print(f"A feira tem {len(frutas)} registros de frutas.")
# Esta lista auxiliar começa vazia e guarda os nomes já apresentados.
# Ela não substitui nem remove elementos da lista original.
frutas_contadas = []
for fruta in frutas:
    # not in significa 'não está em'. Só contamos e exibimos um nome novo.
    # Quando o mesmo nome aparece novamente, este bloco é ignorado.
    if fruta not in frutas_contadas:
        # count() pesquisa a lista original inteira, não apenas o trecho percorrido.
        quantidade = frutas.count(fruta)
        print(f"{fruta}: {quantidade} ocorrência(s)")
        # Registramos que a fruta JÁ FOI apresentada, evitando novas impressões.
        # Esta linha fica dentro do if, depois da contagem e da exibição.
        frutas_contadas.append(fruta)
# O tamanho da auxiliar corresponde ao total de nomes distintos apresentados.
print(f"Quantidade de tipos de frutas: {len(frutas_contadas)}")
print("Programa encerrado.")
