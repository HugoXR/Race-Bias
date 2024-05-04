import numpy as np
import os
import shutil
import random

diretorios = os.listdir('Dataset_Fair_Face_test_3/')

imagens = {diretorio: os.listdir('Dataset_Fair_Face_test_3/'+diretorio) for diretorio in diretorios}

for value in imagens:
    tamanho = len(imagens[value])
    remocao = abs(1500 - tamanho)
    valores = imagens[value]
    for i in range(remocao):
        imagem = random.choice(valores)
        os.remove(f'Dataset_Fair_Face_test_3/'+value+f'/{imagem}')
        valores.remove(imagem)
