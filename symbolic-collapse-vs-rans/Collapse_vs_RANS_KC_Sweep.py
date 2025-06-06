import numpy as np
import matplotlib.pyplot as plt
import time

# Simulated symbolic velocity field
np.random.seed(42)
N = 10000
velocity = np.random.rand(N, 2) * 100
symbolic_field = np.linalg.norm(velocity, axis=1)
symbolic_field = (symbolic_field - symbolic_field.min()) / (symbolic_field.max() - symbolic_field.min()) * 0.3

# Simulated real turbulence mask
real_turbulence = np.random.rand(N) > 0.7

kc_values = np.linspace(0.01, 0.5, 100)
best_kc = 0
best_match = 0
match_history = []

start = time.time()
for kc in kc_values:
    triggered = symbolic_field > kc
    matches = triggered == real_turbulence
    accuracy = 100 * np.sum(matches) / N
    match_history.append((kc, accuracy))
    if accuracy > best_match:
        best_match = accuracy
        best_kc = kc
end = time.time()

print(f"✓ Best match accuracy: {best_match:.2f}% at kc = {best_kc:.4f}")
print(f"✓ Sweep completed in {end - start:.2f} seconds")

kcs, matches = zip(*match_history)
plt.plot(kcs, matches, label='Accuracy')
plt.axvline(best_kc, color='r', linestyle='--', label=f'Best κc = {best_kc:.4f}')
plt.title('Symbolic Collapse Match vs Synthetic Turbulence')
plt.xlabel('Collapse Threshold κc')
plt.ylabel('Match Accuracy (%)')
plt.legend()
plt.tight_layout()
plt.savefig("Collapse_vs_RANS_kc_sweep.png")
plt.show()