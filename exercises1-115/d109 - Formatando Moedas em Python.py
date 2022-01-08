from d107 import moeda1

p = float(input('Digite o preço: R$ '))
print(f"Com o preço de {moeda1.moeda(p)}, temos")
print(f" -> O dobro é {moeda1.dobro(p,True)};")
print(f" -> A metade é {moeda1.metade(p,True)};")
print(f" -> Com aumento de 40% fica {moeda1.aumentar(p,40,True)};")
print(f" -> Com redução de 30% fica {moeda1.diminuir(p,30,True)}.")
