print('=*' * 2, 'Leitor de Sexo', '=*' * 2)
print('[M] para Masculino \n[F] para Feminino')
sexo = str(input('Digite o seu sexo: ')).upper()
lista = ['M','F']

while sexo not in lista:
    sexo = str(input('Digite novamente: ')).upper()

if sexo == 'M':
    print(f'Você digitou {sexo} e você é do sexo masculino!')
if sexo == 'F':
    print(f'Você digitou {sexo} e você é do sexo feminino!')

print('Fim.')