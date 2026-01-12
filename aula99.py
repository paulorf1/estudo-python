# from sys import path

# import aula99_package.modulo
# from aula99_package import modulo
# # from aula99_package.modulo import soma_do_modulo
# from aula99_package.modulo import *

# print(soma_do_modulo(1,2))
# print(aula99_package.modulo.soma_do_modulo(1,2))
# print(modulo.soma_do_modulo(1,2))
# # print(soma_do_modulo)
# print(variavel)
# print(nova_variavel)

# import aula99_package
# # print(*path, sep='\n')



# from aula99_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()



import aula99_package

from aula99_package import falar_oi, soma_do_modulo

print(aula99_package.soma_do_modulo(2,3))
falar_oi()
