from M_1_treino import ephoc
import amostras

arrays = ephoc()
p = str([list(i) for i in arrays[0]])
v = str([list(i) for i in arrays[1]])
txt = f"pesos = {p}\nvieses = {v}erro  = {e}"
open("resultados.py", "w").write(txt)
