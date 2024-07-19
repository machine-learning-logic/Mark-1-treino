import numpy as np

a = lambda x, y: abs(x-y)


def retro(entrada, pesos, vieses, gabarito):

	e = a(np.dot(entrada, pesos) + vieses, gabarito)
	r_par = np.array([entrada * e[0], entrada * e[1], e])
	t_aprendizado = 0.01
	t_pesos = np.zeros((2, 12))
	t_vieses = np.zeros(2)

	def intera():

		e = a(np.dot(entrada, pesos) + vieses, gabarito)
		r_par = np.array([entrada * e[0], entrada * e[1], e])
		t_pesos += t_aprendizado
		t_vieses += t_aprendizado
