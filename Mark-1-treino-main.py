import numpy as np

a = lambda x, y: abs(x-y)

def inferir(entrada, pesos, vises):

	return np.dot(entrada, pesos)+vieses
	
def retro(entrada, vieses, saida, gabarito):
	
	e = a(saida, gabarito)
	return (np.array(entrada[0]*e[0], entrada[1]*e[1]), e)