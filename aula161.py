# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence
from typing import Any, Iterator


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self.__next___index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        # print('GET ITEM', index)
        return self._data[index]

    def __setitem__(self, index, value):
        # print('SET ITEM', index, value)
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.__next___index >= self._index:
            self.__next___index = 0

            raise StopIteration

        value = self._data[self.__next___index]
        self.__next___index += 1
        return value


if __name__ == "__main__":
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    # print(lista._data)

    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')
