#usando (laços, função e try/except),crie um sistema para receber as 3 notas de um aluno e calcule a média anual. se digitar algo sem ser numero tratar o erro
#usando (lista, função, laços, try/except), você deverá criar uma lista com numeros e mensagens. se for numero, adicionar a uma lista a parte. se for 
#mensagem, tratar com o erro de tipo. ao final, mostrar a lista só com os numeros 
#criar uma lista com cadastro de usuario, cadastrar, alterar, excluir, listar, usar (função, lista, try/except, laços)


def media():
    try:

        nota1 = float(input("Nota da 1 Prova: ")) 
        nota2 = float(input("Nota da 2 Prova: ")) 
        nota3 = float(input("Nota da 3 Prova: ")) 


        media = nota1 + nota2 + nota3 /3
        print("soma:", media)
     
     
     

        
    except TypeError:
        print("Erro: - Não é possível somar tipos incompatíveis.")

    except ValueError:
        print("Erro: você digitou algo que não é um número.")

    except NameError:
        print("Erro: - Variável não definida.")


media()a

#-----------------------------------------------------------------

usuarios = []

def mostrar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        for i, u in enumerate(usuarios):
            print(f"{i} - {u['nome']} | {u['email']} | {u['idade']} anos")
        print()

def cadastrar():
    try:
        nome = input("Nome: ")
        email = input("Email: ")
        idade = int(input("Idade: "))
        usuarios.append({"nome": nome, "email": email, "idade": idade})
        print("Usuário cadastrado!\n")
    except:
        print("Erro no cadastro. Idade deve ser número.\n")

def alterar():
    mostrar_usuarios()
    try:
        i = int(input("Número do usuário a alterar: "))
        usuarios[i]['nome'] = input("Novo nome: ")
        usuarios[i]['email'] = input("Novo email: ")
        usuarios[i]['idade'] = int(input("Nova idade: "))
        print("Usuário alterado!\n")
    except:
        print("Erro ao alterar usuário.\n")

def excluir():
    mostrar_usuarios()
    try:
        i = int(input("Número do usuário a excluir: "))
        usuarios.pop(i)
        print("Usuário excluído!\n")
    except:
        print("Erro ao excluir usuário.\n")

def menu():
    while True:
        print("1. Cadastrar | 2. Listar | 3. Alterar | 4. Excluir | 5. Sair")
        opcao = input("Opção: ")
        print()
        if opcao == '1': cadastrar()
        elif opcao == '2': mostrar_usuarios()
        elif opcao == '3': alterar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida.\n")