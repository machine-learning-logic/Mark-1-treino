import numpy as np

a = lambda x: x if x>0 else x * 0.5
b = lambda x: 0.25 * x if x<0 else 0.125 * x

def retro(entrada, pesos, pesos_, vieses, vieses_, saida, gabarito):

    vs = np.copy(vieses)
    vs_ = np.copy(vieses_)

    def inferir():

        def atualiza_vs(n):
            vs[n] = a(np.sum(pesos[n] * entrada))

        for i in range(8):
            atualiza_vs(i)

        vs_[0] = np.sum(vs * pesos_[0])
        vs_[1] = np.sum(vs * pesos_[1])

    vs_1_erro=np.array([gabarito[0] - vs_[0],
                        gabarito[1] - vs_[1]])
    ps_1_erro=np.zeros((2,8))
    ps_1_erro[0] =  / pesos_[0]
    ps_1_erro[1] = vs_1_erro[1] / pesos_[1]

    #considerar a relu e dividir por 8
    vs_0_erro=

def otimizador():
  r_par=np.zeros(112)
  r_impar=np.zeros(112)
  t=np.zeros(112)

  def ciclo():
      r_par=retro()
      t=t+(r_par<r_impar)*2*tp-tp
      p=p+t*tp

      r_impar=retro()
      t=t+(r_impar<r_par)*2*tp-tp
      p=p+t*tp
def ephoc(dados, gab):