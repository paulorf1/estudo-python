# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna

@Multiplicar(10)
def soma(x,y):
    return x + y

dois_mais_quatro = soma(2,4)
print(dois_mais_quatro)