valor1 = int(input("valor1:"))
valor2 = int(input("valor2:"))

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2 

print("soma:", soma)
print("subtracao", subtracao)
print("multiplicacao", multiplicacao)
print("divisao", divisao)



salario = float (input("informe seu salario:"))
salarioanual = salario * 12

print("salario anual", salarioanual)

if (salario >5000):
    imposto = 0.08 * salario

elif (salario <5000):
    imposto = 0.05 * salario

print("imposto", imposto)