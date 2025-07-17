nome = input('Digite seu nome: ')
peso_str = input('Digite seu peso (kg): ')
peso = float(peso_str.replace(',', '.'))
altura_str = input('Digite sua altura (m): ')
altura = float(altura_str.replace(',', '.'))

imc = peso / (altura ** 2)
imc_arredondado = round(imc, 2)
if imc_arredondado <= 18.5:
    print('Seu IMC está abaixo do peso')
elif imc_arredondado >= 18.5 and imc_arredondado <= 24.99:
    print('Seu IMC está normal')
elif imc_arredondado >= 25 and imc_arredondado <= 29.99:
    print('Seu IMC está sobrepeso')
else:
    print('Seu IMC está Obeso')

print(nome, 'você tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc é:', imc_arredondado)