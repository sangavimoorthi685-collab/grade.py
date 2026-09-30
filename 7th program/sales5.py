import numpy as np
import pandas as pd

data = {
    "Name": ["Sangavi", "Ravi", "Kavi"],
    "Age": [20, 22, 21]
}

df = pd.DataFrame(data)

print("CUSTOMER DATA")
print(df)

age = np.array(df["Age"])

print("Total Age:", np.sum(age))
print("Average Age:", np.mean(age))
print("Highest Age:", np.max(age))
print("Lowest Age:", np.min(age))