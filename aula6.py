# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(int('1'), type(int('1'))) #'1' é uma string (texto), int('1'): a função int() está tentando converter a string '1' para um número inteiro
print(type(float('1') + 1)) #quando você realiza uma operação matemática entre um int e um float, o resultado sempre será um float <class 'float'>
print(bool('')) #string vazia é considerada Falsy / false
print(str(11) + 'b') #transformouo o 11 em string e 'concatenou' com o b
print('11' + 'b') #transformouo o 11 em string de outra forma e 'concatenou' com o b