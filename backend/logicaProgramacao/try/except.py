#criar um novo arquivo py para a aula
#pesquisar o funcionamento do try/except
#criar um resumo do funcionamento com #(comente)
#crie 3 exemplos de uso do try/except
#além do try/except, usar a função e lista nos exercícios

#--------------------------------------------------

Quando você executa um código em Python, é bem comum encontrar erros: 

def acessar_lista(lista, i):
    try:
        print(lista[i])
    except IndexError:
        print("Erro: Índice fora do alcance.")

minha_lista = [10, 20, 30]
acessar_lista(minha_lista, 2)  # 30
acessar_lista(minha_lista, 5)  # Erro

#-----------------------------------------------------

#try/except em Python:
#Objetivo: Tratar exceções (erros) sem interromper o programa.
#try: Bloco onde você coloca o código que pode gerar erro.
#except: Bloco onde você define como lidar com o erro (caso ocorra).
#else (opcional): Executado se o código do try não gerar erro.
#finally (opcional): Executado sempre, independentemente de erro ou não. Ideal para liberar recursos.
#Exemplo Básico:
#O except captura o erro e evita que o programa pare.
#Tipos de Exceções:
#ZeroDivisionError: Divisão por zero.
#FileNotFoundError: Arquivo não encontrado.
#ValueError: Valor inválido, etc.
#IndexError: Erro ao tentar acessar um índice que não existe em uma lista, tupla ou string.
#TypeError: Erro quando há operação ou função aplicada a um objeto de tipo inadequado.
#NameError: Erro quando uma variável ou nome não está definido.

#------------------------------------------------------

def dividir(numerador, denominador):
    try:
        return numerador / denominador
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"

# Exemplo de uso
resultado = dividir(10, 0)
print(resultado)  # Erro de divisão por zero

resultado = dividir(10, 2)
print(resultado)  # Saída: 5.0

#------------------------------------------------------

def adicionar_na_lista(lista, indice, valor):
    try:
        lista[indice] = valor  # Tenta adicionar o valor no índice especificado
    except IndexError:
        return "Erro: Índice fora do alcance da lista!"

# Exemplo de uso
minha_lista = [1, 2, 3]
print(adicionar_na_lista(minha_lista, 5, 10))  # Índice inválido
print(minha_lista)  # Lista original

adicionar_na_lista(minha_lista, 1, 10)  # Substitui valor na posição 1
print(minha_lista)  # Saída: [1, 10, 3]

#-------------------------------------------------------

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Erro: O arquivo não foi encontrado!"

# Exemplo de uso
print(ler_arquivo("arquivo_inexistente.txt"))  # Arquivo não encontrado

# Criar e testar com um arquivo existente
with open("exemplo.txt", "w") as file:
    file.write("Conteúdo do arquivo.")

print(ler_arquivo("exemplo.txt"))  # Conteúdo do arquivo