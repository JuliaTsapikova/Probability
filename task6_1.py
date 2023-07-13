#Известно, что генеральная совокупность распределена нормально 
# со средним квадратическим отклонением, равным 16. Найти доверительный 
# интервал для оценки математического ожидания a с надежностью 0.95, 
# если выборочная средняя M = 80, 
#а объем выборки n = 256.

import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy.stats import norm 
import math


mean_std = np.sqrt(16) / 256
interval = t_stat(80, mean_std,256 - 1, 0.05, 'two-sided')
print(interval)
