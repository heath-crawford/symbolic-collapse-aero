# Collapse_Simulator_2D_Reynolds.py
# Simulates entropy collapse + overlays Reynolds number zones

import numpy as np
import matplotlib.pyplot as plt

# Grid size
grid_shape = (10, 10)

# Simulated entropy fields for O₁ and O₂
np.random.seed(42)
O1_entropy = np.random.uniform(0.9, 1.1, size=grid_shape)
O2_entropy = np.random.uniform(0.8, 1.2, size=grid_shape)

# Simulated Reynolds field (just mock data — tweak to reflect real ranges)
# Re = (rho * v * L) / mu, but here we simulate as a normalized field
Reynolds_field = np.random.uniform(1000, 5000, size=grid_shape)

# Thresholds
kappa_c = 0.08
laminar_threshold = 2000
turbulent_threshold = 4000

def calculate_divergence(o1, o2):
    return np.abs(o1 - o2)

def simulate_collapse(o1, o2, kappa):
    delta_phi = calculate_divergence(o1, o2)
    collapsed = delta_phi > kappa
    force_collapse = np.where(collapsed, kappa * delta_phi, 0)
    return delta_phi, collapsed, force_collapse

def analyze_reynolds(re_field):
    # 0 = laminar, 1 = transition, 2 = turbulent
    re_zones = np.zeros_like(re_field, dtype=int)
    re_zones[re_field > laminar_threshold] = 1
    re_zones[re_field > turbulent_threshold] = 2
    return re_zones

def plot_heatmap(data, title, cmap='viridis'):
    plt.imshow(data, cmap=cmap, interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    delta_phi, collapsed, forces = simulate_collapse(O1_entropy, O2_entropy, kappa_c)
    reynolds_zones = analyze_reynolds(Reynolds_field)

    print("Δϕ (Entropy Divergence):\\n", delta_phi)
    print("Collapse Triggered:\\n", collapsed)
    print("Symbolic Collapse Force Fᴄ:\\n", forces)
    print("Reynolds Zones (0 = laminar, 1 = transition, 2 = turbulent):\\n", reynolds_zones)

    # Visualize outputs
    plot_heatmap(delta_phi, "Entropy Divergence Δϕ")
    plot_heatmap(collapsed.astype(int), "Symbolic Collapse Zones (1 = collapse)")
    plot_heatmap(reynolds_zones, "Reynolds Zones (0 = laminar, 1 = trans, 2 = turbulent)")
    plot_heatmap(forces, "Symbolic Collapse Force Field Fᴄ")