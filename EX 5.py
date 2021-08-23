produto = int(input('Valor do produto R$: '))
desconto = int(input('Porcentagem do desconto R: '))
porcentagem = desconto/100
valor_desconto = produto*porcentagem
valor_produto = produto-valor_desconto
print ('O desconto sera de R$: ', valor_desconto)
print (f'O Valor sera de R$: {valor_produto:.2f}')
