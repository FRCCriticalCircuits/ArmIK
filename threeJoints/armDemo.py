import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import time

# Lengths
y1, y2, y3 = 1.05, 1, 1.20

# Points to test
Px = 1              # Fixed x
Py_start = 1.5
Py_end = 3.0
Py_step = 0.1

# Boundary
bounds = [(-160 * np.pi / 180, 160 * np.pi / 180), (-160 * np.pi / 180, 160 * np.pi / 180), (-180 * np.pi / 180, 180 * np.pi / 180)]

# Loss Function
def objective(angles, Px, Py):
    theta1, theta2, theta3 = angles
    Px_estimate = -y1 * np.sin(theta1) - y2 * np.sin(theta1 + theta2) - y3 * np.sin(theta1 + theta2 + theta3)
    Py_estimate = y1 * np.cos(theta1) + y2 * np.cos(theta1 + theta2) + y3 * np.cos(theta1 + theta2 + theta3)
    return np.sqrt((Px - Px_estimate)**2 + (Py - Py_estimate)**2)

initial_guess = [0, 0, 0]

# Graph
plt.figure()
colors = ['y', 'r', 'g', 'b', 'm', 'c']

# Timing
total_time = 0

for i, Py in enumerate(np.arange(Py_start, Py_end, Py_step)):
    start_time = time.time()
    
    # Finding Solution
    result = minimize(objective, initial_guess, args=(Px, Py), bounds=bounds)
    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

    theta1_opt, theta2_opt, theta3_opt = result.x

    # Positions
    x1, y1_pos = 0, 0
    x2, y2_pos = x1 - y1 * np.sin(theta1_opt), y1_pos + y1 * np.cos(theta1_opt)
    x3, y3_pos = x2 - y2 * np.sin(theta1_opt + theta2_opt), y2_pos + y2 * np.cos(theta1_opt + theta2_opt)
    x4, y4_pos = x3 - y3 * np.sin(theta1_opt + theta2_opt + theta3_opt), y3_pos + y3 * np.cos(theta1_opt + theta2_opt + theta3_opt)

    # Lines
    color = colors[i % len(colors)]
    plt.plot([x1, x2], [y1_pos, y2_pos], color, linewidth=6)  # Origin  - Joint 1
    plt.plot([x2, x3], [y2_pos, y3_pos], color, linewidth=3)  # Joint 1 - Joint 2
    plt.plot([x3, x4], [y3_pos, y4_pos], color, linewidth=2)  # Joint 2 - End

    # Points
    plt.plot(x1, y1_pos, 'ko')  # Origin
    plt.plot(x2, y2_pos, 'ko')  # Joint 1
    plt.plot(x3, y3_pos, 'ko')  # Joint 2
    plt.plot(x4, y4_pos, 'ko')  # End

# Graphing Settings
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Arm')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()

# Output
print("Total optimization time: {:.2f} seconds".format(total_time))
print("Optimal angles for each position:")
for Py in np.arange(Py_start, Py_end, Py_step):
    start_time = time.time()
    result = minimize(objective, initial_guess, args=(Px, Py), bounds=bounds)
    end_time = time.time()
    elapsed_time = end_time - start_time
    theta1_opt, theta2_opt, theta3_opt = result.x
    print("Py = {:.1f}: θ1 = {:.2f}, θ2 = {:.2f}, θ3 = {:.2f}, Time = {:.4f} seconds".format(Py, theta1_opt, theta2_opt, theta3_opt, elapsed_time))
