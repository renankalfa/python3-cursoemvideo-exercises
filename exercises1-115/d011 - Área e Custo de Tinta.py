print('Calculadora de Área e Custo de Tinta')
l = float(input('Largura da parede (metros): '))
a = float(input('Altura da parede (metros): '))
print(f'\n Altura da parede: {a}m; \n Largura da parede: {l}m')
area = l * a
t = (area)/2
print(f'\n Calculando a área da parede... \n Área: {area:.3f}m²')
print(f'\n Calculando a quantidade de tinta necessária... \n Quantidade de tinta: {t:.3f}L')