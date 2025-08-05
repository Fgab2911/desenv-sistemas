senha_correta = input("configure uma senha")
senha = input("digite a senha")

while senha != senha_correta:
    print("senha invalida")
    senha = input("digite a senha novamente")

print("senha correta") 

#pedir nome e senha ao usuario 
#mostrar "bem vindo" quando acertar a senha e o nome
#após pedir o salario do usuario 
#mostrar salario anual 
#se o salario anual for maior que 100 mil mostrar mensagem "rico"

senhacorreta = input("configure a senha")
senha = input("digite a senha")
salario = float(input("digite seu salario"))
nome = input("digite o nome")

while senha != senha_correta:
    print("senha incorreta")
    senha = input("digite a senha novamente")

print("bem vindo")

salarioanual = salario * 12
if(salarioanual > 100.000)
print("rico")

else:
    print("faz o L")
