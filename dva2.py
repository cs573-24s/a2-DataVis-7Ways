import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
penguins = pd.read_csv("penglings.csv")

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(penguins["bill_length_mm"], penguins["flipper_length_mm"], alpha=0.6)
plt.title("Penguin Flipper Length vs Bill Length")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Flipper Length (mm)")
plt.grid(True)
plt.show()
