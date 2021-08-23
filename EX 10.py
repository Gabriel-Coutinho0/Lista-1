cigarros_d = int(input('Quantos cigarros você usa? '))
cigarros_a = int(input('Quantos anos você fumou: '))
tempo_d = (cigarros_d * 10) / 1440
tempo_a = cigarros_a * 365 
tempo_t = (tempo_d * tempo_a) 
print (f'O tempo perdido em dias sera de: {tempo_t:.2f}')
