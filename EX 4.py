salario = int(input('Seu salário: '))
aumento = int(input('Porcentagem do aumento: '))
porcentagem = (aumento / 100)
valor_aumento = salario * porcentagem
print ('O aumento sera de: ', valor_aumento)
print ('O salario atual sera de: ', salario + valor_aumento)
