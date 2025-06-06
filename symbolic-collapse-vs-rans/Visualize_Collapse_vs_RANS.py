import pandas as pd
import matplotlib.pyplot as plt

# Load CSV results
df = pd.read_csv("Collapse_vs_RANS.csv")

# Match categories
df['Result'] = df['match'].apply(lambda x: 'Match' if x else 'Mismatch')

# Scatter plot of collapse force vs real ν_t
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df['collapse_force'], df['nu_t'],
    c=df['Result'].map({'Match': 'green', 'Mismatch': 'red'}),
    alpha=0.5, label=df['Result']
)

plt.title("Symbolic Collapse Force vs RANS Turbulent ν_t")
plt.xlabel("Symbolic Collapse Force (Fᴄ)")
plt.ylabel("RANS ν_t")
plt.grid(True)
plt.savefig("Collapse_Force_vs_RANS_nu_t.png")
print("✓ Visualization saved to Collapse_Force_vs_RANS_nu_t.png")