import numpy as np
from amostras import dataset
from resultados_4 import pesos as ps_
from resultados_4 import vieses as vs_

a = lambda x, y: (x -y) ** 2
b = lambda x, y: -1 if x > y else 1


def interacao(entrada, pesos, vieses, gabarito,
			  erro_anterior, sentido, amplitude):

	ps = np.copy(pesos)
	vs = np.copy(vieses)
	se = np.copy(sentido)
	am = np.copy(amplitude)

	e = np.dot(entrada, ps) + vs
	e[0] = ((e[0] < e[1]) == gabarito) #a(e[0], gabarito) *
	e[1] = ((e[0] < e[1]) == gabarito) #a(e[1], float(not gabarito)) *
	erro_atual = np.array(np.concatenate((entrada * e[0], entrada * e[1], e)))
	se = se * [i for i in map(b, erro_atual, erro_anterior)]
	am = am + se

	ps = np.swapaxes(ps, 0, 1)
	ps = ps + np.array([am[0:12], am[12:24]])
	ps = np.swapaxes(ps, 0, 1)
	vs = vs + am[24:26]

	return (ps, vs, erro_atual, se, am)


def ephoc():

	p_0 = np.random.default_rng().normal(-0.003, 0.003, (12, 2))
	#p_0 = ps_

	v_0 = np.array([0.00001, -0.00002])
	#v_0 = np.array([0.0061520999999999625, 0.00594577999999995])
	#v_0 = vs_
	e_0 = np.random.default_rng().random((26,))
	s_0 = np.zeros(26) + 3.2e-9
	a_0 = np.zeros(26) + 2e-6
	val_tr = np.zeros(1000)
	j = 0
	for i in dataset[0:1000]:

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


def batch(n):

	p_0 = np.random.default_rng().normal(-0.001, 0.001, (12, 2))
	v_0 = np.array([0.0, 0.0])
	e_0 = np.random.default_rng().random((26,))
	s_0 = np.zeros(26) + 1e-18
	a_0 = np.zeros(26) + 1e-4
	val_tr = np.zeros(n)
	j = 0
	batch_erro = np.zeros(26)

	for h in range(n):

		#batch_erro = np.zeros(26)

		for i in dataset[0:1000]:

			estado = interacao(i[0:12], p_0, v_0, i[12], e_0, s_0, a_0)
			batch_erro = estado[2] + batch_erro

		batch_erro = batch_erro * 0.01
		s_0 = s_0 * np.array([i for i in map(b, batch_erro, e_0)])
		e_0 = batch_erro
		a_0 = a_0 + s_0
		p_0 = p_0 + np.swapaxes(np.array([a_0[0:12], a_0[12:24]]), 0, 1)
		v_0 = v_0 + a_0[24:26]
		val_tr[j] = e_0[24] + batch_erro[25]
		j += 1


	return (p_0, v_0, val_tr)