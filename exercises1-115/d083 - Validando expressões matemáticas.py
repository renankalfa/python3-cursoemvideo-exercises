expression = str(input('Digite a expressão matemática: '))
count = 0
for c in expression:
    if c == '(':
        count += 1
    if c == ')':
        count -= 1
    if count < 0:
        break
if count == 0:
    print('Expressão coerente!')
else:
    print('Expressão inválida!')