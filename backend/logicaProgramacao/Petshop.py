#crie um sistema de gerenciamento de petshop
#deverá ter os campos: nome, raça, idade, sexo, nome dono, telefone do dono.
#o nome do arquivo json deve ser "petshop.json"
#faça o crud completo
#ao terminar, demonstrar o exercicio para o prefessor

import json

arquivo_json = "petshop.json"
petshop = []

# Lendo os dados do arquivo JSON
try:
    with open(arquivo_json, "r") as arquivo:
        petshop = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, será criado ao salvar os dados.")
except json.decoder.JSONDecodeError:
    print("Arquivo vazio ou corrompido, iniciando novo inventário.")

# cadastrar um novo pet
try:
    id = int(input("Digite o ID do pet: "))
    nome = input("Digite o nome do pet: ")
    raca = input("Digite a raça do pet: ")
    idade = int(input("Digite a idade do pet: "))
    sexo = input("Digite o sexo do pet (M/F): ")
    nome_dono = input("Digite o nome do dono: ")
    telefone_dono = input("Digite o telefone do dono: ")

    novo_pet = {
        "id": id,
        "nome": nome,
        "raca": raca,
        "idade": idade,
        "sexo": sexo.upper(),
        "nome_dono": nome_dono,
        "telefone_dono": telefone_dono
    }

    petshop.append(novo_pet)

    with open(arquivo_json, "w") as arquivo:
        json.dump(petshop, arquivo, indent=4)
    print("Pet cadastrado com sucesso!")

except ValueError:
    print("Erro: Digite os valores corretamente!")

# modificar o pet
try:
    id_modificar = int(input("\nDigite o ID do pet que deseja modificar: "))
    pet_encontrado = False

    for pet in petshop:
        if pet["id"] == id_modificar:
            print("Pet encontrado! Digite os novos dados:")
            pet["nome"] = input("Novo nome: ")
            pet["raca"] = input("Nova raça: ")
            pet["idade"] = int(input("Nova idade: "))
            pet["sexo"] = input("Novo sexo (M/F): ").upper()
            pet["nome_dono"] = input("Novo nome do dono: ")
            pet["telefone_dono"] = input("Novo telefone do dono: ")
            pet_encontrado = True
            break

    if not pet_encontrado:
        print("Pet com o ID informado não foi encontrado.")
    else:
        with open(arquivo_json, "w") as arquivo:
            json.dump(petshop, arquivo, indent=4)
        print("Pet atualizado com sucesso!")

except ValueError:
    print("Erro: Digite os valores corretamente!")

# excluir pet
try:
    id_excluir = int(input("\nDigite o ID do pet que deseja excluir: "))
    novo_petshop = []
    pet_excluido = False

    for pet in petshop:
        if pet["id"] != id_excluir:
            novo_petshop.append(pet)
        else:
            pet_excluido = True
            print("Pet excluído com sucesso!")

    if not pet_excluido:
        print("Pet com o ID informado não foi encontrado.")
    else:
        with open(arquivo_json, "w") as arquivo:
            json.dump(novo_petshop, arquivo, indent=4)

except ValueError:
    print("Erro: Digite os valores corretamente!")

# listar pets
try:
    with open(arquivo_json, "r") as arquivo:
        petshop = json.load(arquivo)

    if not petshop:
        print("\nNenhum pet cadastrado.")
    else:
        print("\n------ Lista de Pets Cadastrados ------")
        for pet in petshop:
            print(f"\n-- PET ID {pet.get('id')} --")
            print(f"Nome: {pet.get('nome')}")
            print(f"Raça: {pet.get('raca')}")
            print(f"Idade: {pet.get('idade')} anos")
            print(f"Sexo: {pet.get('sexo')}")
            print(f"Dono: {pet.get('nome_dono')}")
            print(f"Telefone do Dono: {pet.get('telefone_dono')}")

except FileNotFoundError:
    print("Arquivo não encontrado.")
