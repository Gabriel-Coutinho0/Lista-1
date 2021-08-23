kmp = int(input('Os km percorridos são: '))
dias = int(input('Quantida de dias alugados: '))
kmp_r = kmp * 0.15
dias_a = dias * 60
print (f'O valor sera de R$: {kmp_r + dias_a:.2f}')
