import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Number of experiments
N = 1000

# Noise vector
g = np.random.randn(N)

# Filter coefficients
a = [1, -1.27, 0.81]
x = lfilter([1], a, g)

# Parameters
mu = 0.004
h = np.zeros(2)
er = np.zeros(N-1)

# Filter coefficients
h1 = np.zeros(N-1)
h2 = np.zeros(N-1)

# Loop
for i in range(1, N-1):
    # Algorithm
    d_est = h[0] * x[i] + h[1] * x[i-1]
    e = x[i+1] - d_est
    h[0] = h[0] + mu * e * x[i]
    h[1] = h[1] + mu * e * x[i-1]

    # Coefficients updating
    h1[i] = h[0]
    h2[i] = h[1]
    er[i] = e

# Plot
plt.figure()
plt.plot(np.array([h1, h2]).T)
plt.plot(np.ones(N-1) * 1.27)
plt.plot(np.ones(N-1) * -0.81)
plt.grid(True)

plt.figure(2)
plt.plot(er**2)