import numpy as np
import matplotlib.pyplot as plt

def k(n):
    if n >= 0 and n <= 2:
        return 0
    elif n >= 3 and n <= 5:
        return 1
    elif n >= 6 and n <= 8:
        return 2
    else:
        return 3

T = np.array([123.5,123.2,130.1,126.6,127.9,125.9])

#расчёт Tsr
Tsr = np.zeros(4)

E = 0
for n in range(0,2+1):
    E = E + T[n]
Tsr[k(n)] = E/3

E = 0
for n in range(3,5+1):
    E = E + T[n]
Tsr[k(n)] = E/3

#расчёт S
S = np.zeros(4)

E = 0
for n in range(0,2+1):
    E = E + np.square(T[n]-Tsr[k(n)])
S[k(n)] = np.sqrt(E/2)

E = 0
for n in range(3,5+1):
    E = E + np.square(T[n]-Tsr[k(n)])
S[k(n)] = np.sqrt(E/2)

#расчёт SIGMA
SIGMA = np.zeros(4)

for k in range(0,3+1):
    SIGMA[k] = (4.3/np.sqrt(3))*S[k]

#Tist
Tist = list()
for k in range(0,3+1):
    Tist.append('{:.1f}'.format(Tsr[k])+'+-'+'{:.1f}'.format(SIGMA[k]))

#вывод результатов
for k in range(0,3+1):
    print('Результаты для измерений группы',k+1)
    print('Tsr = {:.1f}'.format(Tsr[k]))
    print('S = {:.1f}'.format(S[k]))
    print('SIGMA = {:.1f}'.format(SIGMA[k]))
    print('Tist =',Tist[k])
    print()