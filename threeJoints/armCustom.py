import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

y1, y2, y3 = 1.05, 1, 1.20
Px = 1
Py = 1.5

# Boundary
bounds = [(-160 * np.pi / 180, 160 * np.pi / 180), (-160 * np.pi / 180, 160 * np.pi / 180), (-180 * np.pi / 180, 180 * np.pi / 180)]

# Loss
def objective(angles):
    theta1, theta2, theta3 = angles
    Px_estimate = -y1 * np.sin(theta1) - y2 * np.sin(theta1 + theta2) - y3 * np.sin(theta1 + theta2 + theta3)
    Py_estimate = y1 * np.cos(theta1) + y2 * np.cos(theta1 + theta2) + y3 * np.cos(theta1 + theta2 + theta3)
    return np.sqrt((Px - Px_estimate)**2 + (Py - Py_estimate)**2)

initial_guess = [0, 0, 0]

# Optimization
result = minimize(objective, initial_guess, bounds=bounds)
theta1_opt, theta2_opt, theta3_opt = result.x

# Calc
x1, y1_pos = 0, 0
x2, y2_pos = x1 - y1 * np.sin(theta1_opt), y1_pos + y1 * np.cos(theta1_opt)
x3, y3_pos = x2 - y2 * np.sin(theta1_opt + theta2_opt), y2_pos + y2 * np.cos(theta1_opt + theta2_opt)
x4, y4_pos = x3 - y3 * np.sin(theta1_opt + theta2_opt + theta3_opt), y3_pos + y3 * np.cos(theta1_opt + theta3_opt + theta3_opt)

# Lines
plt.figure()
plt.plot([x1, x2], [y1_pos, y2_pos], 'y', linewidth=6)
plt.plot([x2, x3], [y2_pos, y3_pos], 'r', linewidth=3)
plt.plot([x3, x4], [y3_pos, y4_pos], 'g', linewidth=2)

# Points
plt.plot(x1, y1_pos, 'ko')
plt.plot(x2, y2_pos, 'ko')
plt.plot(x3, y3_pos, 'ko')
plt.plot(x4, y4_pos, 'ko')

# Plot
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Arm')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()

# Output
print(objective(result.x))
print("Optimal angles: θ1 = {:.2f}, θ2 = {:.2f}, θ3 = {:.2f}".format(theta1_opt, theta2_opt, theta3_opt))
