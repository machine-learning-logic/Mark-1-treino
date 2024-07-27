from M_1_treino import batch #ephoc
import amostras
from matplotlib import pyplot as plt
import numpy as np

arrays = batch(100)#ephoc()
p = str([[float(i[0]), float(i[1])] for i in arrays[0]])
v = str([float(i) for i in arrays[1]])
txt = f"pesos = {p}\nvieses = {v}\nerro  = {str([float(i) for i in arrays[2]])}"
open("resultados_5.py", "w").write(txt)

from resultados_5 import *

g = np.arange(100)
p = plt.plot(g, erro)
plt.show()

def media_movel(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Parâmetros
window_size = 1  # Tamanho da janela da média móvel
max_iteracao = 100  # Limitar até a interação 750

# Limitar os dados de erro até a interação 750
erro_limitado = erro[:max_iteracao]

# Cálculo da média móvel
erro_suavizado = media_movel(erro_limitado, window_size)

# Ajustar o eixo x para corresponder ao tamanho da média móvel
g = np.arange(len(erro_suavizado))

# Plotar os resultados
'''plt.plot(g, erro_suavizado, label='Erro Suavizado')
plt.xlabel('Iterações')
plt.ylabel('Erro')
plt.legend()
plt.show()'''


from amostras import dataset

def eval(input):

    ev = np.dot(np.array(input[0:12]), np.array(pesos))
    ev = ev + np.array(vieses)

    return (ev[0] > ev[1]) == input[12]

print(sum(map(eval, dataset[0:2000])))