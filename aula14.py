""""""
a = 'AAAAA' #definindo variavel do tipo string
b = 'BBBBBB' #definindo variavel do tipo string
c = 1.1 #definindo variavel de ponto flutuante
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' #Esta é a sua string de formato, ela contém texto literal e campos de substituição dentro de chaves {}
formato = string.format(nome1=a, nome2=b, nome3=c) #Quando você chamar o método .format(), o Python irá substituir esses marcadores pelos valores que você especificar
print(formato) #imprimi o conteudo da variavel formato