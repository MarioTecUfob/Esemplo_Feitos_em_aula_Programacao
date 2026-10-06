# Programação I: listas e estruturas de repetição em Python

**Disciplina:** Programação I · **Docente:** Mário Novaes

Nesta aula, vamos trabalhar com listas e construir um cadastro de frutas para uma feira. O conteúdo reúne as operações apresentadas no slide: criação, acesso por índices, alteração, adição, remoção e consulta.

Os quatro arquivos podem ser executados separadamente. Comece pelos exemplos de listas e avance até o menu de cadastro. Ao longo do README, há explicações de `while`, `while True`, `break`, `continue` e tratamento de entradas inválidas com `try` e `except`.

## 1. Objetivos de aprendizagem

Ao concluir os exemplos, você deverá conseguir:

- Criar listas vazias e listas com elementos.
- Acessar e alterar elementos usando índices positivos e negativos.
- Diferenciar `append()`, `insert()` e `extend()`.
- Consultar presença, tamanho, posição e número de ocorrências.
- Percorrer uma lista com `for` e controlar cadastros com `while`.
- Contar nomes repetidos usando uma lista auxiliar e `not in`.
- Diferenciar remoção pelo valor e pelo índice.
- Escolher entre um laço com condição e `while True`.
- Usar `break` para sair de um laço e `continue` para passar à próxima repetição.
- Construir um menu e tratar entradas inválidas com `try` e `except ValueError`.

**Conhecimentos prévios:** variáveis, strings, `input()`, `print()`, condições (`if`, `elif`, `else`) e operadores de comparação. As estruturas de repetição são retomadas nos exemplos.

## 2. Organização dos arquivos

Estude nesta ordem:

| Etapa | Arquivo | Conteúdo principal |
| --- | --- | --- |
| 1 | [aula_listas.py](aula_listas.py) | Operações do slide, cópia e percurso; exemplos independentes de remoção |
| 2 | [aula_lista_dinamica.py](aula_lista_dinamica.py) | Cadastro de tipos de frutas sem duplicatas |
| 3 | [aula_lista_contando.py](aula_lista_contando.py) | Cadastro com repetições e contagem de ocorrências |
| 4 | [aula_lista_removendo.py](aula_lista_removendo.py) | Menu com cadastro, consulta, remoção e saída |

Cada programa começa com sua própria lista. Os dados ficam na memória: encerrar e executar novamente o arquivo restaura a lista inicial. Não há gravação em banco de dados ou arquivo.

## 3. Como executar

Você precisa do **Python 3** instalado. Os programas utilizam apenas recursos da linguagem; não é necessário instalar bibliotecas com `pip`.

1. Baixe os arquivos e mantenha-os na mesma pasta.
2. Abra essa pasta no VS Code ou em outro editor.
3. Abra um terminal nessa pasta.
4. Execute um arquivo por vez:

```bash
python aula_listas.py
python aula_lista_dinamica.py
python aula_lista_contando.py
python aula_lista_removendo.py
```

No Windows, se o comando `python` não estiver disponível, tente `py`. No Linux ou macOS, tente `python3`. Por exemplo:

```bash
py aula_lista_contando.py
```

O primeiro arquivo executa demonstrações sem pedir entrada. Os demais aguardam respostas no terminal. Digite a resposta no terminal e pressione **Enter**.

## 4. O que é uma lista?

Uma lista é uma estrutura que reúne elementos em uma sequência. Ela é:

- **Ordenada:** preserva a sequência dos elementos; isso não significa ordenação alfabética automática.
- **Mutável:** permite adicionar, substituir e remover elementos.
- **Capaz de armazenar repetições:** o mesmo valor pode ocupar várias posições.

```python
minha_lista = []                        # Lista vazia.
nomes = ["Ana", "Bruno", "Carlos"]       # Lista com strings.
dados = [10, "Python", 3.14, True]       # Lista com tipos diferentes.
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
```

Os colchetes `[]` delimitam a lista e as vírgulas separam seus elementos. Listas podem ser utilizadas para representar sequências semelhantes a vetores nas atividades introdutórias, mas a lista do Python pode crescer e conter tipos diferentes.

## 5. Acesso por índices

O **índice** indica a posição de um elemento. A contagem positiva começa em **zero**.

| Elemento | Índice positivo | Índice negativo |
| --- | --- | --- |
| Maçã | `0` | `-4` |
| Banana | `1` | `-3` |
| Uva | `2` | `-2` |
| Laranja | `3` | `-1` |

```python
frutas[0]   # "Maçã": primeiro elemento.
frutas[2]   # "Uva": terceiro elemento.
frutas[-1]  # "Laranja": último elemento.
```

Para uma lista não vazia com `n` elementos, os índices positivos válidos vão de `0` a `n - 1`. Acessar um índice inexistente causa `IndexError`. Em uma lista vazia, nem mesmo o índice `0` ou `-1` é válido.

## 6. Alteração e adição

### Alterar um elemento

```python
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
frutas[1] = "Abacaxi"
# Resultado: ["Maçã", "Abacaxi", "Uva", "Laranja"]
```

A atribuição substitui o conteúdo de uma posição existente. A quantidade de elementos permanece igual.

### Adicionar elementos

| Operação | Finalidade | Exemplo |
| --- | --- | --- |
| `append(valor)` | Adicionar um elemento ao final | `frutas.append("Melancia")` |
| `insert(indice, valor)` | Inserir antes do elemento da posição indicada | `frutas.insert(1, "Pera")` |
| `extend(colecao)` | Adicionar os elementos de uma coleção ao final | `frutas.extend(["Kiwi", "Manga"])` |

No exemplo de `insert(1, "Pera")`, Pera passa a ocupar o índice `1`, e os elementos a partir dessa posição se deslocam. Inserir ou remover pode mudar os índices dos elementos seguintes.

**Atenção à diferença entre `append()` e `extend()`:**

```python
lista_a = ["Maçã"]
lista_a.append(["Kiwi", "Manga"])
# Resultado: ["Maçã", ["Kiwi", "Manga"]]
# Dois elementos: uma string e uma lista interna.

lista_b = ["Maçã"]
lista_b.extend(["Kiwi", "Manga"])
# Resultado: ["Maçã", "Kiwi", "Manga"]
# Três elementos: três strings.
```

## 7. Consultas e cópia

Considere a lista a seguir para todos os exemplos desta tabela:

```python
frutas = ["Maçã", "Banana", "Banana", "Uva"]
```

| Expressão | Resultado | Significado |
| --- | --- | --- |
| `len(frutas)` | `4` | Total de elementos, incluindo repetições |
| `"Banana" in frutas` | `True` | O valor está presente |
| `"Pera" not in frutas` | `True` | O valor está ausente |
| `frutas.count("Banana")` | `2` | Quantas vezes o valor aparece |
| `frutas.count("Pera")` | `0` | Um valor ausente tem zero ocorrências |
| `frutas.index("Banana")` | `1` | Índice da primeira ocorrência |
| `frutas.copy()` | Uma nova lista com os mesmos elementos | Cópia superficial |

`len()` é uma **função**, chamada com a lista como argumento. Já `count()`, `index()` e `copy()` são **métodos**, chamados após o ponto no objeto lista.

`index()` causa `ValueError` se o valor não existir. Verifique antes:

```python
if "Banana" in frutas:
    print(frutas.index("Banana"))
```

### Copiar é diferente de atribuir outro nome

```python
original = ["Maçã", "Banana"]
copia = original.copy()
copia.append("Uva")
# original continua ["Maçã", "Banana"].
# copia passa a ser ["Maçã", "Banana", "Uva"].
```

Se usássemos `copia = original`, os dois nomes apontariam para a **mesma lista**. Uma alteração feita por um deles apareceria no outro.

`copy()` é suficiente para os exemplos com strings. Em listas que contêm outras listas, a cópia é superficial: as listas internas continuam compartilhadas.

## 8. Percorrer uma lista com `for`

```python
for fruta in frutas:
    print(fruta)
```

A variável `fruta` recebe um elemento a cada repetição, na ordem da lista. Os nomes `fruta` e `frutas` foram escolhidos para facilitar a leitura; o Python não deduz uma relação entre singular e plural.

A indentação indica o bloco que será repetido. Se houver nomes duplicados, cada ocorrência também será percorrida.

## 9. Cadastro dinâmico com `while`

Nos arquivos de cadastro, o laço começa com:

```python
continuar = "sim"
while continuar == "sim":
    # Cadastro e pergunta sobre continuidade.
    continuar = input("Deseja continuar? [sim ou não]: ").strip().lower()
```

`==` compara os valores. `=` atribui um valor à variável.

O `while` repete enquanto a condição for verdadeira. Ao digitar `não`, o programa sai do laço e exibe o resultado. Nesta implementação, **qualquer resposta diferente de `sim` encerra**, inclusive `s`, uma resposta vazia ou um erro de digitação. A primeira tentativa de cadastro ocorre porque a variável começa com `sim`.

### Tratamento dos nomes digitados

```python
novo_item = input("Informe uma fruta: ").strip().title()
```

- `input()` devolve uma string.
- `strip()` remove espaços nas extremidades.
- `title()` padroniza a capitalização: ` BANANA ` torna-se `Banana`.
- A condição `novo_item == ""` impede cadastrar texto vazio.

Esse tratamento não valida se o nome é realmente uma fruta e não corrige acentos ou grafia. `Maça`, `Maca` e `Maçã` continuam sendo valores diferentes. Os nomes iniciais utilizam a grafia `Maçã`.

Na Aula 2, `in` impede duplicatas. Nas Aulas 3 e 4, as repetições são permitidas para demonstrar a contagem. O total representa **registros digitados**, não quilogramas nem uma quantidade real de estoque.

## 10. Contar sem repetir a exibição: `not in` e lista auxiliar

```python
frutas_contadas = []
for fruta in frutas:
    if fruta not in frutas_contadas:
        quantidade = frutas.count(fruta)
        print(f"{fruta}: {quantidade}")
        frutas_contadas.append(fruta)
```

As duas listas têm funções diferentes:

| Lista | O que armazena |
| --- | --- |
| `frutas` | Todos os registros, inclusive repetições |
| `frutas_contadas` | Os nomes cuja contagem já foi exibida |

A linha `frutas_contadas.append(fruta)` guarda o nome que acabou de ser contado e exibido. Quando o mesmo nome aparecer novamente, `not in` será falso e o bloco será ignorado. A lista original permanece com todos os registros.

Sem esse `append()`, a auxiliar ficaria vazia e o programa exibiria a contagem novamente a cada ocorrência. `len()` não substitui essa linha: ele informa o tamanho de uma lista, mas não adiciona elementos. Depois do laço, `len(frutas_contadas)` informa quantos nomes diferentes foram apresentados.

Veja o teste de mesa para `frutas = ["Banana", "Uva", "Banana"]`:

| Passo | `fruta` | Auxiliar antes | Entra no `if`? | Saída | Auxiliar depois |
| --- | --- | --- | --- | --- | --- |
| 1 | Banana | `[]` | Sim | `Banana: 2` | `["Banana"]` |
| 2 | Uva | `["Banana"]` | Sim | `Uva: 1` | `["Banana", "Uva"]` |
| 3 | Banana | `["Banana", "Uva"]` | Não | Nenhuma | `["Banana", "Uva"]` |

`count()` consulta a lista inteira. Por isso a primeira passagem já informa duas ocorrências de Banana, mesmo antes de o `for` chegar à segunda Banana.

No menu, a auxiliar é criada novamente em cada consulta. Assim, um cadastro ou uma remoção pode ser considerado na próxima exibição. Aqui usamos uma lista auxiliar para praticar o conteúdo da aula. Em cadastros maiores, vale estudar outras formas de contagem, pois `in` e `count()` fazem buscas repetidas na lista.

### Exemplo de uso da Aula 3

A lista inicial tem quatro registros. Cadastre `banana`, responda `sim`, cadastre `Banana` e responda `não`. O resultado inclui:

```text
Lista final: ['Maçã', 'Banana', 'Uva', 'Laranja', 'Banana', 'Banana']
A feira tem 6 registros de frutas.
Maçã: 1 ocorrência(s)
Banana: 3 ocorrência(s)
Uva: 1 ocorrência(s)
Laranja: 1 ocorrência(s)
Quantidade de tipos de frutas: 4
```

Há seis registros, mas apenas quatro nomes distintos.

## 11. Remoção de elementos

| Operação | Critério | Retorno | Cuidado |
| --- | --- | --- | --- |
| `remove(valor)` | Primeira ocorrência do valor | `None` | Valor ausente causa `ValueError` |
| `pop()` | Último elemento | Elemento removido | Lista vazia causa `IndexError` |
| `pop(indice)` | Índice indicado | Elemento removido | Índice inexistente causa `IndexError` |
| `del lista[indice]` | Índice indicado | Não é uma expressão de retorno | Índice inexistente causa `IndexError` |
| `clear()` | Todos os elementos | `None` | A lista passa a ser `[]` |

Cada linha abaixo é uma demonstração independente, partindo novamente de `["Maçã", "Banana", "Uva", "Laranja"]`:

| Comando | Lista depois |
| --- | --- |
| `frutas.remove("Uva")` | `["Maçã", "Banana", "Laranja"]` |
| `frutas.pop()` | `["Maçã", "Banana", "Uva"]` |
| `frutas.pop(0)` | `["Banana", "Uva", "Laranja"]` |
| `del frutas[2]` | `["Maçã", "Banana", "Laranja"]` |
| `frutas.clear()` | `[]` |

**Não execute todos os comandos de remoção do slide em sequência supondo os mesmos índices.** Cada remoção muda a lista. Na Aula 1, cópias independentes permitem observar cada operação a partir da mesma lista-base.

### `remove()` não devolve a fruta removida

```python
frutas = ["Banana", "Banana", "Uva"]
frutas.remove("Banana")
# Restam ["Banana", "Uva"]. Apenas a primeira ocorrência foi removida.
```

Se você escrever `resultado = frutas.remove("Banana")`, a variável `resultado` receberá `None`. Para remover pelo índice e recuperar o elemento, utilize `pop(indice)`.

Também não escreva `frutas = frutas.append("Pera")`: `append()` altera a lista e retorna `None`. `insert()`, `extend()` e `clear()` igualmente alteram a lista sem devolver uma nova lista.

## 12. O menu da Aula 4

| Opção | Comportamento |
| --- | --- |
| `1` | Cadastra um nome não vazio; permite repetições |
| `2` | Exibe a lista, o total de registros e as ocorrências por nome |
| `3` | Remove uma ocorrência se o nome existir |
| `4` | Encerra o programa com `break` |
| Outra entrada | Exibe uma mensagem e reapresenta o menu |

O menu usa `while True`. Como a condição é sempre verdadeira, ele depende do `break` da opção `4` para terminar normalmente. Não há pergunta adicional sobre continuidade: após cada operação, o menu aparece novamente.

No arquivo `aula_lista_removendo.py`, a opção digitada permanece como string e é comparada com `"1"`, `"2"`, `"3"` e `"4"`. O nome a remover passa pelo mesmo tratamento usado no cadastro, e a verificação com `in` evita remover valores inexistentes.

Mais adiante, veremos outra versão do menu: a opção será convertida para inteiro e a conversão será tratada com `try` e `except`. Nesse caso, as comparações serão com `1`, `2`, `3` e `4`, sem aspas.

## 13. Controle da repetição: `while True`, `break` e `continue`

### Como funciona o `while`

O `while` verifica uma condição antes de cada repetição. Se ela for verdadeira, executa o bloco indentado. Ao chegar ao final do bloco, volta a verificar a condição. Quando a condição se torna falsa, segue para a primeira instrução depois do laço.

```python
contador = 1

while contador <= 3:
    print(contador)
    contador += 1  # Equivale a contador = contador + 1.

print("Contagem encerrada.")
```

Saída:

```text
1
2
3
Contagem encerrada.
```

Depois de imprimir `3`, o contador passa a valer `4`. A condição `4 <= 3` é falsa, e o laço termina. Se retirarmos o incremento, o contador continuará valendo `1` e esse exemplo repetirá sem parar.

Use um `while` com condição quando a regra de continuidade puder ser expressa diretamente, como `continuar == "sim"` ou `tentativas < 3`. Para percorrer todos os elementos de uma lista, geralmente o `for` é mais direto.

### Quando usar `while True`

`True` é o valor booleano verdadeiro. Em `while True`, a condição permanece verdadeira; portanto, ela não encerra o laço sozinha. No menu, definimos a saída dentro do bloco com `break`.

```python
while True:
    resposta = input("Digite 'sair' para encerrar: ").strip().lower()

    if resposta == "sair":
        break

    print(f"Você digitou: {resposta}")

print("Programa encerrado.")
```

Se o usuário digitar `olá`, o programa exibe a resposta e pergunta novamente. Se digitar `sair`, executa `break` e segue para a mensagem fora do laço.

Use `while True` em menus que devem continuar disponíveis até o usuário escolher sair ou em perguntas que precisam ser repetidas até uma entrada válida. Ele é útil quando a decisão de continuar depende de informações obtidas dentro da repetição.

Ao escrever um laço assim, identifique a condição que permitirá chegar ao `break`. Sem uma saída alcançável, o programa continuará repetindo até ser interrompido externamente.

### `break`: encerrar o laço

O `break` encerra imediatamente o laço em que está. As instruções restantes daquela repetição não são executadas, e o programa segue depois do laço.

```python
frutas = ["Maçã", "Banana", "Uva", "Laranja"]

for fruta in frutas:
    print(f"Verificando: {fruta}")

    if fruta == "Uva":
        print("Uva encontrada. Busca encerrada.")
        break

print("Fim da busca.")
```

A saída mostra Maçã, Banana e Uva. Laranja não é verificada porque o `break` encerra o `for` ao encontrar Uva. A mensagem `Fim da busca.` é exibida porque está fora do laço.

Use `break` quando o trabalho daquela repetição já tiver sido concluído: o usuário escolheu sair, um valor de encerramento foi digitado ou o elemento procurado foi encontrado. No cadastro, por exemplo, pode-se usar a palavra `sair` para indicar o fim da entrada de dados.

`break` encerra o laço, não necessariamente o programa. Se houver um laço dentro de outro, ele encerra apenas o laço mais interno que contém a instrução.

### `continue`: pular o restante da repetição atual

O `continue` pula as instruções que ainda seriam executadas naquela repetição. Ele mantém o laço em funcionamento: no `while`, volta à verificação da condição; no `for`, passa ao próximo elemento.

```python
frutas = ["Maçã", "", "Banana", "Uva"]

for fruta in frutas:
    if fruta == "":
        continue  # Ignora o nome vazio e passa ao próximo elemento.

    print(f"Fruta cadastrada: {fruta}")

print("Consulta encerrada.")
```

A saída mostra Maçã, Banana e Uva. O elemento vazio é percorrido, mas não chega ao `print()` porque o `continue` pula essa instrução naquela passagem.

Use `continue` para ignorar uma entrada inválida, um registro vazio ou um item que não deve ser processado. No menu, ele permite voltar à pergunta depois de uma conversão inválida, sem executar as opções abaixo.

Em um `while` controlado por contador, confira se o `continue` pode pular a atualização do contador. Se isso acontecer, a condição pode permanecer verdadeira indefinidamente.

### Diferença entre as instruções

| Recurso | Efeito | Exemplo de uso |
| --- | --- | --- |
| `while condicao` | Repete enquanto a condição for verdadeira | Continuar o cadastro enquanto a resposta for `sim` |
| `while True` | Mantém a condição sempre verdadeira; a saída é decidida no bloco | Mostrar um menu até a opção de saída |
| `break` | Encerra o laço imediatamente | Sair do menu ou parar uma busca |
| `continue` | Pula o restante da passagem atual e continua o laço | Ignorar uma entrada inválida e perguntar novamente |

`break` e `continue` podem ser usados em `while` e `for`. São instruções de controle, não funções: não usam parênteses e precisam estar dentro de um laço.

### A indentação define o que será repetido

```python
while True:
    opcao = input("Digite 4 para sair: ")

    if opcao == "4":
        break

    print("Esta mensagem está dentro do while.")

print("Esta mensagem está fora do while.")
```

O `print()` indentado pertence ao laço e pode executar várias vezes. O último `print()` está fora dele e executa depois do `break`. Digitar `4` pula a mensagem interna e permite chegar à mensagem externa.

## 14. Entradas inválidas: `try` e `except ValueError`

`input()` sempre devolve texto. Para trabalhar com uma opção numérica, podemos usar `int()`:

```python
opcao = int(input("Escolha uma opção: "))
```

Uma entrada como `"2"` pode ser convertida para o inteiro `2`. Já `"abc"`, `"2.5"` ou uma entrada vazia causam `ValueError`. Sem tratamento, esse erro interrompe a execução normal do programa.

O `try` delimita o trecho que pode produzir a exceção. O `except ValueError` define o que fazer se essa exceção ocorrer:

```python
while True:
    try:
        opcao = int(input("Escolha uma opção de 1 a 4: "))
    except ValueError as erro:
        print("Entrada inválida. Digite um número inteiro de 1 a 4.")
        print(erro)  # Mostra a explicação técnica produzida pelo Python.
        continue

    if 1 <= opcao <= 4:
        print(f"Opção válida: {opcao}")
        break

    print("Número fora das opções. Escolha de 1 a 4.")
```

Nesse exemplo, o laço termina quando uma opção válida é recebida. Ele valida a entrada; ainda não executa as operações de cadastro.

Se o usuário digitar `abc`, a saída do tratamento será:

```text
Entrada inválida. Digite um número inteiro de 1 a 4.
invalid literal for int() with base 10: 'abc'
```

Em `except ValueError as erro`, `erro` é o nome escolhido para receber o objeto da exceção. `print(erro)` exibe sua mensagem. Isso ajuda a entender o problema durante o estudo. Se quiser mostrar somente a orientação ao usuário, retire `print(erro)` e use apenas `except ValueError:`.

O `continue` impede que o programa use `opcao` após uma conversão que falhou. A variável pode nem ter recebido um valor nessa tentativa; por isso o programa deve voltar à pergunta.

Há duas verificações diferentes:

| Entrada | Conversão com `int()` | Tratamento |
| --- | --- | --- |
| `abc`, `2.5` ou texto vazio | Falha com `ValueError` | Executa o `except` e pergunta novamente |
| `7` | Funciona: resulta no inteiro `7` | Verifica o intervalo e informa que a opção não existe |
| `2` | Funciona: resulta no inteiro `2` | Aceita a opção |

Use `try` e `except ValueError` ao converter entradas para números quando o usuário puder digitar um texto inadequado. Mantenha o `try` próximo da operação que você deseja tratar; neste caso, apenas a leitura e a conversão. Para verificar se uma fruta existe na lista antes de removê-la, o teste com `in` continua sendo uma solução direta.

Depois de converter com `int()`, compare com números sem aspas: `opcao == 3`. Se mantiver a entrada como string, compare com `"3"`. O inteiro `3` e a string `"3"` são valores de tipos diferentes.

## 15. Exemplo de menu com tratamento de entrada

Este exemplo reúne `while True`, `try`, `except`, `continue` e `break`. As opções 1, 2 e 3 apenas exibem mensagens para que você acompanhe o fluxo; as operações completas estão em `aula_lista_removendo.py`.

```python
while True:
    print("\n===== MENU DA FEIRA =====")
    print("1 - Cadastrar fruta")
    print("2 - Consultar frutas")
    print("3 - Remover fruta")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError as erro:
        print("Entrada inválida. Digite um número inteiro de 1 a 4.")
        print(erro)
        continue  # Volta ao menu sem executar os testes abaixo.

    if opcao == 1:
        print("Cadastrando fruta...")
    elif opcao == 2:
        print("Consultando frutas...")
    elif opcao == 3:
        print("Removendo fruta...")
    elif opcao == 4:
        print("Encerrando o programa.")
        break  # Sai do while e segue para a mensagem final.
    else:
        print("Opção inválida. Escolha um número de 1 a 4.")

print("Você saiu do menu.")
```

Teste as entradas `abc`, `7`, `2` e `4`, nessa ordem:

| Entrada | Caminho percorrido | O que acontece depois |
| --- | --- | --- |
| `abc` | A conversão falha → `except` → `continue` | Mostra as mensagens de erro e reapresenta o menu |
| `7` | A conversão funciona → `else` | Informa que a opção não existe e chega ao final do bloco; o laço repete |
| `2` | A conversão funciona → `elif opcao == 2` | Mostra a mensagem de consulta e chega ao final do bloco; o laço repete |
| `4` | A conversão funciona → `elif opcao == 4` → `break` | Sai do laço e exibe `Você saiu do menu.` |

Observe que as opções `2` e `7` voltam ao menu mesmo sem `continue`. Ao chegar ao final do bloco, o `while` já inicia outra repetição. O `continue` é necessário no tratamento do erro porque queremos pular as instruções que ainda estão abaixo do `except`.

