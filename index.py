real = float(input('Qual o valor em real? R$: '))

dolar = real / 5.5
euro = real / 0.92

print('Com R${:.2f}, pode comprar US${:.2f} e EUR{:.2f}'.format(real, dolar, euro))
