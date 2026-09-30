import numpy as np
import pandas as pd
data = {
    "Product": ["Pen", "Book", "Bag"],
    "Quantity": [10, 5, 3],
    "Price": [20, 100, 500]
}
df = pd.DataFrame(data)
df["Total"] = df["Quantity"] * df["Price"]
print("SALES DATA")
print(df)
sales = np.array(df["Total"])
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

best = df.loc[df["Total"].idxmax()]
print("Best Selling Product:", best["Product"])