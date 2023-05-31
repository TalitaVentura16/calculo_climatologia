from random import random
xxx, yyy = "", ""

# pentada = open(xxx, 'r')
# pentclim = open(yyy, 'r')

NY, NP = 10, 15
pentada=[random() for i in range(NP)]
pentclim=[random() for i in range(NP)]

for k in range(NY):
  icont_i = 0
  icont_f = 0
  for i in range(NP):
    for j in range(i, i+8):
      if pentada[i] < pentclim[i]:
        icont_i += 1
      else:
        icont_f += 1

      if icont_i >= 6:
        kpi = k * i
        print(k, i, kpi[k])
      if icont_f >= 6:
        kpf = k * i
        print(k, i, kpf[k])
    
    for k in range(NY):
      dsl = kpf[k] - kpi[k]
      print(k, dsl)


