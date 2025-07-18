"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Luiz Otávio') #forma mais comum de definir um texto em python
print(1, 'Luiz "Otávio"')

# Aspas duplas
print("Luiz Otávio") #também uma forma comum de definir um texto em python (fica a sua escolha)
print(2, "Luiz 'Otávio'")

# Escape
print("Luiz \"Otávio\"") #\ escape, usa-se fala pro python que as aspas é para serem usadas na string

# r
print(r"Luiz \"Otávio\"") #string bruta (raw), utilizando o r"" ele não tira a \ invertida, util quando usar caminhos do windowns
print('Explícito', 'é', 'melhor " do que implícito')