# Try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('abrir arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('dividiu zero')
except IndexError:
    print('dividiu zero')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('não deu erro')
finally:
    print('fechar arquivo')