import numpy as np
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_NUMERIC, "de_RU")


def k(n):
    if 0 <= n <= 2:
        return 0
    elif 3 <= n <= 5:
        return 1
    elif 6 <= n <= 8:
        return 2
    else:
        return 3


# результаты измерений
# в мкс
T = np.array([
    63.5,
    64.5,
    63.9,
    86.9,
    84.0,
    86.9,
    98.3,
    97.2,
    97.0,
    113.4,
    113.6,
    114.4,
])

# в мм
D = np.array([
    22,
    30,
    35,
    40,
])

# расчёт Tsr
Tsr = np.zeros(4)

E = 0
for n in range(0, 2 + 1):
    E = E + T[n]
Tsr[k(n)] = E / 3

E = 0
for n in range(3, 5 + 1):
    E = E + T[n]
Tsr[k(n)] = E / 3

E = 0
for n in range(6, 8 + 1):
    E = E + T[n]
Tsr[k(n)] = E / 3

E = 0
for n in range(9, 11 + 1):
    E = E + T[n]
Tsr[k(n)] = E / 3

# расчёт S
S = np.zeros(4)

E = 0
for n in range(0, 2 + 1):
    E = E + np.square(T[n] - Tsr[k(n)])
S[k(n)] = np.sqrt(E / 2)

E = 0
for n in range(3, 5 + 1):
    E = E + np.square(T[n] - Tsr[k(n)])
S[k(n)] = np.sqrt(E / 2)

E = 0
for n in range(6, 8 + 1):
    E = E + np.square(T[n] - Tsr[k(n)])
S[k(n)] = np.sqrt(E / 2)

E = 0
for n in range(9, 11 + 1):
    E = E + np.square(T[n] - Tsr[k(n)])
S[k(n)] = np.sqrt(E / 2)

# расчёт SIGMA
SIGMA = np.zeros(4)

for k in range(0, 3 + 1):
    SIGMA[k] = (4.3 / np.sqrt(3)) * S[k]

# Tist
Tist = list()
for k in range(0, 3 + 1):
    Tist.append('{:.1f}'.format(Tsr[k]) + '+-' + '{:.1f}'.format(SIGMA[k]))

# вывод результатов
for k in range(0, 3 + 1):
    print('Результаты для измерений группы', k + 1)
    print('Tsr = {:.1f}'.format(Tsr[k]))
    print('S = {:.1f}'.format(S[k]))
    print('SIGMA = {:.1f}'.format(SIGMA[k]))
    print('Tist =', Tist[k])
    print()

# построение графика T(D)
font = {'family': 'Times New Roman',
        'size': 12}
plt.rc('font', **font)
plt.rcParams['axes.formatter.use_locale'] = True
s = 0.001
plt.grid()

# Tist
l = 0.3
h = 1
for k in range(0, 3 + 1):
    y = np.arange(Tsr[k] - SIGMA[k], Tsr[k] + SIGMA[k] + s, s)
    x = D[k] + 0 * y
    plt.plot(x, y, color='black', linewidth=h)

    x = np.arange(D[k] - l, D[k] + l + s, s)

    y = Tsr[k] + SIGMA[k] + 0 * x
    plt.plot(x, y, color='black', linewidth=h)

    y = Tsr[k] + 0 * x
    plt.plot(x, y, color='black', linewidth=h)

    y = Tsr[k] - SIGMA[k] + 0 * x
    plt.plot(x, y, color='black', linewidth=h)

plt.xlim(0)
plt.ylim(0)
plt.xlabel('D, мм', loc='right')

plt.savefig('graph.svg')
plt.show()
