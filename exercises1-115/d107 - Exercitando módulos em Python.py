from d107 import moeda

p = float(input('Digite o preço: R$ '))
print(f"Com o preço de R${p:.2f}, temos\n"
      f" -> O dobro é R${moeda.dobro(p):.2f};\n"
      f" -> A metade é R${moeda.metade(p):.2f};\n"
      f" -> Com aumento de 50% fica R${moeda.aumentar(p):.2f};\n"
      f" -> Com redução de 50% fica R${moeda.diminuir(p):.2f}.")
