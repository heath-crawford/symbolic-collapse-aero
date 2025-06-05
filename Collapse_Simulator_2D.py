# Collapse_Simulator_2D.py
# Simulates symbolic entropy collapse in a 2D grid

import numpy as np
import matplotlib.pyplot as plt

# Grid size (10x10 surface)
grid_shape = (10, 10)

# Simulated entropy fields for O₁ and O₂ (random for now, tweak as needed)
np.random.seed(42)
O1_entropy = np.random.uniform(0.9, 1.1, size=grid_shape)
O2_entropy = np.random.uniform(0.8, 1.2, size=grid_shape)

# Collapse threshold (symbolic ethics constant)
kappa_c = 0.08

def calculate_divergence(o1, o2):
    return np.abs(o1 - o2)

def simulate_collapse(o1, o2, kappa):
    delta_phi = calculate_divergence(o1, o2)
    collapsed = delta_phi > kappa
    force_collapse = np.where(collapsed, kappa * delta_phi, 0)
    return delta_phi, collapsed, force_collapse

def plot_heatmap(data, title, cmap='viridis'):
    plt.imshow(data, cmap=cmap, interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    delta_phi, collapsed, forces = simulate_collapse(O1_entropy, O2_entropy, kappa_c)

    print("Δϕ (Entropy Divergence):\\n", delta_phi)
    print("Collapse Triggered:\\n", collapsed)
    print("Symbolic Collapse Force Fᴄ:\\n", forces)

    # Plot outputs
    plot_heatmap(delta_phi, "Entropy Divergence Δϕ")
    plot_heatmap(collapsed.astype(int), "Collapse Zones (1 = collapse)")
    plot_heatmap(forces, "Collapse Force Field Fᴄ")