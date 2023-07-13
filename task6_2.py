#В результате 10 независимых измерений некоторой величины X, выполненных 
# с одинаковой точностью, получены опытные данные: 
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 
# Предполагая, что результаты измерений подчинены нормальному закону 
# распределения вероятностей, оценить 
# истинное значение величины X при помощи доверительного интервала, 
# покрывающего это значение с доверительной вероятностью 0,95.
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy.stats import norm 
import math

X = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
mean_X = X.mean()
std_X = X.std(ddof=1)
mean_std_X = std_X / (np.sqrt(len(X)))
interval = t_stat(mean_X, mean_std_X,len(X) - 1, 0.05, 'two-sided')
print(interval)