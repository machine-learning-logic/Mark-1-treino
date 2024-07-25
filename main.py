from M_1_treino import ephoc
import amostras

arrays = ephoc()
p = str([list(i) for i in arrays[0]])
v = str(list(arrays[1]))
txt = f"pesos = {p}\nvieses = {v}\nerro  = {str(list(e))}"
open("resultados.py", "w").write(txt)
