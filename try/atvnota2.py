#sou o dono de uma concessionária e vi o sistema do dono da padaria. Gostaria de um sistema igual para meus carros.


# Lista para guardar os carros
carros = []                                            #Cria uma lista vazia onde todos os carros cadastrados vão ser guardados.

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== MENU DA CONCESSIONÁRIA ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")                         #Mostra as opções disponíveis para o usuário escolher o que quer fazer.
    print("3 - Alterar carro")
    print("4 - Excluir carro")
    print("5 - Sair")

# Função para cadastrar carro
def cadastrar():
    modelo = input("Modelo do carro: ")
    marca = input("Marca: ")
    ano = input("Ano: ")
    preco = input("Preço: R$ ")

    carro = {                                         #Pede as informações do carro e salva em um dicionário.  #Depois, adiciona esse dicionário à lista carros.

        "modelo": modelo,
        "marca": marca,
        "ano": ano,
        "preco": preco
    }

    carros.append(carro)
    print("Carro cadastrado com sucesso!")

# Função para listar carros
def listar():
    if len(carros) == 0:
        print("Nenhum carro cadastrado.")                             #Mostra todos os carros cadastrados, um por um, com o número (índice) de cada carro.
    else:
        print("\n=== Lista de Carros ===")
        for i in range(len(carros)):
            print(f"{i} - {carros[i]}")

# Função para alterar carro
def alterar():
    listar()
    indice = int(input("Digite o número do carro que deseja alterar: "))

    if 0 <= indice < len(carros):
        modelo = input("Novo modelo: ")                                          #Primeiro mostra a lista de carros.
        marca = input("Nova marca: ")                                            #Depois, o usuário escolhe qual carro quer alterar (pelo número).
        ano = input("Novo ano: ")                                                #O sistema então atualiza as informações daquele carro.
        preco = input("Novo preço: R$ ")

        carros[indice]["modelo"] = modelo
        carros[indice]["marca"] = marca
        carros[indice]["ano"] = ano
        carros[indice]["preco"] = preco

        print("Carro alterado com sucesso!")
    else:
        print("Número inválido.")

# Função para excluir carro
def excluir():
    listar()
    indice = int(input("Digite o número do carro que deseja excluir: "))          #Mostra os carros. Ousuario escolhe o numero do carro a ser excluido., afunção remove o carro da lista
 
    if 0 <= indice < len(carros):
        carros.pop(indice)
        print("Carro excluído com sucesso!")
    else:
        print("Número inválido.")

# Programa principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":                               #Fica repetindo o menu e executando o que o usuário escolher. Quando o usuário digita "5", o programa para.
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente de novo.")
