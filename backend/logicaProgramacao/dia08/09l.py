import os

 ARQUIVO = "carros.txt"

 def carregar():
     carros = []
     if os.path.exists(ARQUIVO):
         with open(ARQUIVO, 'r') as f:
             for linha in f:
                 if linha.strip():
                     id, marca, modelo, ano, preco = linha.strip().split('|')
                     carros.append({'id': id, 'marca': marca, 'modelo': modelo, 'ano': ano, 'preco': preco})
     return carros

 def salvar(carros):
     with open(ARQUIVO, 'w') as f:
         for c in carros:
             f.write(f"{c['id']}|{c['marca']}|{c['modelo']}|{c['ano']}|{c['preco']}\n")

 def cadastrar():
     carros = carregar()
     novo_id = str(int(carros[-1]['id']) + 1) if carros else '1'
     marca = input("Marca: ")
     modelo = input("Modelo: ")
     ano = input("Ano: ")
     preco = input("Preço: ")
     carros.append({'id': novo_id, 'marca': marca, 'modelo': modelo, 'ano': ano, 'preco': preco})
     salvar(carros)

 def listar():
     carros = carregar()
     for c in carros:
         print(f"{c['id']}: {c['marca']} {c['modelo']} - {c['ano']} - R${c['preco']}")

 def alterar():
     carros = carregar()
     id = input("ID do carro: ")
     for c in carros:
         if c['id'] == id:
             c['marca'] = input(f"Marca ({c['marca']}): ") or c['marca']
             c['modelo'] = input(f"Modelo ({c['modelo']}): ") or c['modelo']
             c['ano'] = input(f"Ano ({c['ano']}): ") or c['ano']
             c['preco'] = input(f"Preço ({c['preco']}): ") or c['preco']
             salvar(carros)
             return
     print("Carro não encontrado!")

 def excluir():
     carros = carregar()
     id = input("ID do carro: ")
     novos_carros = [c for c in carros if c['id'] != id]
     if len(novos_carros) < len(carros):
         salvar(novos_carros)
         print("Carro excluído!")
     else:
         print("Carro não encontrado!")

 def menu():
     while True:
         print("\n1-Cadastrar 2-Listar 3-Alterar 4-Excluir 5-Sair")
         op = input("Opção: ")
         if op == '1': cadastrar()
         elif op == '2': listar()
         elif op == '3': alterar()
         elif op == '4': excluir()
         elif op == '5': break

 if __name__ == "__main__":