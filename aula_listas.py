"""Aula 1 — Fundamentos e operações com listas em Python.

Objetivo: acompanhar o conteúdo do slide e observar como cada operação
altera uma lista. Execute este arquivo e compare as saídas com os comentários.
Os exemplos de remoção usam cópias para não interferirem uns nos outros.
"""

# 1. CRIAÇÃO: colchetes delimitam a lista; vírgulas separam os elementos.
# Uma lista mantém a ordem, permite repetições e pode ser modificada (mutável).
lista_vazia = []
nomes = ["Ana", "Bruno", "Carlos"]
# É possível misturar tipos, embora cada problema possa exigir um único tipo.
dados = [10, "Python", 3.14, True]
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
print(f"Lista inicial: {frutas}")

# 2. ACESSO: índices positivos começam em 0, não em 1.
# Índices negativos contam a partir do final: -1 é o último elemento.
print(f"Primeira fruta (índice 0): {frutas[0]}")
print(f"Terceira fruta (índice 2): {frutas[2]}")
print(f"Última fruta (índice -1): {frutas[-1]}")
# frutas[4] causaria IndexError: a lista inicial só tem índices de 0 a 3.

# 3. ALTERAÇÃO: a atribuição substitui o elemento de um índice existente.
# Não adiciona uma posição: a lista continua com quatro elementos.
frutas[1] = "Abacaxi"
print(f"Após substituir Banana: {frutas}")

# 4. ADIÇÃO: cada método tem uma finalidade diferente.
# append() adiciona UM elemento ao final da lista.
frutas.append("Melancia")

# insert(índice, valor) insere antes do elemento que ocupa aquela posição.
# Os elementos seguintes se deslocam; Pera passa a ocupar o índice 1.
frutas.insert(1, "Pera")

# extend() adiciona cada elemento da coleção recebida ao final da lista.
# append(["Kiwi", "Manga"]) adicionaria uma lista dentro da outra lista.
frutas.extend(["Kiwi", "Manga"])
print(f"Após as adições: {frutas}")

# 5. CONSULTAS: estas operações não alteram a lista.
# in verifica a presença e produz True ou False (valor booleano).
verificar = "Maçã" in frutas
print(f"Maçã está na lista? {verificar}")

# len() é uma função: informa o total de elementos, incluindo repetições.
quantidade_de_elementos = len(frutas)
print(f"Quantidade de elementos: {quantidade_de_elementos}")

# count() é um método: conta as ocorrências de um valor; retorna 0 se ausente.
contador = frutas.count("Pera")
print(f"Quantidade de ocorrências de Pera: {contador}")

# index() retorna o índice da PRIMEIRA ocorrência do valor.
# Se o valor não existir, causa ValueError; por isso verificamos com in.
if "Pera" in frutas:
    indice = frutas.index("Pera")
    print(f"A fruta do índice {indice} é {frutas[indice]}.")

# 6. CÓPIA: copy() cria outra lista, que pode receber novos elementos.
# Como os elementos deste exemplo são strings, esta cópia é suficiente.
# Em listas com outras listas internas, copy() é uma cópia superficial:
# as listas internas continuam compartilhadas (aprofundamento futuro).
copia_frutas = frutas.copy()
copia_frutas.append("Melancia")
print(f"Cópia: {copia_frutas}")
print(f"Melancia na cópia: {copia_frutas.count('Melancia')}")
print(f"Melancia na original: {frutas.count('Melancia')}")
# copia_frutas = frutas, sem copy(), apenas daria outro nome à MESMA lista.

# 7. PERCURSO: a cada repetição, fruta recebe um elemento de frutas.
# 'fruta' e 'frutas' são nomes escolhidos pelo programador, não palavras especiais.
print("Percorrendo a lista original:")
for fruta in frutas:
    print(fruta)

# 8. REMOÇÃO: cada demonstração parte da mesma lista-base.
# Assim, os índices de um exemplo não são afetados pela remoção anterior.
base_remocao = ["Maçã", "Banana", "Uva", "Laranja"]

# remove(valor) remove apenas a PRIMEIRA ocorrência e retorna None.
# O valor precisa existir; caso contrário, ocorrerá ValueError.
exemplo_remove = base_remocao.copy()
exemplo_remove.remove("Uva")
print(f"remove('Uva'): {exemplo_remove}")

# pop() remove E RETORNA o último elemento; a lista não pode estar vazia.
exemplo_pop = base_remocao.copy()
ultima_fruta = exemplo_pop.pop()
print(f"pop(): removeu {ultima_fruta}; restaram {exemplo_pop}")

# pop(índice) remove E RETORNA o elemento de um índice válido.
exemplo_pop_indice = base_remocao.copy()
primeira_fruta = exemplo_pop_indice.pop(0)
print(f"pop(0): removeu {primeira_fruta}; restaram {exemplo_pop_indice}")

# del é uma instrução, não um método: exclui pelo índice, sem retornar o valor.
exemplo_del = base_remocao.copy()
del exemplo_del[2]
print(f"del no índice 2: {exemplo_del}")

# clear() remove todos os elementos, mantendo a lista existente e vazia.
exemplo_clear = base_remocao.copy()
exemplo_clear.clear()
print(f"clear(): {exemplo_clear}")
