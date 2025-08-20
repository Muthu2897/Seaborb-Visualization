import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer data
np.random.seed(42)
data = {
    "Segment": np.random.choice(["High Value", "Medium Value", "Low Value"], size=300),
    "PurchaseAmount": np.concatenate([
        np.random.normal(500, 50, 100),   # High Value
        np.random.normal(300, 40, 100),   # Medium Value
        np.random.normal(150, 30, 100)    # Low Value
    ])
}

df = pd.DataFrame(data)

# Create figure sized 512x512 pixels (8x8 inches at 64 dpi)
plt.figure(figsize=(8, 8))

# Create Seaborn boxplot
sns.boxplot(
    x="Segment",
    y="PurchaseAmount",
    data=df,
    palette="Set2"
)

# Add labels and title
plt.title("Purchase Amount Distribution by Customer Segment", fontsize=14, weight="bold")
plt.xlabel("Customer Segment", fontsize=12)
plt.ylabel("Purchase Amount ($)", fontsize=12)

# Save chart as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
