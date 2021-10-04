diasAlugado = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))

precoFinal = (60 * diasAlugado) + (0.15 * km)

print(f'O total a pagar é de {precoFinal:.2f}')