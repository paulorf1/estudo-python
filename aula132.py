# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor
        self.cor_tampa = None

    @property
    def cor(self):
        print('Estou no getter')
        # print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no setter')
        # if valor == 'Rosa':
        #     raise ValueError ('Não aceito essa cor')
        # print('Setter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
            
# def mostrar(caneta):
#     return caneta.cor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Verde'
# getter -> obrter valor
print(caneta.cor)
print(caneta.cor_tampa)