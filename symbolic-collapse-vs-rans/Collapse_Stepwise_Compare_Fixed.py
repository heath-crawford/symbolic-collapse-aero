import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt

# Load simulation
mesh = pv.read(r'C:/Users/heath_b8o4sl3/AEROSPACE_PROOF/AirfRANS_Data/Dataset/airFoil2D_SST_31.283_-4.156_0.919_6.98_14.32/airFoil2D_SST_31.283_-4.156_0.919_6.98_14.32_internal.vtu')
velocity = mesh['U']
nut = mesh['nut']

# Compute symbolic collapse from velocity magnitude
mag = np.linalg.norm(velocity, axis=1)
field = (mag - mag.min()) / (mag.max() - mag.min()) * 0.3

kc = 0.3
collapse = field > kc
collapse_force = np.where(collapse, field**2, 0)
real_turb = nut > 1e-5

# Stepwise comparison
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].scatter(range(len(field)), field, s=1, label='Field', color='blue')
ax[0].scatter(np.where(collapse)[0], field[collapse], s=1, label='Collapse', color='red')
ax[0].set_title('Symbolic Collapse Field')
ax[0].legend()

ax[1].scatter(np.where(real_turb)[0], field[real_turb], s=1, label='RANS Turbulent', color='orange')
ax[1].scatter(np.where(~real_turb)[0], field[~real_turb], s=1, label='RANS Laminar', color='green')
ax[1].set_title('RANS Turbulence Map')
ax[1].legend()

plt.tight_layout()
plt.savefig("Collapse_Stepwise_Compare.png")
plt.show()

# Print overlap score
matches = (collapse == real_turb)
score = 100 * np.sum(matches) / len(matches)
print(f"✓ Collapse match with RANS turbulence: {score:.2f}%")