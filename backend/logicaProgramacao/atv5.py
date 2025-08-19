#crie uma lista de tarefas
#adicione 5 tarefas na lista
#adicione uma tarefa na posição 2 da lista
#remova a tarefa "lavar louça" da lista
#remover a tarefa da posição 1 da lista



tarefas = []


tarefas.append("lavar louça")
tarefas.append("estudar Python")
tarefas.append("fazer compras")
tarefas.append("limpar o quarto")
tarefas.append("exercício físico")


tarefas.insert(2, "pagar contas")


tarefas.remove("lavar louça")


del tarefas[1]


print("Lista de tarefas atualizada:")
for tarefa in tarefas:
    print("-", tarefa)

#-------------------------------------------------------------

#crie uma lista de 10 alunos, mostre "olá" + nome de cada aluno
#crie uma lista de 10 numeros mostre a soma de todos os numeros da lista
#crie uma lista de 20 numeros diga quantis numeros pares e impares tem na lista



# Lista de alunos e saudação
alunos = ["Ana", "Bruno", "Carlos", "janaina", "Eduardo", "Fernando", "Gustavo", "Helena", "Gabriel", "Juliana"]

for nome in alunos:
    print("Olá", nome)

print()

# Lista de 10 números e soma
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for num in numeros:
    soma = soma + num

print("Soma dos números:", soma)

print()

# Lista de 20 números e contagem de pares e ímpares
numeros_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pares = 0
impares = 0

for numero in numeros_20:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)


desafio: diga quantos numeros pares e impares tem na lista