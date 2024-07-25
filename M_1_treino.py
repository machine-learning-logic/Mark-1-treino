import numpy as np
from amostras import dataset

a = lambda x, y: x ** 2 + y **y
b = lambda x, y: 1 if x < y else -1


def interacao(entrada, pesos, vieses, gabarito,
			  erro_anterior, sentido, amplitude):

	ps = np.copy(pesos)
	vs = np.copy(vieses)
	se = np.copy(sentido)
	am = np.copy(amplitude)

	e = a(np.dot(entrada, ps) + vs, gabarito)
	erro_atual = np.array(np.concatenate((entrada * e[0], entrada * e[1], e)))
	se = se * [i for i in map(b, erro_atual, erro_anterior)]
	am = am + se

	ps = np.swapaxes(ps, 0, 1)
	ps = ps + np.array([am[0:12], am[12:24]])
	ps = np.swapaxes(ps, 0, 1)
	vs = vs + am[24:26]

	return (ps, vs, erro_atual, se, am)


def ephoc():

	p_0 = np.random.default_rng().normal(-0.01, 0.01, (12, 2))
	v_0 = np.array([0.001, -0.002])
	e_0 = np.random.default_rng().random((26,))
	s_0 = np.zeros(26) + 0.00000001
	a_0 = np.zeros(26) + 0.00000001
	val_tr = np.zeros(1500)
	j = 0
	for i in dataset[0:1501]:

		estado = interacao(i[0:12], p_0, v_0, i[12], e_0, s_0, a_0)
		p_0, v_0 = estado[0], estado[1]
		e_1, s_0, a_0 = estado[2], estado[3], estado[4]
		val_tr[j] = estado[2][24] + estado[2][25]
		j += 1
		s_0 = s_0 * [i for i in map(b, e_1, e_0)]
		e_0 = e_1
		a_0 = a_0 + s_0
		p_0 = np.swapaxes(p_0, 0, 1)
		p_0 = p_0 + np.array([a_0[0:12], a_0[12:24]])
		p_0 = np.swapaxes(p_0, 0, 1)
		v_0 = v_0 + a_0[24:26]
		
	return (p_0, v_0, val_tr)

#corrigir dimenções incossistentes
