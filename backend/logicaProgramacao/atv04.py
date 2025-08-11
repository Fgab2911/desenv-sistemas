#criar função de menu de opções e pedir a opção desejada ao usuário 
#criar função de depósito 
#criar função de saque 
#criar função de ver saldo 
#ao digitar "sair" encerrar o programa 


saldo = 0
def menu():
    while opcao != "sair":

        print("=== Menu de Opções === \n")
        print ("1 - Depositar \n")

        opcao = input("digite a opção")

        if opcao == "1":
            depositar(saldo)

        elif opcao == "2":
            sacar(saldo)

        elif opcao == "3":
            versaldo(saldo)

        elif opcao == "sair":
            ("")
            break

def depositar(saldo):
    valor = input("digite o valor do deposito")
    saldo += valor

def sacar(saldo):
    valor = input("digite o valor do saque: ")
    saldo -= valor

def versaldo()
print("seu saldo é: ", saldo)
