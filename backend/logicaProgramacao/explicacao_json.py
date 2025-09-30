#trabalhando com json - explicação_json.py

#{} - chaves: definir um objeto - ficha de cadastro
#[] - colchete: definir uma lista
# chave/valor: descreve o valor
#sempre importar seu json

import json
inventario = []
try:
    with open("loja.json", "r")as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    prin("arquivo não encontrado")
try:
    nome = input("digite o nome do produto")
    quantidade = int(input("digite a quantidade"))
    preço = float(input("digite o preço"))
    except ValueError:
        print("digite o valor corretamente")
# montar o objeto
nome_produto = {"nome"; nome, "quantidade": quantidade, "preço": preco, "em_estoque": quantidade > 0 } #expressao verdadeira ou falsa
#escrever o objeto no arquivo
inventario.append(novo_produto)
with open("loja.json", "w")as arquivo:
    json.dump(inventario, arquivo, indent = 4)
    #indent - formatar o arquivo json
    print("produto cadastrado com sucesso")