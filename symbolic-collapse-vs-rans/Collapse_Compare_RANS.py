import airfrans as af
import numpy as np
import matplotlib.pyplot as plt
import csv

# Load a high-Reynolds RANS simulation
sim_name = 'airFoil2D_SST_31.283_-4.156_0.919_6.98_14.32'
sim = af.Simulation(root='C:/Users/heath_b8o4sl3/AEROSPACE_PROOF/AirfRANS_Data/Dataset', name=sim_name)

# Compute symbolic entropy field
field = np.linalg.norm(sim.velocity, axis=1)
normalized = (field - field.min()) / (field.max() - field.min())
delta_phi = normalized * 0.3

# Symbolic collapse threshold
kc = 0.08
triggered = delta_phi > kc
collapse_force = np.where(triggered, delta_phi**2, 0)

# Real turbulence field from RANS (ν_t)
real_turb = sim.nu_t
real_trigger = real_turb > 0.00001  # Heuristic threshold

# Match comparison
matches = (triggered == real_trigger)
match_percent = 100 * np.sum(matches) / matches.size
print(f"✓ Match accuracy with real RANS turbulence: {match_percent:.2f}%")

# Save CSV of comparison
with open("Collapse_vs_RANS.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["delta_phi", "collapse", "collapse_force", "nu_t", "RANS_turb", "match"])
    for i in range(delta_phi.size):
        writer.writerow([
            round(delta_phi[i], 5),
            triggered[i],
            round(collapse_force[i], 5),
            round(real_turb[i], 6),
            real_trigger[i],
            matches[i]
        ])

# Show visual comparison
plt.figure(figsize=(10,5))
plt.hist(delta_phi[triggered], bins=30, alpha=0.7, label="Symbolic Collapsed")
plt.hist(real_turb[real_trigger], bins=30, alpha=0.7, label="RANS Turbulent ν_t")
plt.title("Collapse vs RANS Turbulence Comparison")
plt.xlabel("Field Magnitude")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("Collapse_vs_RANS.png")
print("✓ Results saved to Collapse_vs_RANS.csv and Collapse_vs_RANS.png")