import numpy as np
from scipy.stats import t

# задаем выборку
x = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])

# вычисляем выборочное среднее и стандартное отклонение
x_mean = np.mean(x)
s = np.std(x, ddof=1)

#Определяем значение t-критерия для выбранного уровня доверия 0.95) и степеней свободы, равных 9
alpha = 0.05 # уровень значимости
df = len(x) - 1 # степени свободы
t_value = t.ppf(1 - alpha/2, df)

#Вычисление доверительного интервала
lower = x_mean - t_value * s / np.sqrt(len(x))
upper = x_mean + t_value * s / np.sqrt(len(x))

print('Доверительный интервал:', (lower, upper))