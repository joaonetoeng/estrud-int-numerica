l = 4
discretizar = 10

deltal = 4/10

secoes = discretizar + 1

import numpy as np
r = np.arange(4, 0, -0.4)
print (r)



L=4
reserva=L
delta=0.4
lista=[]
i=0
while(reserva>0):
  reserva=L-(delta*i)
  lista.append((reserva,2))
  i+=1
print(lista)