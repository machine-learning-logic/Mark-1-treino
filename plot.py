from matplotlib import pyplot as plt
import numpy as np
from resultados import erro

g = np.arange(1500)
p = plt.plot(g, erro)
plt.show()
