import numpy as np
from amostras import dataset

a = lambda x, y: abs(x-y)
b = lambda x, y: 1 if x < y else -1


def interacao(entrada, pesos, vieses, gabarito,
			  erro_anterior, sentido, amplitude):

	ps = np.copy(pesos)
	vs = np.copy(vieses)
	se = np.copy(sentido)
	am = np.copy(amplitude)

	e = a(np.dot(entrada, ps) + vs, gabarito)
	erro_atual = np.array(np.concatenate((entrada * e[0], entrada * e[1], e)))
	se = se * b(erro_atual, erro_anterior)
	am = am + se

	ps = ps + np.array([am[0:12], am[12:24]]) * np.array([erro_atual[0:12], erro_atual[12:24]])
	vs = vs + am[24:26] * erro_atual[24:26]

	return (ps, vs, erro_atual, sentido, amplitude)


def ephoc():

	p_0 = np.random.default_rng().random((2, 12))
	v_0 = np.array([0.1, -0.2])
	e_0 = np.random.default_rng().random((26,))
	s_0 = np.zeros(26)
	a_0 = np.zeros(26)
	val_tr = np.zeros(1500)
	i = 0
	for i in dataset[0:1501]:

		estado = interacao(i[0:12], p_0, v_0, i[12], e_0, s_0, a_0)
		p_0, v_0 = estado[0], estado[1]
		e_0, s_0, a_0 = estado[2], estado[3], estado[4]
		val_tr[i] = 0
		i += 1

	return tuple(p_0, v_0, val_tr)
