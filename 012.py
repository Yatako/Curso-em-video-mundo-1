valor = float(input('insira um preço: '))

desconto = valor - (valor * 5) / 100

print('preço com desconto é de {:.3f}'.format(desconto))