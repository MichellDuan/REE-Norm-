import numpy as np
import matplotlib.pyplot as plt

# Chondrite normalization for REE
# Load data from text file
with open('D:/Peking University/2024Mitchell/Himalaya/LA/7_YD02-11B_REE.txt', 'r') as file:
    lines = file.readlines()

# Extract data from text file, skipping the first line
data = np.array([line.strip().split() for line in lines[1:]])

# Sun & McDonough (1989) chondrite values
chondrite_values = {
    'La': 0.237,
    'Ce': 0.612,
    'Pr': 0.095,
    'Nd': 0.467,
    'Sm': 0.153,
    'Eu': 0.058,
    'Gd': 0.2055,
    'Tb': 0.0374,
    'Dy': 0.2540,
    'Ho': 0.0566,
    'Er': 0.1655,
    'Tm': 0.0255,
    'Yb': 0.170,
    'Lu': 0.0254
}

# Normalization
m, n = data.shape
REE_norm = np.zeros((m, n))
for i in range(n):
    column_name = lines[0].strip().split()[i]
    REE_norm[:, i] = data[:, i].astype(float) / chondrite_values[column_name]

# Eu/Eu*
Eu_anomaly = (2 * REE_norm[:, 5]) / (REE_norm[:, 4] + REE_norm[:, 6])

# Plot
x = [1, 1.01466, 1.02975, 1.04529, 1.07357, 1.08650, 1.09975, 1.11333, 1.12725, 1.14042, 1.15278, 1.16426, 1.17480, 1.18434]
plt.figure('Chondrite Normalized diagram')
for c in range(m):
    plt.semilogy(x, REE_norm[c, :], '-')
plt.ylabel('REE/Cl')
plt.ylim(0, 10000)
plt.xlim(1, 1.18434)
plt.xticks(x, ['La', 'Ce', 'Pr', 'Nd', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'])
plt.show()
