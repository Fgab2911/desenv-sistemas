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




soma = 0
for i in range(1, 21):
    soma += i

print(f'A soma dos números de 1 a 20 é: {soma}')

soma_usuario = 0

while True:
    try:
        numero = int(input('Digite um número (ou 0 para parar): '))
        if numero == 0:
            break
        soma_usuario += numero
    except ValueError:
        print("Por favor, digite um número válido.")

print(f'A soma dos números digitados é: {soma_usuario}')