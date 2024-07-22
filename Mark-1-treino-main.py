import numpy as np

a = lambda x, y: abs(x-y)
b = lambda x, y: 1 if x < y else -1


def interacao(entrada, pesos, vieses, gabarito,
			  erro_anterior, sentido, amplitude):

	ps = np.copy(pesos)
	vs = np.copy(vieses)
	se = np.copy(sentido)
	am = np.copy(amplitude)

	e = a(np.dot(entrada, ps) + vs, gabarito)
	erro_atual = np.array(np.concatenate(
		(entrada * e[0], entrada * e[1], e)))
	se = se * b(erro_atual, erro_anterior)
	am = am + se

	ps = ps + np.array([am[0:12], am[12:24]])
	vs = vs + am[24:26]

	return (ps, vs, erro_atual, sentido, amplitude)


def ephoc(carac, tipo):

	