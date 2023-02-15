import numpy as np
from scipy.stats import t

mother_heights = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
daughter_heights = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]

diff = [h1 - h2 for h1, h2 in zip(mother_heights, daughter_heights)]
diff_mean = np.mean(diff)
diff_std = np.std(diff, ddof=1)

t_val = t.ppf(0.975, 9) # 0.975, так как мы используем двусторонний доверительный интервал
CI = (diff_mean - t_val * diff_std / np.sqrt(10), diff_mean + t_val * diff_std / np.sqrt(10))

print(f"95% доверительный интервал для разности среднего роста: [{CI[0]:.2f}, {CI[1]:.2f}]")
