largura = float(input('largura da parede é? '))
altura = float(input('altura da parede é? '))
area = largura * altura
litroDeTinta = area / 2
print('A area é {}m2 \nA quantidade de tinta para pintar a parede é de {}l'.format(area, litroDeTinta))