#3.Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 
# Используя эти данные построить 95% 
# доверительный интервал для разности среднего роста родителей и детей.
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy.stats import norm 
import math
X = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
Y = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
diff = X.mean() - Y.mean()
nx, ny = X.size, Y.size
diff_sd = np.sqrt(X.var(ddof=1)/nx + Y.var(ddof=1)/nx)
left, right = norm.interval(0.95, loc = diff, scale = diff_sd)
print("Доверительный интервал [{:.4};{:.4}]".format(left,right, right-left))
