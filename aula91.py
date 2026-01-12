# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

#Exemplo
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
        
gen = generator(n=5, maximum=8)
for n in gen:
    print(n)

#Exemplo
def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'Acabou'

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = generator(n=0)
for n in gen:
    print(n)