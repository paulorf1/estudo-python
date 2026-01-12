# os.listdir para navegar em caminhos
# C:\Users\Paulo\Desktop\Estudo Python\EXEMPLO
# caminho = r'C:\\Users\\Paulo\\Desktop\\Estudo Python\\EXEMPLO'

import os

caminho = os.path.join('/Users', 'Paulo', 'Desktop',
                       'Estudo Python', 'EXEMPLO')
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
