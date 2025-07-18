"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
#maneiras de contornar o numero flutuante


# import decimal #1 forma
# numero_1 = decimal.Decimal('0,1')
# numero_2 = decimal.Decimal('0,7')

numero_1 = 0.1 # numero flutuante
numero_2 = 0.7 # numero flutuante
numero_3 = numero_1 + numero_2 # soma numero flutuante
print(numero_3) # resultado sem f string
# print(f'{numero_3:.2f}') # 2 forma, resultado com formatação
print(round(numero_3, 2)) # 3 forma, usado para arredondar casas decimais