import numpy as np
import pandas as pd
data = {
    "Product": ["Pen", "Book", "Bag"],
    "Price": [20, 100, 500]
}
df = pd.DataFrame(data)
print("PRODUCT DATA")
print(df)
price = np.array(df["Price"])
print("Total Price:", np.sum(price))
print("Average Price:", np.mean(price))
print("Highest Price:", np.max(price))
print("Lowest Price:", np.min(price))