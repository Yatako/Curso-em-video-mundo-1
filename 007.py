primeiraNota = float(input('Primeira nota do aluno: '))
segundaNota = float(input('Segunda nota do aluno: '))

mediaNota = (primeiraNota + segundaNota) / 2

print('A media entre {} e {} é {:.1f}' .format(primeiraNota, segundaNota, mediaNota))