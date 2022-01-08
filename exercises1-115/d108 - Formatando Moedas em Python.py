from d107 import moeda

p = float(input('Digite o preço: R$ '))
print(f"Com o preço de {moeda.moeda(p)}, temos")
print(f" -> O dobro é {moeda.moeda(moeda.dobro(float(p)))};")
print(f" -> A metade é {moeda.moeda(moeda.metade(p))};")
print(f" -> Com aumento de 50% fica {moeda.moeda(moeda.aumentar(p))};")
print(f" -> Com redução de 50% fica {moeda.moeda(moeda.diminuir(p))}.")
